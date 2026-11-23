# Changelog

## 0.1.9 — 2026-11-23

* **Batch → ☢ CT dose + scan range**: for each CT, the upper and lower anatomical boundary of the scan (from the organ and vertebrae maps, made first when missing), then CTDIvol, DLP, SSDE and an effective dose estimate for the whole scan and per body region (head, neck, chest, abdomen, pelvis, legs). One CSV row per CT.
* The vertebrae model of TotalSegmentator can be downloaded from the Batch tab after accepting its licence (Apache-2.0).
* **Lesion tracking**: two methods, *Conventional* (registration) and *Organ-guided* (anatomy: vertebrae and organs, no registration). Missing anatomy maps are segmented for you (CT; PET without CT: choose the tracer).
* **Right-click on an image → Create body contour**: min / max suggested from the modality and the histogram, and *Remove the CT table* (ticked by default) keeps the table out of the contour.
* **AI tab**: *Find a model* by kind (organs, lesions …) in a guide window, a basket of the chosen models, short model information on hover and right-click; adding your own models is in its own folded section.
* **Simple mode** shows fewer sections at once: Image (window / level, fusion), Segment (segmentations, labels, manual tools); configuration, patient & study and lesion spill-out are folded.
* Register tab: separate sections to align image centres, align on segmentations and align by picked points.
* Dosimetry: *Convert image to dose*. CT dose tab: sections for exposure, size options, regional CTDIvol, curves and density map. Compare tab: own sections for the gamma map and the NPS.
* **DICOM curation**: drag the folder-name tags left and right, a *Tracer* tag for PET / NM, and *Stop* stops at once.
* **Segment / score a database**: PDF or text documents of a case (physician report, disease description) shown to readers under *Additional information*, readable in a large window; on or off per reader.

## 0.1.8 — 2026-11-22

* **Right-click a colour bar** on any view for the window presets of that image's modality (CT, PET / SPECT), and its colours.
* CT: new **Abdomen** window (C 50 / W 400, key 9).
* **Visible frames** around every text box, number box, drop-down, tick box and radio button, in every theme and surface style (e.g. the licence request form).
* Tool panel tables (e.g. Dosimetry → SIRT): the names on the left are shown in full instead of a few letters, and drop-downs use the width of the panel.
* Tool panel: a row that continues on the next line no longer overlaps the row below (e.g. the nuclide in single time point dosimetry), and a wide row no longer pushes the following sections past the panel's edge.
* Segment tab: the segmentation name box grows with the panel.
* 3D view: untick **Use image window** (3D view tab → Transfer function) for a window of its own: right-drag, colour bar, presets and keys on the 3D view then leave the slices and fusions as they are.
* **Drag an image onto a 3D view**: it is shown in that view only, without asking for its role. In *Two MPRs side by side* the three slice views of that MPR keep theirs (e.g. CT with fused PET, and the PET in 3D).

## 0.1.7 — 2026-11-21

