"""ORCA-MI: prepare a SEPARATE, SHAREABLE copy of a segmentation and / or scoring database.

Run with any Python 3:  python 07_prepare_copy_segment_score_database.py
(only the synthetic demo, DEMO = True, needs numpy)
Put orcami.py next to this script or add the ORCA-MI folder to sys.path.

Unlike example 05 (which may use hard links to save disk space), every image is COPIED into TARGET, so the
folder is self-contained: copy it to a USB disk or a shared drive and give it to the physicians.
Your original files are only read, never changed.

TARGET/
    README_for_physicians.txt        what to do (written by this script)
    segmentation_db/                 root / patient / image-1-ct, image-2-pet ...
        _segmentations/segdb.json    the shared set-up: labels, colours, questions (same for every observer)
    scoring_db/                      root / patient / configuration / image-1-pet ...
        session_<reader>.json        one ready-to-open reading session per physician (blinded, own order)
        <reader>.orcascore           each physician's shortcut (double-click it, or drop it on ORCA-MI)
        Everyone - choose your name.orcascore   asks who is scoring (a new reader gets a session too)
        scoredb.json                 the set-up (questions, view, readers)
    copy_log.csv                     every copied file: source, copy, size

Each physician needs ORCA-MI WITH A LICENCE (segmenting / scoring a database is not part of the 7-day trial;
the licence is free: Help -> Licence -> Request your free licence) and the TARGET folder:
    segmentation: double-click TARGET/segmentation_db/<their name> - segmentation.orcaseg (or drop it onto ORCA-MI)
    scoring:      double-click TARGET/scoring_db/<their name>.orcascore (or drop it onto ORCA-MI)
Results are written inside the folder (_segmentations, _scores): collect the folder (or just those two
sub-folders) back from every physician and read them with ORCA-MI (Scores tab -> Results -> Load results folder).
"""
import csv
import json
import shutil
import sys
from pathlib import Path

# orcami.py: next to this script, in the ORCA-MI folder above it, or in the installed ORCA-MI
import os
for _d in (Path(__file__).resolve().parent, Path(__file__).resolve().parent.parent,
           Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "ORCA-MI",
           Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "ORCA-MI"):
    if (_d / "orcami.py").is_file():
        sys.path.insert(0, str(_d))
        break
import orcami as om

DEMO = True                                     # True: make three small synthetic patients; False: your data below
TARGET = Path(r"D:\shared_reading_study")       # the folder to give to the physicians (created)
MAKE_SEGMENTATION_DB = True
MAKE_SCORING_DB = True
MAKE_ZIP = False                                # also write TARGET.zip (one file to send)

READERS = ["Dr A", "Dr B", "Dr C"]              # one session file per physician (scoring)
REFERENCE = "reference"                         # configuration shown next to every other one ("" = none)
ORDER = "patient"                               # "patient" (configurations shuffled per patient), "random", "inorder"
LAYOUT = "auto"                                 # with a reference: "side", "2x2", "dualmpr"; without: "one", "mpr"
BASE = "anatomical"                             # "anatomical" (CT base, PET/SPECT fused), "functional", "functional_only"
VIEW_3D = "functional"                          # MPR layouts: the 3D view shows "functional" or "anatomical"
TITLE = "Lesion segmentation"
INSTRUCTIONS = "Segment every lesion; label the liver reference region."

# your own data (DEMO = False): one entry per patient, images by role (files or DICOM folders).
# The patient names become folder names that the physicians see: use study codes, never real patient names.
# DICOM folders are copied as they are (with their patient tags): anonymise them first, or use NIfTI files.
PATIENTS = {
    "patient_01": {"ct": r"D:\data\p01\ct.nii.gz", "pet": r"D:\data\p01\pet.nii.gz"},
    "patient_02": {"ct": r"D:\data\p02\ct_dicom_folder", "pet": r"D:\data\p02\pet_dicom_folder"},
}
SEGMENT_ON = "pet"                              # the role that receives the segmentation

