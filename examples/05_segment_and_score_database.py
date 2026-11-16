"""ORCA-MI: build a segmentation database and a scoring database, then segment / refine / score them.

Run with any Python 3:  python 05_segment_and_score_database.py
(only the synthetic demo, DEMO = True, needs numpy and SimpleITK)
Put orcami.py next to this script or add the ORCA-MI folder to sys.path.

1. SEGMENTATION database   root / study / images      (or root / patient / study / images)
       observers segment every study with the same labels and can score it too;
       results: root/_segmentations/<study>/<user>.nii.gz + <user>.json (scores, times, computer),
       root/_segmentations/summary_<user>.csv and progress_<user>.log (time per study, ETA).
       A second observer can start from scratch, refine another observer's segmentation
       (e.g. a senior correcting a junior) or correct an nnU-Net result made in the background.
2. SCORING database        root / patient / configuration / images
       readers score each configuration (blinded), optionally next to a reference;
       results: root/_scores/<patient>/<config>_<reader>.json + summary CSV + progress log.

The same can be done without code: Tools -> "Segment a database..." and Tools -> "Score a database...".
"""
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

DEMO = True                                   # True: make small synthetic images; False: use PATIENTS below
WORK = Path(r"D:\orca_databases")             # where the two databases are created

# your own data (DEMO = False): one entry per patient, images by role
PATIENTS = {
    "patient_01": {"ct": r"D:\data\p01\ct.nii.gz", "pet": r"D:\data\p01\pet.nii.gz"},
    "patient_02": {"ct": r"D:\data\p02\ct_dicom_folder", "pet": r"D:\data\p02\pet_dicom_folder"},
}
# scoring: the configurations (e.g. reconstructions) to compare for each patient
CONFIGS = {
    "patient_01": {"reference": r"D:\data\p01\pet.nii.gz", "low_dose": r"D:\data\p01\pet_lowdose.nii.gz",
                   "ai_denoised": r"D:\data\p01\pet_ai.nii.gz"},
}

LABELS = [  # value, name, colour: the same for every observer
    {"value": 1, "name": "Lesion soft tissue", "color": [230, 40, 40]},
    {"value": 2, "name": "Lesion bone", "color": [40, 180, 60]},
    {"value": 3, "name": "Reference (liver)", "color": [50, 110, 240]},
]


def likert(name, desc, opts, required=True):
    return {"name": name, "description": desc, "kind": "Likert", "min": 1.0, "max": float(len(opts)),
            "options": opts, "required": required}


CRITERIA = [  # answered for every study while segmenting (leave [] for segmentation only)
    likert("Image quality", "Overall diagnostic quality", ["non-diagnostic", "poor", "fair", "good", "excellent"]),
    likert("Confidence", "Confidence in the segmentation", ["very low", "low", "medium", "high", "very high"]),
    {"name": "Lesions missed by AI", "description": "", "kind": "YesNo", "min": 0.0, "max": 1.0, "options": [],
     "required": False},
]


def put(src, dst):
    """Copy an image file or a DICOM folder into the database (hard link when possible: no extra disk space)."""
    src, dst = Path(src), Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        if not dst.exists():
            shutil.copytree(src, dst)
        return
    try:
        dst.unlink(missing_ok=True)
        dst.hardlink_to(src)
    except OSError:
        shutil.copy2(src, dst)


