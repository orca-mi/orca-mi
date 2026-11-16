"""Batch: crop every patient to lungs + liver (head-feet only, 20 mm margin above, 10 mm below), save the
cropped images and export presentation figures + GIFs for each patient.

Segmentation with organ names, e.g. from TotalSegmentator (labels contain "lung" and "liver").
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

ROOT = Path(r"D:\study")
FIG = ROOT / "_figures"

with om.Viewer() as v:
    for pdir in sorted(p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith("_")):
        ct, pet, organs = pdir / "ct.nii.gz", pdir / "pet_suv.nii.gz", pdir / "organs.nii.gz"
        if not ct.exists():
            continue
        v.closeall()
        v.load(str(ct), window=(-160, 240))                                  # soft-tissue window
        if pet.exists():
            v.load(str(pet), role="overlay", colormap="hot iron", opacity=0.45)
        if organs.exists():
            v.load(str(organs), role="seg", palette="distinct", opacity=0.35)

        # crop CT, PET (and anything else loaded) to the same physical box:
        #   box around every voxel of "lung*" and "liver" labels, only along head-feet (S-I),
        #   +20 mm superior, +10 mm inferior; left-right and anterior-posterior are kept whole.
        new = v.crop_to_segments(["lung", "liver"], margins={"S": 20, "I": 10}, axes="SI", replace=True)
        print(pdir.name, "cropped images:", new)

        v.save_image(str(pdir / "ct_cropped.nii.gz"))                       # active image (the cropped CT)

        v.layout("mpr")
        v.mode3d("mip")                                                     # 3D view as a MIP
        v.export_images(str(FIG / pdir.name),
                        items=["layout", "coronal", "sagittal", "3d", "gif3d", "gifcoronal"],
                        quality=92, size=1280, gif_size=480, gif_delay_ms=70, gif_frames=60,
                        prefix=pdir.name)

# Other ways to crop:
#   v.crop_box(x=(100, 400), y=(80, 420), z=(30, 200))               # voxel box of the active image
#   v.crop_to_segments(margin=15)                                     # all labels, 15 mm on every side
#   v.crop_to_segments(["kidney"], margins={"R": 5, "L": 5}, axes="LR,AP,SI", all_images=False)
