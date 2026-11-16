"""ORCA-MI example 4: time-activity curves.

A) Dynamic PET (one 4D series): motion correction, TAC per segment, Patlak Ki with an aorta input function.
B) Therapy SPECT at several time points: registration, TAC, effective half-life and time-integrated activity.

Edit the paths, then run:  python 04_dynamic_and_time_points.py
"""
import os
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

v = om.Viewer()
v.closeall()

# ---------------------------------------------------------------- A) dynamic PET
DYNAMIC = r"D:\data\patient01\dynamic_pet"          # DICOM folder or 4D NIfTI
ROIS = r"D:\data\patient01\rois.nii.gz"              # label 1 = aorta, 2 = tumour, … (on the PET grid)
if os.path.exists(DYNAMIC):
    v.command(f"loaddicom {DYNAMIC}") if os.path.isdir(DYNAMIC) else v.load(DYNAMIC)
    v.load(ROIS, role="seg", labels={1: "aorta", 2: "tumour"})
    r = v.dynamic_tac(frames=0,                 # image index of the 4D image
                      reference=20,             # a late frame (0-based index) as the motion reference
                      register=True, register_from=10,
                      input_label=1, t_star=10,  # Patlak from 10 min on
                      csv="dynamic_tac.csv", ki_map=True)
    for p in r["patlak"]:
        print(f"{p['name']}: Ki = {p['ki']:.5f} /min, V0 = {p['v0']:.3f}, r² = {p['r2']:.3f}")

# ---------------------------------------------------------------- B) SPECT time points
TIME_POINTS = [r"D:\data\patient02\spect_4h", r"D:\data\patient02\spect_24h", r"D:\data\patient02\spect_72h"]
KIDNEYS = r"D:\data\patient02\kidneys_on_4h.nii.gz"
if all(os.path.exists(p) for p in TIME_POINTS):
    v.closeall()
    for p in TIME_POINTS:
        v.command(f"loaddicom {p}") if os.path.isdir(p) else v.load(p)
    v.load(KIDNEYS, role="seg", labels={1: "kidney_left", 2: "kidney_right"})
    r = v.dynamic_tac(images=[0, 1, 2], reference=0, register=True,
                      times=[4, 24, 72], time_unit="h",   # or leave out: read from DICOM
                      tail_points=2, csv="spect_kinetics.csv")
    for k in r["kinetics"]:
        print(f"{k['name']}: effective half-life {k['half_life']:.1f} h, TIA {k['tia']:.3e} (total × h)")
