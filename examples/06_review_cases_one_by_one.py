"""ORCA-MI: show a series of cases one by one (image, fused image, segmentation, colormaps, layout ...).

Run with any Python 3:  python 06_review_cases_one_by_one.py
(only the synthetic demo, DEMO = True, needs numpy)
Put orcami.py next to this script or add the ORCA-MI folder to sys.path.

Each case is shown with view(...); in this console press
    Enter = next case    b = back    r = show again    s = save a snapshot (PNG)    q = quit
ORCA-MI stays fully usable meanwhile (scroll, zoom, change the window, measure ...).
"""
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

DEMO = True                                     # True: make three small synthetic cases; False: use CASES below
SNAPSHOTS = Path(r"D:\orca_review\snapshots")   # where "s" saves the screen of a case

# your own cases (DEMO = False): any of image / fused / seg can be a NIfTI file, a DICOM folder, ...
CASES = [
    {"name": "patient_01", "image": r"D:\data\p01\ct.nii.gz", "fused": r"D:\data\p01\pet.nii.gz",
     "seg": r"D:\data\p01\lesions.nii.gz"},
    {"name": "patient_02", "image": r"D:\data\p02\ct_dicom_folder", "fused": r"D:\data\p02\pet_dicom_folder",
     "seg": r"D:\data\p02\lesions.nii.gz", "fused_colormap": "pet"},           # per-case settings win
    {"name": "patient_03", "image": r"D:\data\p03\pet.nii.gz", "seg": r"D:\data\p03\lesions.nii.gz",
     "colormap": "hot iron", "window": (0, 10), "layout": "1x3"},              # a single image, no fusion
]

# settings used for every case unless the case sets its own
DEFAULTS = {
    "colormap": "grayscale",          # colormap of the image ("grayscale", "hot iron", "pet", "jet", "viridis" ...)
    "window": (-160, 240),            # display window of the image (lo, hi); None = automatic
    "fused_colormap": "hot iron",     # colormap of the fused image
    "fused_opacity": 0.5,             # 0..1
    "fused_window": (0, 8),           # e.g. SUV 0..8; None = automatic
    "seg_palette": "distinct",        # "distinct", a colormap name, "#ff0000", "red" or an (r, g, b) tuple
    "seg_opacity": 0.4,               # 0..1
    "seg_outline": True,              # outlines (True) or filled labels (False)
    "labels": {1: "Lesion", 2: "Liver reference"},  # label names (value: name); None = keep the file's
    "layout": "mpr",                  # 1, 1x2, 2x1, 2x2, 1x3, 3x3, 4x4, 5x5, 1+3, mpr, dualmpr
    "go_to_seg": True,                # crosshair to the centre of the segmentation: True = all labels, 1 = label 1, ...
}


def view(v, image, fused=None, seg=None, colormap=None, window=None, fused_colormap=None, fused_opacity=None,
         fused_window=None, seg_palette=None, seg_opacity=None, seg_outline=None, labels=None, layout=None,
         go_to_seg=None, name=None):
    """Show one case: the previous one is closed first. Returns the image's index in ORCA-MI."""
    v.closeall()
    img = v.load(image, colormap=colormap, window=window, name=name)
    if fused is not None:
        v.overlay(fused, colormap=fused_colormap, opacity=fused_opacity, window=fused_window)
    if seg is not None:
        v.segmentation(seg, palette=seg_palette, opacity=seg_opacity, labels=labels)
        if seg_outline is not None:
            v.segoutline("on" if seg_outline else "off")
    if layout:
        v.layout(layout)
    if seg is not None and go_to_seg:
        v.command("gotoseg" if go_to_seg is True else f"gotoseg {int(go_to_seg)}")
    return img.get("index", 0)


def make_demo():
    """Three cases: a CT-like body, a PET with two lesions and their segmentation."""
    import numpy as np
    out = SNAPSHOTS.parent / "demo"
    x, y, z = np.ogrid[:80, :80, :60]
    for k in range(1, 4):
        body = (x - 40) ** 2 + (y - 40) ** 2 <= 33 ** 2
        ct = np.where(body, 40.0, -1000.0) * np.ones((1, 1, 60))
        pet = np.where(body, 1.0, 0.0) * np.ones((1, 1, 60))
        seg = np.zeros(ct.shape, np.uint8)
        for value, (cx, cy, cz, r, suv) in enumerate([(28 + 4 * k, 34, 30, 5, 6.0 + k), (54, 48, 22, 7, 1.8)], start=1):
            m = (x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2 <= r * r
            pet[m] = suv
            seg[m] = value
        case = out / f"case_{k:02d}"
        case.mkdir(parents=True, exist_ok=True)
        for arr, fname in ((ct, "ct"), (pet, "pet"), (seg, "seg")):
            om.write_nifti(str(case / f"{fname}.nii.gz"), arr.astype(np.uint8 if fname == "seg" else np.float32),
                           spacing=(3.0, 3.0, 3.0))
        CASES.append({"name": f"case_{k:02d}", "image": case / "ct.nii.gz", "fused": case / "pet.nii.gz",
                      "seg": case / "seg.nii.gz"})


if DEMO:
    CASES.clear()
    make_demo()

v = om.Viewer()                                 # starts ORCA-MI (or connects to a running one)
i = 0
while 0 <= i < len(CASES):
    case = {**DEFAULTS, **CASES[i]}
    paths = {k: str(case[k]) if case.get(k) is not None else None for k in ("image", "fused", "seg")}
    print(f"\n[{i + 1}/{len(CASES)}] {case['name']}")
    try:
        view(v, paths["image"], paths["fused"], paths["seg"], case["colormap"], case["window"],
             case["fused_colormap"], case["fused_opacity"], case["fused_window"], case["seg_palette"],
             case["seg_opacity"], case["seg_outline"], case["labels"], case["layout"], case["go_to_seg"], case["name"])
    except om.OrcaMIError as e:
        print("  could not show this case:", e)
    while True:
        key = input("  Enter = next, b = back, r = again, s = snapshot, q = quit: ").strip().lower()
        if key == "s":                          # save the screen and stay on this case
            SNAPSHOTS.mkdir(parents=True, exist_ok=True)
            # the whole viewing area as displayed (add "axial", "coronal", "sagittal", "3d" for clean renders)
            for f in v.export_images(str(SNAPSHOTS), items=["layout"], png=True, size=1600, prefix=case["name"]):
                print("  saved", f)
            continue
        break
    if key == "q":
        break
    if key == "b":
        i = max(0, i - 1)
    elif key != "r":
        i += 1
print("done")