# segmentation: earlier label maps (NIfTI) given to the readers as a starting point to refine or clean, e.g. a public
# dataset or a former manual segmentation. The readers then start from them ("observer PRIOR_NAME").
PRIOR_NAME = ""                                 # e.g. "Public dataset" ("" = the readers start from an empty segmentation)
PRIOR_SEGMENTATIONS = {}                        # patient -> label map, e.g. {"patient_01": r"D:\labels\p01.nii.gz"}
SEG_READERS = READERS                           # one segmentation shortcut per reader (double-click to start)
# segmentation: what the readers see (the same for everyone)
SEG_LAYOUT = "mpr"                              # "mpr" (axial, sagittal, coronal + 3D), "one" (one axial view), "auto"
SEG_BASE = "segmented"                          # main image: "segmented" (the image to segment, the other fused on it),
#                                                 "anatomical" (CT under), "functional" (SPECT under), "functional_only"
SEG_VIEW_3D = "functional"                      # image in the 3D view: "functional" | "anatomical"
SEG_COLORMAP_FUNCTIONAL = "Hot iron"            # PET / SPECT colormap ("" = as loaded)
SEG_COLORMAP_ANATOMICAL = "Grayscale"           # CT / MR colormap
# scoring: the configurations (e.g. reconstructions) to compare for each patient; every image of a configuration
# is listed by role (a CT with each configuration lets ORCA-MI fuse the PET on it)
CONFIGS = {
    "patient_01": {"reference": {"pet": r"D:\data\p01\pet.nii.gz", "ct": r"D:\data\p01\ct.nii.gz"},
                   "low_dose": {"pet": r"D:\data\p01\pet_lowdose.nii.gz", "ct": r"D:\data\p01\ct.nii.gz"},
                   "ai_denoised": {"pet": r"D:\data\p01\pet_ai.nii.gz", "ct": r"D:\data\p01\ct.nii.gz"}},
}

LABELS = [  # value, name, colour: the same for every observer
    {"value": 1, "name": "Lesion soft tissue", "color": [230, 40, 40]},
    {"value": 2, "name": "Lesion bone", "color": [40, 180, 60]},
    {"value": 3, "name": "Reference (liver)", "color": [50, 110, 240]},
]


def likert(name, desc, opts, required=True):
    return {"name": name, "description": desc, "kind": "Likert", "min": 1.0, "max": float(len(opts)),
            "options": opts, "required": required}


SEG_QUESTIONS = [  # answered for every study while segmenting ([] = segmentation only)
    likert("Image quality", "Overall diagnostic quality", ["non-diagnostic", "poor", "fair", "good", "excellent"]),
    likert("Confidence", "Confidence in the segmentation", ["very low", "low", "medium", "high", "very high"]),
]
SCORE_QUESTIONS = [  # scoring questions of every configuration ([] = ORCA-MI's default for the reference design:
    # similarity to the reference, confidence, differences)
    likert("Image quality", "Overall diagnostic quality", ["non-diagnostic", "poor", "fair", "good", "excellent"]),
    likert("Lesion detectability", "How well are lesions seen?", ["not seen", "poor", "fair", "good", "excellent"]),
    likert("Noise", "Image noise", ["unacceptable", "high", "moderate", "low", "none"]),
    {"name": "Diagnostic decision changed", "description": "Compared with the reference", "kind": "YesNo",
     "min": 0.0, "max": 1.0, "options": [], "required": False},
]

LOG = []


def suffix(p):
    p = Path(p)
    return "" if p.is_dir() else "".join(p.suffixes)


def copy(src, dst):
    """A real copy (file or DICOM folder); an existing identical copy is kept (the script can be re-run)."""
    src, dst = Path(src), Path(dst)
    if not src.exists():
        raise FileNotFoundError(f"missing: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    files = [f for f in src.rglob("*") if f.is_file()] if src.is_dir() else [src]
    for f in files:
        d = dst / f.relative_to(src) if src.is_dir() else dst
        if not (d.exists() and d.stat().st_size == f.stat().st_size):
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, d)
        if d.stat().st_size != f.stat().st_size:
            raise IOError(f"copy incomplete: {d}")
        LOG.append((str(f), str(d), f.stat().st_size))


