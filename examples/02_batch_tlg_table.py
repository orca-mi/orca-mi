"""Batch: MTV / SUVmean / SUVmax / SUVpeak / TLG for every patient -> one CSV.

Folder layout (one folder per patient):
    D:/study/
        patient_001/  ct.nii.gz  pet_suv.nii.gz  lesions.nii.gz
        patient_002/  ...
"""
import csv
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

ROOT = Path(r"D:\study")
OUT_CSV = ROOT / "tlg_results.csv"

rows = []
with om.Viewer() as v:                                   # the viewer closes at the end
    for pdir in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        ct, pet, seg = pdir / "ct.nii.gz", pdir / "pet_suv.nii.gz", pdir / "lesions.nii.gz"
        if not (ct.exists() and pet.exists() and seg.exists()):
            print("skipped (missing files):", pdir.name)
            continue
        v.closeall()
        v.load(str(ct))
        v.load(str(pet), role="overlay")                 # image index 1
        v.load(str(seg), role="seg")
        whole = v.stats(value_image=1)                   # per label
        lesions = v.stats(value_image=1, split=True)     # per connected lesion
        for r in whole:
            rows.append({"patient": pdir.name, "structure": r["name"], "level": "label", **r})
        for r in lesions:
            rows.append({"patient": pdir.name, "structure": r["name"], "level": "lesion", **r})
        print(pdir.name, "total TLG:", round(sum(r["tlg"] for r in whole), 1))

keys = ["patient", "level", "structure", "volume_ml", "mean", "max", "peak", "tlg", "std", "min", "median", "voxels"]
with open(OUT_CSV, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
print("saved", OUT_CSV)
