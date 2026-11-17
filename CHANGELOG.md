# Changelog

## 0.1.0 — 2026-11-16

First public version.

* Session recording for training videos (MP4 with microphone, camera picture-in-picture, pointer, pressed keys,
  watermark, four qualities up to 3840 px / 30 fps); 🎞 picture viewer for GIFs (play, pause, speed, zoom).
* French interface; menus by category; colormap on right-click of any image; NEMA IEC window size.
* Python: numpy arrays and SimpleITK images load directly; new script commands `viewports`, `showall`, `fuseall`,
  `image3d`, `measurements`; colormap names in scripts ignore case, spaces and dashes; example `00_load_images.py`.
* Brush up to 128 mm (B or Alt + wheel); ruler ends can be dragged; Z selects the zoom tool.
* Recording: virtual cameras (NVIDIA Broadcast, OBS, Logi Capture …) can be chosen as the camera.
* Licence 1.1: personal licence file and trial (1a), orcami.py and the examples under MIT (2a), data and privacy (5a).
* Fix: removing a fusion with the view's ✖ (or using the view's own buttons and sliders) no longer moves the crosshair.
* Tools → DICOM curation & conversion → Curate tab: organize PACS exports (e.g. syngo.via) into folders from DICOM header tags (patient, study, date, series …), DICOM copied / moved / left, NIfTI + Excel optional, preview, undo, parallel. The batch converter window is now *DICOM curation & conversion* (one Tools entry, opens on the tab used last; the NIfTI options are a foldable section on the Convert and Curate tabs instead of an Options tab).
* Segmentation opacity per view (the ▦ Seg slider of each view, ↺ back to the segmentation's own; saved with workspaces).
* Licence: a free personal licence file per computer, 7-day trial without one.
* Video tutorials on YouTube: [youtube.com/@ORCA-MI](https://www.youtube.com/@ORCA-MI) (Help → ▶ Video tutorials, About, welcome page).

* Viewer for DICOM (CT, MR, PET, SPECT, X-ray, US, RTSTRUCT, RTDOSE, SEG), NIfTI, NRRD, MHA/MHD and more;
  layouts up to 3×3, MPR, PET/CT and SPECT/CT fusion, GPU 3D, 4D cine, hanging protocols, patient database.
* Segmentation by hand, threshold and region growing, nnInteractive, nnU-Net, iterative PET lesion segmentation,
  body contour; SUV, MTV, SUVpeak and TLG per segment.
* Dynamic and multi-time-point PET/SPECT (time-activity curves, Patlak, effective half-life), CT dose,
  cardiac 17-segment model, dosimetry (DVH, SIRT Y-90), registration, image comparison, lesion tracking
  (RECIST 1.1, PERCIST 1.0) and report folders.
* Export to DICOM for the PACS (images, SEG, RTSTRUCT, SR), figures and GIFs, CSV and Excel.
* Autosave and crash recovery, reader studies, scripting and Python API (`orcami.py`).
* One-click AI environment installer, model library, nnU-Net training and nnInteractive fine-tuning.
* Models download fold by fold (choose which folds, add or remove folds later); fold check boxes for nnU-Net and
  image-to-image inference; GPU memory released after every inference.
* Trained and fine-tuned models, their data and evaluation stay on the user's computer.
* Help → 🌐 ORCA-MI on GitHub.
* Image → ☢ Q.SPECT: quantitative SPECT with a library of conversion factors per scanner, isotope and
  reconstruction (kept across updates, JSON export / import); also in the Image tab → PET / SPECT.
* Image → ⏳ Decay correction: activity calculator between two times (Bq … Ci, 36 radionuclides) and decay
  correction of a whole PET / SPECT image to a target time; dates as yyyy.mm.dd hh:mm:ss or with a calendar.
* Image → 🔢 Values: convert the data type (float32 / float64 / int32 / int16 / uint16 / uint8), clip, normalize
  (0 … 1 or any range, from min/max, min/p99, p1/p99 or entered values) and exact histogram percentiles; the
  histogram in the Image tab marks the 99th percentile.
* View → 🖥 Graphics: GPU (power-saving on laptops by default), graphics API, VSync — for windows that blink.
* Segment tab: deleting a label works (it was re-created when it was the active label).
* Saving: a CT is written as int16 only when every value is a whole number in range (before, only a sample was checked).
* New look: Segoe UI type scale, Fluent icons, a toolbar in named groups, a progress line and job chips, notifications
  with icons; the tool panel has a rail of coloured icons with the tabs' full names (Compare images, Lesion tracking …)
  and is wider; viewport text never overlaps; empty pages say what to do; a new welcome page.
* View → 🎨 Appearance and styles: five styles (ORCA Standard, Clinical reading room, Research compact, Presentation,
  Soft teal), density, corners, surfaces, accent colour, reading room, tool panel icon size (also View → ▥ Tool panel icons).
* The NEMA IEC and DICOM converter windows follow ORCA-MI's colours.
* Your country: a separate, optional question at the first start, sent once (Windows' region setting only).
* Layouts: two MPRs side by side (two images, each axial / sagittal / coronal / 3D), 4 × 4 and 5 × 5.
* Segment tab: Morphology & cleanup choose their segmentation and label (or every label); region growing key Shift+R.
* Register tab: 📉 loss curve of the last registration; ☑ Select all to combine registrations.
* File → 💾 Save images, segmentations, registrations (several at once, into one folder); 🛒 export basket from the
  image's right-click menu; File → Save workspace with copies of every image (opens without the original files).
* AI models: folders below the task (scanner, dose …) are their own levels; model folder names shown in parts
  (swin · light · 2.0mm · 96 · 15703K · 3D); a model already downloaded, also under an earlier name, is not downloaded again.
* Dose tab: ✖ Remove colour wash; the dose as an image in Gy (new image or overwrite).
* Tools → 🎯 NEMA IEC phantom analysis: the NEMA IEC body phantom tool built in (contrast recovery, background
  variability, SPECT calibration, PDF / Excel reports), with images from ORCA-MI, ROIs to and from ORCA-MI
  segmentations and the calibration saved as a Q.SPECT conversion factor; several ORCA-MI images sent at once with
  their roles, colormaps and windows; Smooth display toggle (key I).
* Tools → 🗂 Batch DICOM → NIfTI conversion: the Yazdan DICOM converter built in (folder trees, Excel header tables,
  PET SUV, gantry tilt and uneven spacing correction, renaming, dcm2niix).

Downloads: [installer](download/ORCA-MI-0.1.0-setup.exe) ·
[portable zip](download/ORCA-MI-0.1.0-portable.zip)