def make_demo():
    """Three patients: CT, PET with two lesions, and a noisier low-dose PET."""
    import numpy as np
    src = TARGET.parent / (TARGET.name + "_demo_source")
    rng = np.random.default_rng(1)
    x, y, z = np.ogrid[:80, :80, :60]
    for k in range(1, 4):
        body = (x - 40) ** 2 + (y - 40) ** 2 <= 33 ** 2
        ct = np.where(body, 40.0, -1000.0) * np.ones((1, 1, 60))
        pet = np.where(body, 1.0, 0.0) * np.ones((1, 1, 60))
        for (cx, cy, cz, r, v) in [(30 + 3 * k, 35, 30, 5, 8.0), (52, 50 - 2 * k, 25, 4, 5.0)]:
            pet[(x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2 <= r * r] = v
        p = src / f"patient_{k:02d}"
        p.mkdir(parents=True, exist_ok=True)
        low = pet + rng.normal(0, 0.4, pet.shape) * body
        for arr, name in ((ct, "ct"), (pet, "pet"), (low, "pet_lowdose")):
            om.write_nifti(str(p / f"{name}.nii.gz"), arr.astype(np.float32), spacing=(3.0, 3.0, 3.0))
        PATIENTS[p.name] = {"ct": p / "ct.nii.gz", "pet": p / "pet.nii.gz"}
        CONFIGS[p.name] = {"reference": {"pet": p / "pet.nii.gz", "ct": p / "ct.nii.gz"},
                           "low_dose": {"pet": p / "pet_lowdose.nii.gz", "ct": p / "ct.nii.gz"}}


if DEMO:
    PATIENTS.clear()
    CONFIGS.clear()
    make_demo()

# check everything first: nothing is copied when a source is missing
missing = [str(s) for roles in PATIENTS.values() for s in roles.values() if not Path(s).exists()] if MAKE_SEGMENTATION_DB else []
if MAKE_SCORING_DB:
    missing += [str(s) for cfgs in CONFIGS.values() for roles in cfgs.values() for s in roles.values() if not Path(s).exists()]
if missing:
    sys.exit("Missing source files / folders:\n  " + "\n  ".join(missing))
TARGET.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- 1. segmentation database (copies)
if MAKE_SEGMENTATION_DB:
    SEG = TARGET / "segmentation_db"
    for patient, roles in PATIENTS.items():
        # image-1-ct, image-2-pet: a fixed order for every patient
        for k, (role, src) in enumerate(roles.items(), start=1):
            copy(src, SEG / patient / f"image-{k}-{role}{suffix(src)}")
    (SEG / "_segmentations").mkdir(parents=True, exist_ok=True)
    (SEG / "_segmentations" / "segdb.json").write_text(json.dumps({
        "title": TITLE, "instructions": INSTRUCTIONS, "labels": LABELS, "segment_on": SEGMENT_ON,
        "anonymize": True, "fuse": True, "criteria": SEG_QUESTIONS,
        "view_layout": SEG_LAYOUT, "view_base": SEG_BASE, "view_3d": SEG_VIEW_3D,
        "cmap_functional": SEG_COLORMAP_FUNCTIONAL, "cmap_anatomical": SEG_COLORMAP_ANATOMICAL,
    }, indent=2), encoding="utf-8")
    # earlier segmentations, saved as if an observer called PRIOR_NAME had made them
    if PRIOR_NAME and PRIOR_SEGMENTATIONS:
        safe = lambda s: "".join(c if c.isalnum() or c in "-_." else "_" for c in s.strip()) or "user"
        for patient, lab in PRIOR_SEGMENTATIONS.items():
            if patient not in PATIENTS:
                sys.exit(f"PRIOR_SEGMENTATIONS: {patient} is not in PATIENTS")
            d = SEG / "_segmentations" / safe(patient)
            copy(lab, d / f"{safe(PRIOR_NAME)}.nii.gz")
            (d / f"{safe(PRIOR_NAME)}.json").write_text(json.dumps({
                "title": TITLE, "user": PRIOR_NAME, "study": patient, "start_from": "imported", "labels": LABELS,
                "comments": f"imported from {lab}"}, indent=2), encoding="utf-8")
        print(f"  {len(PRIOR_SEGMENTATIONS)} earlier segmentations imported as '{PRIOR_NAME}'")
    # shortcuts: one per reader + one for everyone (asks the name); double-click, or drop onto ORCA-MI
    start = f"observer:{PRIOR_NAME}" if PRIOR_NAME and PRIOR_SEGMENTATIONS else "empty"
    short = lambda s: "".join(c if c.isalnum() or c in " -_." else "_" for c in s).strip()
    for r in list(SEG_READERS) + [""]:
        name = f"{short(r)} - segmentation" if r else "Everyone - segmentation (choose your name)"
        (SEG / f"{name}.orcaseg").write_text(json.dumps({"orcami": "segmentation", "title": TITLE, "session": "",
                                                          "user": r, "start": start}, indent=2), encoding="utf-8")
    print("segmentation database:", SEG, f"({len(PATIENTS)} patients)")

# ---------------------------------------------------------------- 2. scoring database (copies + reader sessions)
if MAKE_SCORING_DB:
    SCORE = TARGET / "scoring_db"
    for patient, configs in CONFIGS.items():
        for config, roles in configs.items():
            for k, (role, src) in enumerate(roles.items(), start=1):
                copy(src, SCORE / patient / config / f"image-{k}-{role}{suffix(src)}")
    print("scoring database:", SCORE, f"({len(CONFIGS)} patients)")
    # ORCA-MI writes one portable session file per reader (paths relative to scoring_db: they keep working
    # wherever the folder is copied); it starts in the background and closes again
    crit = TARGET / "scoring_db" / "scoring_questions.json"
    crit.write_text(json.dumps(SCORE_QUESTIONS, indent=2), encoding="utf-8")
    line = f"scoredb {SCORE}|reader={','.join(READERS)}|order={ORDER}|layout={LAYOUT}|base={BASE}|view3d={VIEW_3D}|title={TITLE}|save=1"
    if REFERENCE:
        line += f"|reference={REFERENCE}"
    if SCORE_QUESTIONS:
        line += f"|criteria={crit}"
    v = om.Viewer()
    for l in v.command(line).get("log", []):
        if l.startswith("[scoredb] session "):
            print("  reader session:", l[len("[scoredb] session "):])
    v.close(quit_viewer=v.proc is not None)      # quit ORCA-MI only when this script started it

# ---------------------------------------------------------------- 3. instructions, log, zip
with open(TARGET / "copy_log.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["source", "copy", "bytes"])
    w.writerows(LOG)
total = sum(b for _, _, b in LOG)
lines = [f"{TITLE}", "", "You need ORCA-MI (installer or portable zip) with a licence, and this whole folder.",
         "The licence is free for research: in ORCA-MI, Help -> Licence -> Request your free licence, then load the",
         "file you receive (segmenting and scoring a database are not part of the 7-day trial).", ""]
if MAKE_SEGMENTATION_DB:
    lines += ["SEGMENTATION", "  ORCA-MI: Tools -> Segment a database... -> choose the folder 'segmentation_db' -> type your name.",
              "  " + INSTRUCTIONS, "  You can stop at any time; start again to continue where you stopped.", ""]
if MAKE_SCORING_DB:
    lines += ["SCORING", "  Double-click 'scoring_db/<your name>.orcascore' (or drop it onto the ORCA-MI window).",
              "  Not in the list? Use 'scoring_db/Everyone - choose your name.orcascore' and type your name.",
              "  Cases are blinded and in your own order. Score every case, then 'Next'.", ""]
lines += ["WHEN YOU ARE DONE", "  Send the folder back (or only 'segmentation_db/_segmentations' and 'scoring_db/_scores').",
          "  Do not rename or move the image folders."]
(TARGET / "README_for_physicians.txt").write_text("\r\n".join(lines) + "\r\n", encoding="utf-8")
print(f"{len(LOG)} files, {total / 1e6:.1f} MB copied to {TARGET}")

if MAKE_ZIP:
    z = shutil.make_archive(str(TARGET), "zip", root_dir=TARGET.parent, base_dir=TARGET.name)
    print("zip:", z)
print("Ready to share:", TARGET)
