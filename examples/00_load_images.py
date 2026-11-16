"""ORCA-MI: the simplest ways to load images from Python.

Run with any Python 3:  python 00_load_images.py
(the synthetic demo, DEMO = True, needs numpy; SimpleITK images work too when SimpleITK is installed)
Put orcami.py next to this script or add the ORCA-MI folder to sys.path.

What can be loaded:
    a file path       NIfTI (.nii / .nii.gz), NRRD, MHA / MHD, a DICOM folder, ...
    a numpy array     with its voxel spacing (axes="zyx" for arrays from SimpleITK, "xyz" for nibabel)
    a SimpleITK image (its spacing, origin and direction are kept)
    a nibabel image
Roles: "image" (shown in the views), "overlay" (fused on the image, in every view) and "seg" (a label map:
0 = background, 1, 2, ... = labels, on the grid of the image).
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

DEMO = True        # True: three small synthetic PET/CT cases made with numpy; False: your files in CASES

# your own cases (DEMO = False): files or DICOM folders; "seg" may be left out
CASES = [
    {"ct": r"D:\data\patient_01\ct.nii.gz", "pet": r"D:\data\patient_01\pet.nii.gz", "seg": r"D:\data\patient_01\lesions.nii.gz"},
    {"ct": r"D:\data\patient_02\ct_dicom_folder", "pet": r"D:\data\patient_02\pet_dicom_folder"},
]


def synthetic_case(k):
    """A CT-like body, a PET with one hot lesion and the lesion's label map (numpy arrays, z, y, x)."""
    import numpy as np
    z, y, x = np.ogrid[:60, :96, :96]
    body = ((x - 48) ** 2 + (y - 48) ** 2 <= 40 ** 2) & (z >= 0)
    ct = np.where(body, 40.0, -1000.0).astype(np.float32)
    pet = np.where(body, 1.0, 0.0).astype(np.float32)
    lesion = (x - 30 - 6 * k) ** 2 + (y - 40) ** 2 + (z - 30) ** 2 <= 6 ** 2
    pet[lesion] = 6.0 + 2 * k
    return ct, pet, lesion.astype(np.uint8)


v = om.Viewer()    # starts ORCA-MI, or connects to the one that is open

n = 3 if DEMO else len(CASES)
for k in range(n):
    v.closeall()                                         # the previous case is closed
    if DEMO:
        ct, pet, seg = synthetic_case(k)
        geometry = dict(spacing=(3.0, 3.0, 3.0), axes="zyx")   # 3 mm voxels, numpy (z, y, x) order
        v.load(ct, name=f"CT {k + 1}", window=(-160, 240), **geometry)
        pet_reply = v.load(pet, role="overlay", name=f"PET {k + 1}", colormap="pet dicom", opacity=0.5, **geometry)
        v.load(seg, role="seg", name="Lesion", labels={1: "Lesion"}, **geometry)
    else:
        case = CASES[k]
        v.load(case["ct"], window=(-160, 240))
        pet_reply = v.load(case["pet"], role="overlay", colormap="pet dicom", opacity=0.5)
        if case.get("seg"):
            v.load(case["seg"], role="seg")
    v.layout("mpr")                                      # axial, sagittal, coronal and 3D
    v.command("showall 0")                               # the CT in every view of the layout
    v.command(f"fuseall {pet_reply['index']}|opacity=0.5")   # the PET fused on every view
    v.command("gotoseg", check=False)                    # crosshair to the lesion (if there is a segmentation)

    # SimpleITK works the same way:  import SimpleITK as sitk;  v.load(sitk.ReadImage("ct.nii.gz"))

    key = input(f"case {k + 1}/{n}: Enter = next, q = quit: ").strip().lower()
    if key == "q":
        break
print("done")
