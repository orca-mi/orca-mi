"""ORCA-MI quick start: load a PET/CT with a segmentation, measure, export figures.

Run with any Python 3 (no extra packages needed):  python 01_quick_start.py
Put orcami.py next to this script or add the ORCA-MI folder to sys.path.
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

CT = r"D:\data\patient_01\ct.nii.gz"
PET = r"D:\data\patient_01\pet_suv.nii.gz"
SEG = r"D:\data\patient_01\lesions.nii.gz"      # label 1 = lesion (drawn on the CT grid)
OUT = r"D:\figures\patient_01"

v = om.Viewer()                                  # starts ORCA-MI (or connects to a running one)
v.load(CT)                                       # image 0
v.load(PET, role="overlay", colormap="hot iron", opacity=0.5)   # image 1, fused on the CT
v.load(SEG, role="seg")                          # segmentation of the CT
v.layout("mpr")                                  # axial, sagittal, coronal + 3D

# volume, SUVmean, SUVmax, SUVpeak, TLG - measured on the PET (image 1), each lesion separately
for r in v.stats(value_image=1, split=True):
    print(f"{r['name']:<12} MTV {r['volume_ml']:8.2f} mL  SUVmean {r['mean']:6.2f}  "
          f"SUVmax {r['max']:6.2f}  SUVpeak {r['peak']:6.2f}  TLG {r['tlg']:8.1f}")

# presentation images: the screen as displayed, clean planes, 3D, and GIFs
files = v.export_images(OUT, items=["layout", "axial", "coronal", "sagittal", "3d", "gif3d", "gifcoronal"],
                        quality=95, size=1536, gif_delay_ms=60, gif_frames=48)
print("\n".join(files))