* Auto-hidden panels: a new **mini** button next to the pin and push / over. While hidden, the tool panel leaves a narrow strip with every tab's icon and name, the image list a narrow strip with one small card per study (date, modalities, name). Click a tab or a study to open the panel there; keep the mouse on the strip to open it.
* Segment a database: **👍 Good as it is — approve & next** when the studies start from a segmentation (another reader's, a file's or an nnU-Net model's): it is saved unchanged, marked approved (column *approved* in the summary CSV), and the next study opens.
* Tools → 🏥 **New segmentation database from the patient database**: choose the images by modality (e.g. PET + CT), tick the studies, pick the series where a study has several, and ORCA-MI writes the database (NIfTI, PET in SUV, case folders without names); then the usual set-up opens for labels, questions and readers.
* Segment a database: each reader can **start from** a different point (scratch, another reader, nnU-Net), in the set-up's readers table and in the Everyone shortcut's "who is segmenting?" window.
* Segment a database: readers who start **from scratch** are not asked the score questions (nothing to judge yet).
* Segment a database: **summary of all readers** (`_segmentations/summary_all_readers.csv`, updated at every save); **Tools → 📊 Segment a database results** shows every reader's time spent, time of day, normal / approved cases and scores (means and the distribution of each score) as tables and charts in the Results tab, which can be saved as JPEG / PNG, Excel and CSV, and each reader is asked once whether the **time of day** and the **time spent** may be recorded (two separate choices; otherwise only the date / no duration).
* AI group of the toolbar: choose the image nnInteractive segments (*the image I click on* or a loaded image) and **✔ Next** (next object), without opening the Segment tab. The *⚡ Speed up* options (AI tab, nnInteractive) are now a foldable section.
* 3D view: with *Use image colormap* off (3D view tab), the colour bar of the 3D view and its right-click *Colormap* change only the 3D view's colours; the 2D views keep theirs.
* Narrow tool panel (laptops): rows with drop-down menus (e.g. the segmentation and label pickers of the spill-out correction) continue on the next line instead of being cut off.
* Segment tab: **Threshold → label** and **Double threshold** can be limited to a **3D box** (📦 only inside a 3D box; drag its edges on the views, as in Crop).
* nnInteractive *Segment on* (Segment tab and AI toolbar group): lists only the images shown on the views, grouped by study and then series.
* The segmentation opacity slider is on every view that shows a segmentation (also another image's); right-click it for **outline / filled in this view**.
* Image list: a long segmentation name continues on the next line instead of widening the panel (the panel can be made narrow again).
* nnInteractive: **✖ Cancel** on its progress banner stops a long step (or the loading) at once and frees the CPU / GPU.

## 0.1.6 — 2026-11-20

* Segment a database and Score a database: a **"Set it up yourself"** shortcut next to the readers' and the everyone shortcuts. It opens the set-up window with the database folder already chosen (as Tools → Segment / Score a database), where anyone sets their own name and options. Always written in the database folder; a tick puts it on the Desktop too.

## 0.1.5 — 2026-11-20

* Double-clicking a DICOM file (Open with ORCA-MI) opens its whole folder in the DICOM browser, as if the folder were dropped: choose the series to load.
* Info tab: geometry, patient and header values use the whole width of the panel (they were cut short, even in a wide panel); the nickname box is as wide as the panel.
* The colourful appearance is on for new installations (Settings → Appearance).

## 0.1.4 — 2026-11-19

* Segment a database and Score a database: choose the **3D colormap** of the readers' 3D view (same as the image, or any colormap), next to the choice of the image shown in 3D (PET / SPECT or CT / MR). Script option `cmap3d=` and command `cmap3d`.
* Windows only: the Linux (Ubuntu) test version stays at 0.1.3 (download it from the v0.1.3 release).

## 0.1.3 — 2026-11-19

* 🙂 Simple and 🛠 Expert mode (switch at the right of the menus): in Simple mode every tab shows its basic options and the others are *More options* chips (click to show a section, click again to hide it). New installations start in Simple mode; updates keep Expert mode (every option at once, as before).
* 🕶 Anonymize DICOM → ↩ Re-identify: undo the anonymization with the decode file, into a new folder, also for what was made from the anonymized images (DICOM SEG / RTSTRUCT, NIfTI segmentations, annotations, result tables): names, IDs, birth dates, emptied fields and original UIDs come back (so later segmentations point to the original images), with the original folders or a patient / study / series structure. The decode file now also keeps the original paths, the emptied values and every UID (needed for a complete re-identification).
* 📁 Folder view (Tools, or 📁 Show in ORCA-MI next to the output of the anonymizer, re-identify and DICOM curation): a folder as a live tree inside ORCA-MI, so session recordings can show what a tool writes; names can be hidden for the video.
* 🐧 Linux (Ubuntu) test version: `ORCA-MI-0.1.3-ubuntu.tar.gz` in this release (same program; no session recording, system monitor or automatic updates).

## 0.1.2 — 2026-11-18

* Several files dropped at once: 🖼 All as images / 🎨 All as segmentations in one click.
* New segmentations get colours different from the other segmentations of the same study (on by default; files with their own colour table keep theirs).
* 🏷 Segment name guide: right-click a view (2D or 3D) → Show segment name guide: a line in each segment's colour to its name at the edge of the view.
* Fix: AI set-up with new NVIDIA drivers (2026, e.g. 610): the GPU's CUDA version is found again, so the CUDA build of PyTorch is installed instead of the CPU one; choosing a CUDA build after a CPU one now really replaces it.
* Fix: links in ORCA-MI (start page, About, NEMA window) open in the browser; Help → 🌐 ORCA-MI website (orca-mi.github.io) and 🐙 ORCA-MI on GitHub.

## 0.1.1 — 2026-11-18

* Updates: ORCA-MI looks for a newer version when it opens (with your consent to notifications) and installs it for you (downloaded installer checked with the author's signature); Help → ⬆ Check for ORCA-MI updates. Downloads are now on the GitHub releases page and on orca-mi.github.io.
* Tools → DICOM curation & conversion → Curate tab: organize PACS exports (e.g. syngo.via) into folders from DICOM header tags (patient, study, date, series …), DICOM copied / moved / left, NIfTI + Excel optional, preview, undo, parallel. The batch converter window is now *DICOM curation & conversion* (one Tools entry, opens on the tab used last; the NIfTI options are a foldable section on the Convert and Curate tabs instead of an Options tab).
* Tools → 📈 Scanner calibration & QC: PET and SPECT calibration phantoms (moved from the NEMA IEC window, which keeps a link) and a history per scanner (found from the DICOM header): calibration and NEMA IEC results (📈 Save to scanner history) compared with the previous and a reference record, your own ± % tolerances, EARL1 / EARL2 bands for ¹⁸F-FDG PET (hide each with one click), charts per sphere and over time, JSON export / import, Excel report.
* Recording: virtual cameras (NVIDIA Broadcast, OBS, Logi Capture …) can be chosen as the camera.
* Licence 1.1: personal licence file and trial (1a), orcami.py and the examples under MIT (2a), data and privacy (5a).
* Fix: removing a fusion with the view's ✖ (or using the view's own buttons and sliders) no longer moves the crosshair.
* Fix: on a PC with two monitors that use different Windows scaling, the interface no longer keeps switching between big and small on first start (the automatic size waits until it is stable and is kept after a few changes).

## 0.1.0 — 2026-11-16

First public version.

* Session recording for training videos (MP4 with microphone, camera picture-in-picture, pointer, pressed keys,
  watermark, four qualities up to 3840 px / 30 fps); 🎞 picture viewer for GIFs (play, pause, speed, zoom).
* French interface; menus by category; colormap on right-click of any image; NEMA IEC window size.
* Python: numpy arrays and SimpleITK images load directly; new script commands `viewports`, `showall`, `fuseall`,
  `image3d`, `measurements`; colormap names in scripts ignore case, spaces and dashes; example `00_load_images.py`.
* Brush up to 128 mm (B or Alt + wheel); ruler ends can be dragged; Z selects the zoom tool.
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