def make_demo():
    """Three patients with a CT and a PET showing two lesions; PET reconstructions for scoring."""
    import numpy as np
    import SimpleITK as sitk

    def save(a, p):
        p.parent.mkdir(parents=True, exist_ok=True)
        im = sitk.GetImageFromArray(a.astype(np.float32))
        im.SetSpacing((3.0, 3.0, 3.0))
        sitk.WriteImage(im, str(p))

    rng = np.random.default_rng(1)
    z, y, x = np.ogrid[:60, :80, :80]
    for k in range(1, 4):
        body = ((x - 40) ** 2 + (y - 40) ** 2 <= 33 ** 2)
        ct = np.where(body, 40.0, -1000.0) * np.ones((60, 1, 1))
        pet = np.where(body, 1.0, 0.0) * np.ones((60, 1, 1))
        for (cx, cy, cz, r, v) in [(30 + 3 * k, 35, 30, 5, 8.0), (52, 50 - 2 * k, 25, 4, 5.0)]:
            m = (x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2 <= r * r
            pet[m] = v
        save(ct, WORK / "src" / f"patient_{k:02d}" / "ct.nii.gz")
        save(pet, WORK / "src" / f"patient_{k:02d}" / "pet.nii.gz")
        save(pet + rng.normal(0, 0.4, pet.shape) * body, WORK / "src" / f"patient_{k:02d}" / "pet_lowdose.nii.gz")
        PATIENTS[f"patient_{k:02d}"] = {"ct": WORK / "src" / f"patient_{k:02d}" / "ct.nii.gz",
                                        "pet": WORK / "src" / f"patient_{k:02d}" / "pet.nii.gz"}
        CONFIGS[f"patient_{k:02d}"] = {"reference": WORK / "src" / f"patient_{k:02d}" / "pet.nii.gz",
                                       "low_dose": WORK / "src" / f"patient_{k:02d}" / "pet_lowdose.nii.gz"}


if DEMO:
    PATIENTS.clear()
    CONFIGS.clear()
    make_demo()

# ---------------------------------------------------------------- 1. segmentation database
SEG = WORK / "segmentation_db"
for patient, roles in PATIENTS.items():
    # image-1-ct, image-2-pet: a fixed order; PET is fused on the CT and gets the segmentation ("segment on: pet")
    for k, (role, src) in enumerate(roles.items(), start=1):
        suffix = "" if Path(src).is_dir() else "".join(Path(src).suffixes)
        put(src, SEG / patient / f"image-{k}-{role}{suffix}")
# the shared set-up (what Tools -> Segment a database writes when the first observer starts)
(SEG / "_segmentations").mkdir(parents=True, exist_ok=True)
(SEG / "_segmentations" / "segdb.json").write_text(json.dumps({
    "title": "Lesion segmentation",
    "instructions": "Segment every lesion; label the liver reference region.",
    "labels": LABELS,
    "segment_on": "pet",
    "anonymize": True,
    "fuse": True,
    "criteria": CRITERIA,
}, indent=2), encoding="utf-8")
print("segmentation database:", SEG)

# ---------------------------------------------------------------- 2. scoring database
SCORE = WORK / "scoring_db"
for patient, configs in CONFIGS.items():
    for config, src in configs.items():
        suffix = "" if Path(src).is_dir() else "".join(Path(src).suffixes)
        put(src, SCORE / patient / config / f"image-1-pet{suffix}")
print("scoring database:", SCORE)

# ---------------------------------------------------------------- 3. use them in ORCA-MI
v = om.Viewer()                                  # starts ORCA-MI (or connects to a running one)


def wait_study(timeout=60):
    """The study's images load in the viewer after the command returns: wait until it is shown."""
    import time
    for _ in range(int(timeout * 2)):
        info = [l for l in v.command("segdbinfo").get("log", []) if l.startswith("[segdb]")]
        if info and "current=Some" in info[0]:
            return info[0]
        time.sleep(0.5)
    return ""


# a junior observer segments (and scores) from scratch; stop any time, start again to continue
v.command(f"segdb {SEG}|user=Dr Junior")
print(wait_study())
# ... the observer works in the viewer; from a script the loaded study can be scored and saved:
v.command("segdbscore Image quality=4|Confidence=3")
v.command("segdbnext")                           # save this study, open the next one not done
v.command("segdbend")

# a senior refines the junior's segmentations: only the studies Dr Junior has done are shown
v.command(f"segdb {SEG}|user=Dr Senior|from=Dr Junior")
v.command("segdbend")

# start from an nnU-Net model (its name in the AI tab): it segments the studies in the background,
# each study opens with its prediction as soon as it is ready ("please wait" until then)
# v.command(f"segdb {SEG}|user=Dr C|nnunet=Lesions PET-CT")

# score the configurations (blinded, next to the reference)
v.command(f"scoredb {SCORE}|reference=reference|reader=Dr A|order=patient")
# ... score in the viewer (Scores tab), then:
# v.command("sessionend")

# ---------------------------------------------------------------- 4. read the results
for csv in sorted((SEG / "_segmentations").glob("summary_*.csv")):
    print(csv.name)
    print(csv.read_text(encoding="utf-8"))
for log in sorted((SEG / "_segmentations").glob("progress_*.log")):
    print(log.name, "\n", log.read_text(encoding="utf-8")[-600:])
