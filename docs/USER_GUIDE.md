# 🐋 ORCA-MI user guide — version 0.1

**Open Radiology & Computational Analysis — Molecular Imaging** · Author: **Yazdan Salimi** (salimiyazdan@gmail.com) · Built with the help of Jean-Claude (Claude by Anthropic).

🐋 *Agile intelligence, deep insight.* **Why ORCA?** Like the orca, ORCA-MI is fast, intelligent and sees deep beneath
the surface of your images.

> For research use only. Not a certified medical device. ORCA-MI is an independent research project, not affiliated with any company or product named ORCA.

🌐 **Website, new versions and documentation: [github.com/orca-mi/orca-mi](https://github.com/orca-mi/orca-mi)** (also Help → 🌐 ORCA-MI on GitHub).

▶ **Video tutorials: [youtube.com/@ORCA-MI](https://www.youtube.com/@ORCA-MI)** — short videos, one feature each (also Help → ▶ Video tutorials).

In the program: **Help → 📖 User guide** opens this guide; **Help → 🐞 Report a bug / 💡 Request a feature** sends a message to the author.

## Contents

* [1. Getting started](#1-getting-started)
    * [Getting ORCA-MI: portable or installer](#getting-orca-mi-portable-or-installer)
    * [First start](#first-start)
    * [Mouse & keys](#mouse--keys)
    * [Memory used](#memory-used)
    * [📈 System monitor (CPU, RAM, GPU)](#-system-monitor-cpu-ram-gpu)
    * [Recent files](#recent-files)
    * [Interface size](#interface-size)
    * [🖥 Graphics (if the window blinks)](#-graphics-if-the-window-blinks)
    * [Busy tabs](#busy-tabs)
    * [Contrast levels](#contrast-levels)
    * [Coloured section titles](#coloured-section-titles)
    * [🌐 Language: English / Français](#-language-english--français)
    * [3D view toolbar background](#3d-view-toolbar-background)
    * [🎨 Appearance and styles](#-appearance-and-styles)
    * [Text on the views: sizes for papers and talks](#text-on-the-views-sizes-for-papers-and-talks)
    * [◐ Window / level menu](#-window--level-menu)
    * [The tool panel and its icon rail](#the-tool-panel-and-its-icon-rail)
* [2. Loading and viewing images](#2-loading-and-viewing-images)
    * [What ORCA-MI reads, shows and computes](#what-orca-mi-reads-shows-and-computes)
    * [Drag & drop roles](#drag--drop-roles)
    * [Overlay sync & roles](#overlay-sync--roles)
    * [🖼 Hanging protocols](#-hanging-protocols)
    * [3D view](#3d-view)
    * [3D view: image and segments on / off](#3d-view-image-and-segments-on--off)
    * [Colormap gamma and colorbar](#colormap-gamma-and-colorbar)
    * [📈 Line profiles](#-line-profiles)
    * [📍 Values of all images at the crosshair](#-values-of-all-images-at-the-crosshair)
    * [🌫 Filters and denoising](#-filters-and-denoising)
    * [▦ Resampling to a spacing](#-resampling-to-a-spacing)
    * [⇄ Match space and ◩ masking to segmentations](#-match-space-and--masking-to-segmentations)
    * [✖ Scaling the values](#-scaling-the-values)
    * [☢ Q.SPECT: quantitative SPECT with conversion factors](#-qspect-quantitative-spect-with-conversion-factors)
    * [⏳ Decay correction](#-decay-correction)
    * [🔢 Data type, clipping, normalisation and percentiles](#-data-type-clipping-normalisation-and-percentiles)
    * [🎯 NEMA IEC phantom analysis](#-nema-iec-phantom-analysis)
    * [🧠 Brain PET resolution (EIR, EARL)](#-brain-pet-resolution-eir-earl)
    * [Loading: role, nickname and comment](#loading-role-nickname-and-comment)
    * [📅 Studies in the image list](#-studies-in-the-image-list)
* [3. Segmentation and measurements](#3-segmentation-and-measurements)
    * [▦ Segmentations on every image (as in 3D Slicer)](#-segmentations-on-every-image-as-in-3d-slicer)
    * [🎯 nnInteractive: progress and inference region](#-nninteractive-progress-and-inference-region)
    * [Live threshold](#live-threshold)
    * [Double threshold (two images, AND / OR)](#double-threshold-two-images-and--or)
    * [🧍 Body contour](#-body-contour)
    * [Measurements: volume, SUVmean, SUVmax, SUVpeak, TLG](#measurements-volume-suvmean-suvmax-suvpeak-tlg)
    * [📈 Iterative segmentation (XEOS method)](#-iterative-segmentation-xeos-method)
    * [✂ Crop](#-crop)
* [4. Dynamic PET and multi-time-point imaging](#4-dynamic-pet-and-multi-time-point-imaging)
    * [Time-activity curves, Patlak, half-life](#time-activity-curves-patlak-half-life)
    * [Named registrations: apply them to other images](#named-registrations-apply-them-to-other-images)
    * [Interactive registration: live preview, mouse, segments, landmarks](#interactive-registration-live-preview-mouse-segments-landmarks)
    * [Registration constraints: masks and a focus sphere](#registration-constraints-masks-and-a-focus-sphere)
* [5. Dosimetry](#5-dosimetry)
    * [Dosimetry (☢ Dose tab)](#dosimetry--dose-tab)
    * [DVH metrics](#dvh-metrics)
    * [⚛ Dose point kernel (coming soon)](#-dose-point-kernel-coming-soon)
    * [🧪 SIRT Y-90 dose: local deposition method (LDM)](#-sirt-y-90-dose-local-deposition-method-ldm)
* [5b. CT dose, patient size and density](#5b-ct-dose-patient-size-and-density)
    * [Density map](#density-map)
    * [📦 Batch tab: inputs by pattern, output names and folders](#-batch-tab-inputs-by-pattern-output-names-and-folders)
    * [💪 Arms position (batch)](#-arms-position-batch)
* [5c. Cardiac: short axis, 17 segments, bull's-eye](#5c-cardiac-short-axis-17-segments-bulls-eye)
* [5d. Image comparison: errors, gamma index, noise power spectrum](#5d-image-comparison-errors-gamma-index-noise-power-spectrum)
* [5e. Lesion tracking: RECIST, PERCIST, TMTV](#5e-lesion-tracking-recist-percist-tmtv)
* [5e2. Prognosis (coming soon)](#5e2-prognosis-coming-soon)
* [5f. Report folders: lesion tracking, segment statistics, image comparison, segmentation comparison](#5f-report-folders-lesion-tracking-segment-statistics-image-comparison-segmentation-comparison)
* [6. AI: segmentation, enhancement, training](#6-ai-segmentation-enhancement-training)
    * [Installing on a new PC (no Python)](#installing-on-a-new-pc-no-python)
    * [Inputs of multi-channel models: which image is which](#inputs-of-multi-channel-models-which-image-is-which)
    * [AI inference details](#ai-inference-details)
    * [Distributing models (download links)](#distributing-models-download-links)
    * [🧠 Downloadable models (Google Drive links)](#-downloadable-models-google-drive-links)
    * [Model library file (your future models)](#model-library-file-your-future-models)
    * [🏋 Train tab: your own nnU-Net and fine-tuned nnInteractive](#-train-tab-your-own-nnu-net-and-fine-tuned-nninteractive)
    * [AI troubleshooting on another PC](#ai-troubleshooting-on-another-pc)
    * [If the window blinks or stutters while AI runs](#if-the-window-blinks-or-stutters-while-ai-runs)
    * [AI models: folders, several models at once, progress](#ai-models-folders-several-models-at-once-progress)
    * [⚡ Faster inference: crop to the body and to a z-range](#-faster-inference-crop-to-the-body-and-to-a-z-range)
    * [🗂 Model folder (e.g. Google Drive)](#-model-folder-eg-google-drive)
    * [📣 News and new models from the author](#-news-and-new-models-from-the-author)
* [7. Export](#7-export)
    * [🏥 Export to DICOM / PACS (images, SEG, RTSTRUCT, SR)](#-export-to-dicom--pacs-images-seg-rtstruct-sr)
    * [📸 Export images & GIFs](#-export-images--gifs)
    * [🎞 Picture viewer (GIF, PNG, JPEG)](#-picture-viewer-gif-png-jpeg)
    * [🗂 DICOM curation & conversion (batch DICOM → NIfTI)](#-dicom-curation--conversion-batch-dicom--nifti)
    * [🗃 Curate a DICOM database](#-curate-a-dicom-database)
    * [⏺ Record a session (training video)](#-record-a-session-training-video)
    * [🕶 Anonymize DICOM](#-anonymize-dicom)
* [8. Sessions, workspaces and reader studies](#8-sessions-workspaces-and-reader-studies)
    * [♻ Autosave, crash recovery and workspaces](#-autosave-crash-recovery-and-workspaces)
    * [Reading sessions (physician scoring)](#reading-sessions-physician-scoring)
    * [Scoring a database (patients × configurations)](#scoring-a-database-patients--configurations)
    * [🗂 Segmenting a database (studies × observers)](#-segmenting-a-database-studies--observers)
    * [📊 Results tab](#-results-tab)
* [9. Automation: scripts and Python](#9-automation-scripts-and-python)
    * [Automation / batch scripts](#automation--batch-scripts)
    * [Python API](#python-api)
    * [Examples (folder `examples`)](#examples-folder-examples)
* [10. Feedback and privacy](#10-feedback-and-privacy)
    * [💬 Feedback, bug reports and feature requests](#-feedback-bug-reports-and-feature-requests)
* [11. Roadmap](#11-roadmap)
    * [Radiomics (planned)](#radiomics-planned)

## 1. Getting started

### 🔑 Licence and trial

ORCA-MI is free for research with a **personal licence file** from the author, for **one person on one computer**:
the request form shows this computer's **PC code** (made from Windows' installation number; it tells nothing else about
the computer) and asks for your own name for the computer (e.g. *office PC, left table*); both are sent with the request
and written into the licence, which then works on that computer only. A new or reinstalled computer needs a new
licence (the request form is filled in for you). Without one it runs as a **7-day
trial** on each computer: the Image, Segment (nnInteractive included) and Info tabs, viewing, the image tools, NEMA
IEC and every save / export work; the other tabs can be looked at (view only). After 7 days only the licence screen is
left. **Help → 🔑 Licence…**: *Request your free licence* (a short form sent to the author, like feedback; the
author's e-mail is shown with a copy button) and *Load licence file…* (or drop the `.lic` file onto the window). Once
the request is sent, the form says so and what comes next: the ORCA-MI team sends you a licence file (`.lic`) by
e-mail; save it somewhere on your computer and load it with *🔑 Load licence file…* (a button right there, and in
Help → Licence); *✖ Close* closes the window. The licence is personal and must not be shared; Help → About shows whom it is
issued to. The top bar shows `🔑 Licensed · until <date>` (name and institution on hover); in the last 14 days it
turns orange (`Licence ends in N days`). **Renewal:** click that label, or use the licence screen once the licence has
ended: it asks for an **extension of the same licence**. Your details (name, institution, e-mail, licence ID, this
computer) are shown from your licence; you only write a short **reason for the extension** (required) and press
*🔄 Request extension* (*✏ Change my details* opens the full form if something changed); then load the new licence
file. Script / Python: `licence` (status),
`licence load <file.lic>`. The request form has an optional **Country** (where you work): it is used for the author's map of users instead of Windows' region setting, which is often a default (e.g. United States) on hospital computers.

### Getting ORCA-MI: portable or installer

| | `ORCA-MI.exe` (portable) | `ORCA-MI-0.1.0-setup.exe` (installer) |
|---|---|---|
| Administrator rights | not needed | not needed (installs for the current user) |
| Where it runs | anywhere: Desktop, USB stick, shared folder | `%LOCALAPPDATA%\Programs\ORCA-MI` |
| Start menu / desktop shortcut | – | ✔ (desktop optional) |
| "Open with ORCA-MI" for .nii .nrrd .mha .mhd .dcm | – | optional; your default programs are not changed |
| Uninstall | delete the file | Windows *Apps* list or the Start-menu uninstaller |

Both contain the same program. Settings, models and AI environments are stored in your user profile, so
switching between the two, or updating, keeps everything. Windows may show a SmartScreen "unknown publisher"
note the first time; choose *More info → Run anyway* (a code-signing certificate would remove it).

### First start

Copy `ORCA-MI.exe` anywhere and run it. No installation is needed. Settings live in
`%APPDATA%\ORCA-MI\settings.json`.

**Data folders:** `%APPDATA%\ORCA-MI` (settings, logs, hanging protocols, autosave, training list) and
`%LOCALAPPDATA%\ORCA-MI` (downloaded models, nnU-Net workspace, AI Python).

#### Optional Python AI back-ends

The viewer itself needs no Python. AI features call a Python environment of your choice through a bridge
script that is embedded in the exe (written to `%APPDATA%\ORCA-MI\orcami_bridge.py`).

* **nnInteractive** (default env: `orca-mi`):
  ```
  conda create -n orca-mi --clone totalseg        # or any env with torch + CUDA
  conda run -n orca-mi pip install nninteractive huggingface_hub
  ```
  The model (`nnInteractive_v1.0`) is downloaded automatically on first start.
* **nnU-Net v2:** any env with `nnunetv2`; point the preset to the trained model folder
  (`…/DatasetXXX/nnUNetTrainer__nnUNetPlans__3d_fullres`).
* **Your MONAI models:** the default preset uses the `image` env and the `yazdan` runner
  (`yazdan.DL.model_inference_regression_multi_workers`). Select a `…-Full.pth` model. The bridge adds
  compatibility shims for checkpoints pickled with older MONAI versions (SwinUNETR `patch_size`, reader
  `to_gpu`). Predictions are mapped back from the network range (`output_b_min/max`) to intensities (`output_lower/upper_intensity`, read from `params_to_torch_save-record.json` or the checkpoint): "Undo output normalization" = auto / on / off.

Check an environment from the AI tab with **Environment check**.

### Mouse & keys

| Action | Input |
|---|---|
| Scroll slices | wheel, ↑/↓, PgUp/PgDn |
| Zoom | Ctrl + wheel, or Zoom tool (Z) |
| Distance | Ruler tool (M): drag to draw; drag an end of a drawn distance to change it (the end under the mouse gets a white ring) |
| Window / level | right-drag (always), or W/L tool |
| Pan | middle-drag, or Pan tool |
| 4D frames | Shift + wheel, ←/→, Space = cine |
| Maximize viewport | double-click |
| Fusion overlay | Shift + drag a thumbnail onto a viewport |
| nnInteractive | left = include, Ctrl + left = exclude, Enter = next object |
| Brush size | `[` `]`, or hold B (or Alt) + wheel, up to 128 mm (Shift + paint erases) |
| Undo / redo | Ctrl+Z / Ctrl+Y |
| Presets | 1…9, 0 = smart window |

**Same scale in every view** (View menu, on by default): 2D views of the same orientation show one millimetre with
the same number of pixels, so a CT (small voxels, small field of view) and a PET (large voxels, large field of view)
side by side show the anatomy at the same size. The view with the largest field of view still fits; zoom each view
as usual (or *Sync zoom & pan*). Script: `samescale 0|1`.

### The menus

The drop-down menus are sorted into categories:

* **View**: *Interface* (language, appearance, theme, contrast, interface size, graphics), *Layout* (layouts,
  hanging protocols, orientation of the active view), *Image display* (interpolation, crosshair, corner text,
  colorbar, segment names) and *Linking views* (link viewports, sync zoom, same scale, sync fusion), then full screen.
* **Image** (the active image): *Display* (smart window / level, 🎨 colormap), *Units and quantification* (SUV,
  Q.SPECT, decay), *Geometry* (match space, resample), *Filter and mask*, *Values and maths*, *Information and copies*.
* **Segmentation**: *Files* (new, load, export), *Visibility* (🙈 hide all / 👁 show all segmentations), *Analysis*
  (statistics, compare) and *AI segmentation* (nnInteractive, AI models, segment a database).
* **Tools**, with the same titled sections: *Analysis* (dynamic PET, NEMA IEC, brain PET resolution), *AI and
  nnU-Net* (nnInteractive, AI models, training, prepare nnU-Net training, model library, AI environment),
  *Reading studies and databases* (image quality scoring, score / segment a database, reading sessions, results) and
  *Data, privacy and recording* (curate a DICOM database, batch DICOM → NIfTI, anonymize DICOM, record a session); then Log and Settings.
  Registration is the 🔗 tab of the tool panel.

**🎨 Colormap on the right-click menu**: right-click any image (a 2D view, the 3D view or its thumbnail in the image
list) → *🎨 Colormap* to change its colours; on a fused view, *🎨 Colormap of the fused overlay* changes the overlay's.

### Memory used

The menu bar shows the memory used by ORCA-MI (🧠, e.g. *2.3 GB*); hover for the peak, the committed memory and the
memory free on the computer. It turns orange below 20 % and red below 10 % free RAM.

### 📈 System monitor (CPU, RAM, GPU)

Next to the licence in the top bar, a strip shows the load of the **whole computer** (not only ORCA-MI), read once
a second: the processor and its load (`i9-13900KF 12 %`), the RAM used / total (`RAM 21.3/63.7 GB`), the graphics card
and its engine load (`RTX 4090 7 %`) and its memory used / total (`VRAM 3.1/24.0 GB`), or *no GPU*. Values turn orange
above 75 % and red above 90 %; hover for the full names, the free memory and ORCA-MI's own share of the RAM.

**📈** (or Settings → *📈 System monitor…*) opens the **System monitor** window: four cards, each with the value in
large type, a load bar (green, amber above 60 %, red above 85 %) and a graph of the last 1, 2, 5 or 10 minutes:

* **CPU**: processor name and logical cores, and one small bar per logical core (hover for its load).
* **RAM**: used / total of the computer, page file, free memory, ORCA-MI's own part (violet line) and the committed memory.
* **GPU usage**: graphics card, with its **temperature**, power (used / limit) and fan speed; the temperature is the
  red line in the graph (°C on the same scale).
* **GPU memory**: used / total and free.

NVIDIA cards are read through the NVIDIA driver (the same values as `nvidia-smi`), other cards through Windows' GPU
counters (as Task Manager; temperature and power are then not available). The **CPU temperature** is not shown: Windows
gives it only to programs running with administrator rights (the sensor it gives to others is a motherboard zone, not the
processor).

**Settings → Appearance:** *Show CPU, RAM and GPU of this computer in the top bar* (on by default, as *Icon only*) and how it looks:
*All information* (values, with or without the processor and graphics card names), *Names only* (the processor, RAM and
graphics card as small pills whose colour and bar show the load; values on hover) or *Icon only* (just 📈: click it to open the
System monitor; the readings show on hover). The same choice is in the System monitor window. Nothing is read while
neither the strip nor the window is shown. Script / Python: `sysmon` (prints `[sysmon] cpu=…|cpu_name=…|ram_used_gb=…|
gpu=…|gpu_name=…|vram_used_gb=…|vram_total_gb=…|gpu_temp=…|gpu_power=…`), `sysmon window`, `sysmon bar=0|1`,
`sysmon mode=all|names|icon`.

### Recent files

File → 🕘 Recent lists the last 12; **📜 All recent files…** opens a window with every one (up to 300) with its
folder and when it was opened, a filter, *clear missing* and ✖ to forget one (hidden during blinded reading).

### Fold all sections

Every tab of the tool panel has **⊟ Fold all** next to its title: it closes all the tab's sections at once, so the
sections lower down are easy to reach; open the one you need again.

### Interface size

*Settings → Appearance* (the 🎨 button in the toolbar's Interface group, also View → *Interface size*) offers three ways to set it:
* **Automatic** (the default on a new PC): smaller on laptops with high Windows scaling, standard on desktops.
* **Fixed steps** from 70 % to 250 %.
* **Custom value**, applied with a button. There's no slider, so nothing moves under the mouse while the interface resizes.

`Ctrl +`, `Ctrl −` and `Ctrl 0` also work.

### 🖥 Graphics (if the window blinks)

*View → 🖥 Graphics…* shows the GPU in use (also in Help → About and the log) and chooses, for the next start:

* **GPU:** *Automatic* (default: the power-saving, built-in GPU on a PC with a battery, the high-performance GPU
  otherwise), *power-saving / built-in* or *high-performance / discrete*. On laptops with two GPUs the screen is driven
  by the built-in one; drawing on the discrete GPU copies every frame across, a common cause of a blinking window.
* **Graphics API:** Automatic, DirectX 12, Vulkan or OpenGL.
* **VSync** and **frames queued** (1 = lowest latency, 2 = smoother).

If the window blinks, try the power-saving GPU first, then another API. The settings are kept in `graphics.json`
next to your settings; images, results and every other setting are not affected.

### Busy tabs

While a tab has work running (a training, an AI model, a registration, a filter, resampling …) a dot pulses on its
icon in the tool panel's rail; hovering over it says what is running. A thin line under the toolbar and a chip in the
status bar (progress, %, ✖ cancel) show the work too.

### Contrast levels

View → **◑ Contrast** (also in 🎨 Appearance, or **Ctrl+Shift+H** to cycle): *Standard*, *High*,
*Higher*, *Maximum*. The level is applied on top of every theme: darker / lighter panels, pure white / black text,
brighter dim text and thicker, clearer button borders. Script / Python: `contrast 0..3`.

### Coloured section titles

Section titles in the tool panels (Segmentations, Manual tools, Threshold → label …) are coloured. Each title always has the same colour, so sections are quick to find, and there are darker shades on light themes. Switch it off in View or Settings.

### 🌐 Language: English / Français

**Settings → Appearance → Language** (also the 🌐 box at the top of the View menu) switches the menus, buttons,
labels, tabs, tooltips and window titles to **French**, at once, without a restart. Only what is shown changes:
everything ORCA-MI saves, compares or sends stays in English — settings, image, segmentation and label names (e.g.
*Liver*, *FDG organs (ULDCT values)*), file names, logs, the Python / script commands and their replies (`[tag] …`),
reports, exports and the user guide. So scripts, sessions and results are the same in both languages. A text without
a translation (long help texts, units, DICOM tag names, product, theme and colormap names) is shown in English.
The translations are in `assets/i18n/fr.tsv` (`English<TAB>French`); corrections are welcome (Help → Feedback).
Script: `language en|fr`, `trfr <text>` (prints `[trfr]` with the French text).

### 3D view toolbar background

The 3D view's buttons (Reset, A, P, L, R, S, I, Rotate…) have their own background. With **Settings → Appearance →
Opaque background behind the 3D view's checkboxes** (on by default; also in 🎨 Appearance and styles → *3D view
toolbar*), the checkboxes (🔗, Auto-rotate, Crosshair, Marks, Image, Segments, Image in segments) get one too, so
they stay readable over the image when the 3D view is zoomed. Script: `opaque3d on|off`.

### Colourful appearance

**Settings → Appearance → Colourful appearance** (off by default; also in 🎨 Appearance and styles → *Colours*) gives
choices that mean different things their own colours, the same everywhere: **green** = fast / light, **blue** =
balanced, **violet** = best quality (slowest), **amber** = fastest but not accurate. It is used for the 3D quality
presets (Low / Balanced / High), the nnU-Net speeds (Ultra fast / Fast / Balanced / Accurate, also in *Segment a
database*) and the nnInteractive speeds. Two equal ways of doing something get **teal** and **rose**: the panels'
**◫ push** / **▣ over** button. The chosen preset is filled with its colour; the others show it in their text and
outline. Off: the usual accent colour (the push / over button is then neutral in both states, as it is a choice, not
an on / off switch). Script: `colorful on|off`.

### Window size

ORCA-MI starts maximized. **Restore down** (the button next to ×) gives a window of at least about half the screen
(60 % × 70 %, centred) when the restored size would be smaller. Script (tests): `windowstate [max|restore]`.

### 🎨 Appearance and styles

*View → 🎨 Appearance and styles…* (also the 🎨 button in the toolbar's Interface group: the colour theme, contrast and
interface size are chosen here, no longer in the toolbar) changes how ORCA-MI looks,
on top of any colour theme and contrast level. Nothing else changes: every tool, menu and setting stays where it is.

* **Styles** set everything at once (a new installation starts with **ORCA Cards**; your choice is kept): *ORCA Standard*, *Clinical reading room* (dark neutral surroundings
  and black viewports, so only the images draw the eye, with any theme), *Research compact* (more on screen),
  *Presentation* (large controls, names under the toolbar groups), *Soft teal* and **ORCA Cards**.
* **ORCA Cards** looks like the System monitor: a deep background (pale in light themes) with every panel section as
  a rounded card with more room and a larger title (a coloured dot shows its colour); the welcome page has larger
  action cards and a live *This computer* row (processor, memory, graphics card, with load bars and the GPU
  temperature); the CPU / RAM / GPU values in the top bar are small pills with a load bar; *Statistics in segments*
  shows MTV, SUVmax, SUVmean and TLG as large tiles above the table. Only the look changes.
* **Options** (change them after picking a style): density (compact, comfortable, spacious), corners (sharp,
  rounded, soft), surfaces (flat, layered cards, outlined, cards), accent colour (the theme's or one of seven), reading
  room, toolbar group names (on by default: each toolbar group has an outline with its name inside, under its tools), tool panel icons (small, medium, large), coloured section titles, the interface size and
  **Animations**: *Off*, *Subtle* or *Fancy* (the default: the image browser and the tool panel slide in and out,
  and a section card glows softly while it opens or closes). New installations start with the light *GitHub Light* theme.

**Mouse pointer shows the tool** (Settings → Appearance, or 🎨 Appearance and styles → *Mouse pointer*; on by
default): over an image the pointer follows the selected tool — an arrow for Navigate, a hand for Pan (closed while
dragging), a magnifier for Zoom, a crosshair for the drawing and clicking tools — with the tool's toolbar icon in a
small badge next to it (◐ W/L, ruler, brush, eraser, 🎯 nnInteractive point, box, scribble, lasso…). On a 3D view it
shows rotate, remove object, the nnInteractive MIP point, or keep / remove the clicked object. The tip of the pointer
is still the exact click point; switching it off gives the normal arrow everywhere. It costs no measurable time.
Script: `toolcursor on|off`.

The toolbar shows its buttons in groups (File, Layout, Navigate, Segment, AI, Display, Output, Interface); a group
that no longer fits moves to a second row. Script / Python: `appearance` opens the page, `appearance <style name>`
applies a style.

### Text on the views: sizes for papers and talks

Image tab → **Display** → *Corner text & orientation labels* (on/off for all of it), then:

* **corner text size** (8–36): patient name, ID and date (top left), slice, position and zoom (bottom left), W / L
  (bottom right);
* **orientation labels size** (8–60): the R L A P S I letters at the edges;
* **Image name, modality and unit (top right)**: shown or hidden on its own, with its own **size**, **bold** and a
  **dark background** behind it (for images with bright edges); the fusion line (⊕ overlay and opacity) belongs to it;
* **↺ default sizes** puts everything back.

Make the text larger before a screen capture for a slide or a figure. (*📷 Save screenshot* saves the image itself,
without the text.) Script / Python: `viewtext corner=20|orient=30|topright=1|trsize=18|bold=1|bg=1`.

### ◐ Window / level menu

The toolbar's **W/L** menu (Display group), a **right-click on the W/L mouse tool** (◐ in the Navigate group) and the
image's right-click menu (*◐ Window / level*) list the same choices as the Image tab's *Window / level* section:
**✨ Smart** (key **0**), **Full range**, **1–99 %**, and the presets of the image (CT: soft tissue, lung, bone,
brain, liver, mediastinum, stroke, angio; PET in SUV: 0–5 … 0–15, full range, 0–50 % max), each with its centre /
width and its key (**1–9**), with the image's current C / W at the top. The keys work on the active view.

**PET and NM images** have the same number keys on every image: **0** smart window, **1** full range, **2** 0–50 % of
the maximum, and **9 → 3** percentile windows of the body voxels (above 1 % of the maximum), brighter step by step:
**9** p1–p99, **8** p5–p95, **7** p10–p90, **6** p15–p85, **5** p20–p80, **4** p25–p75, **3** p30–p70. A short
message shows the window chosen. The SUV presets stay in the W/L menu (without a key).

### The tool panel and its icon rail

The tool panel on the right has a rail of coloured icons with the tabs' names (Image, Segment, 3D view,
Registration, AI models, Scoring, Dosimetry, CT dose, Cardiac, Compare images, Lesion tracking, Batch, Train AI,
Results, Info). Hover over an icon for what the tab does; the open tab's name and purpose are shown over its content.
*View → ▥ Tool panel icons* (or the Appearance page) makes the rail small, medium or large; drag the panel's left
edge to make the panel wider.

**Whole panels in their own window.** The top row of the tool panel (*TOOL PANEL*) has **⧉ Pop out the whole
panel**: the whole tool panel, with all its tabs and its icon rail, moves to its own window and the images get the
space. The image list (*IMAGE LIST*, left) has **⧉ Pop out the list** in the same way. In the main window a slim strip
stays on that side with **⇤ / ⇥**, *back* and *show* (bring the window to the front); in the window, **⇥ Put the whole
panel back** / **⇤ Put the list back** (or close the window). In a popped-out image list, double-click a thumbnail to
show it in the active view (dragging onto the views works only inside the main window). ORCA-MI always starts with
everything in the main window. Script: `panelout right|left[|0]`.

**Auto-hide.** The image list and the tool panel can each hide themselves (off by default, set separately for
left and right). The quickest way is the **pin** at the top of each panel (next to *Pop out*): pinned (highlighted) =
the panel stays; click it to unpin = auto-hide. The same choices are in Settings → Appearance and on a right-click on
the panel buttons at the right end of the toolbar. A hidden panel leaves a thin strip with a large arrow (› on the
left, ‹ on the right) on its edge: move the mouse onto it and the panel slides open; it stays open while the mouse is
inside it (or a menu opened from it is open) and slides away 1.5 s after the mouse leaves. By default the images make
room for the panel; the button next to the pin switches between **◫ push** and **▣ over** (slide over the images,
so the views keep their size); the same choice is the *slide over the images* tick next to the auto-hide tick. A panel or tab in its own window is never auto-hidden. The panels slide in and out
more slowly with *Animations* set to *Fancy* (Settings → Appearance) than with *Subtle*. Script:
`autohide left|right on|off|over|push`.

**Pop-out windows.** Every tab (Segment, Registration, AI models, Scoring, Dosimetry, Train AI, Batch …) can open
in its own window (like the NEMA IEC tool), for example to keep it open on a second screen: **⧉ Pop out** in the
tab's header (**⧉ Pop out this tab**: only that tab); several tabs can be out at the same time. A tab's work on the images (registration mouse editing and
points, cardiac axes, CT dose lines, lesion names, dose outlines …) stays on while its window is open. The window uses the same images, segmentations, views and running jobs as the
main window and is redrawn with it, so both always agree (move it to a second screen, for example). Meanwhile the
panel shows *open in its own window* with **🔝 Bring the window to the front** and **↩ Put it back in this panel**,
and the tab's icon in the rail has a small ⧉ (a click brings the window to the front). Close the window or press
**↩ Back to the panel** to put the tab back. Keyboard shortcuts of the views (tools, W/L keys, Ctrl+Z …) work
when the main window has the focus: click on the images first. Script: `popout <tab>[|0]` (e.g. `popout segment`).
## 2. Loading and viewing images

### What ORCA-MI reads, shows and computes

| Area | What you get |
|---|---|
| **Formats in** | DICOM (CT, MR, PET, SPECT/NM, CR/DX/MG, US, XA, enhanced multi-frame, JPEG/JPEG-2000/RLE compressed), **RTSTRUCT**, **RTDOSE**, **DICOM SEG**, NIfTI-1/2 (.nii/.nii.gz), Analyze (.hdr/.img), NRRD/NHDR, MetaImage (.mha/.mhd), NumPy (.npy), PNG/JPEG/BMP/TIFF |
| **Formats out** | NIfTI, NRRD, MHA/MHD, NPY, DICOM series, **DICOM SEG, RTSTRUCT and measurement SR for PACS**, STL/OBJ meshes, PNG/JPEG figures, GIF movies, CSV (stats, metrics, scores, TACs) |
| **Patient database** | Point it at one or more PACS-like folders: every DICOM file is indexed into patients → studies → series (NIfTI / NRRD / MHA / NPY files are listed per folder). Searchable by name, ID, date, description, modality or accession; click a series or "Load study" **Group by** patient name (A–Z), patient ID, year or month (newest first; each study then shows its patient), filter by **modality** and **date** (today, last 7 / 30 days, 3 / 12 months, 5 years); the choices are remembered. The index is saved and updated incrementally (only new files are read), optionally on start-up. Ctrl+B or 🏥 in the toolbar |
| **Viewing** | Radiant-style drag & drop of thumbnails onto viewports, 1×1 … 3×3, 4×4, 5×5 / 1+3 / MPR / two MPRs side by side layouts, linked cursors, crosshair, zoom/pan/flip, 22 colormaps, modality-aware **smart window/level** + presets, fusion overlays (PET/CT, SPECT/CT, dose), voxel value and label under the cursor, corner info, orientation labels, colorbar, cine |
| **4D / dynamic** | Dynamic PET/MR/CT from DICOM or NIfTI, frame slider, cine, time-activity curve at the cursor; **motion correction, TAC per segment, Patlak Ki (+ Ki map), multi-time-point half-life and TIA** |
| **Workflow** | **Hanging protocols** (automatic PET/CT, SPECT/CT … screens, your own), **autosave and crash recovery**, workspaces with segmentations |
| **3D** | GPU (wgpu) or multithreaded CPU ray casting: MIP, MinIP, DVR with shading, iso-surface, segmentation surfaces, clipping box | Trackball rotation (the model follows the mouse, no gimbal limits), one-click ⟲ reset and A / P / L / R / S / I viewpoints on the 3D viewport, orientation letters and an axis compass, automatic CT table removal.
| **Segmentation** | Multiple segmentations/labels, brush (2D/3D, round/square), eraser, polygon, region growing, threshold, erode/dilate/open/close (mm), fill holes, keep largest, remove small, split components, slice interpolation, lock labels, paint-over modes, undo/redo |
| **AI** | **nnInteractive** click/box/scribble/lasso segmentation; **nnU-Net v2** inference (multi-channel, folds, TTA); image-to-image models (denoising, translation) via your `yazdan.DL.model_inference_regression_multi_workers` (queued async saving), a standalone MONAI runner, TorchScript, or any custom command; batch queues |
| **Quantification** | SUVbw / SUL / SUVbsa from DICOM tags or manual entry; segment statistics (volume, mean, SD, min/max, median, percentiles, SUVpeak 1 mL, TLG); Dice, Jaccard, sensitivity, specificity, precision, volume similarity, Hausdorff, HD95, ASSD, MASD, surface Dice, centroid distance (Segment tab → 📐 Compare segmentations; with *All labels of A*, each label and their **mean over all labels**) |
| **Registration** | Manual interactive (live fused overlay), image-center and center-of-mass alignment, automatic rigid / similarity / affine (mutual information, NCC, MSE; multi-resolution), deformable Demons; resample moving image + its segmentations |
| **Reader studies** | Customisable scoring template (Likert, slider, yes/no, choice, free text) for image quality, confidence, conspicuity, artifacts, …; point annotations with text; nicknames & comments per image; CSV + JSON export |
| **Look & feel** | 10 themes (Adwaita dark/light, Nord, Dracula, Catppuccin, Gruvbox, Tokyo Night, Solarized, Ubuntu, Matrix), GNOME-style rounded widgets, UI scaling for any screen size |

### Drag & drop roles

Dropping a file (from Explorer) or a thumbnail onto a viewport asks how to use it. The view you release the mouse
over is the one chosen in the dialog (while dragging from Explorer it is outlined, *Drop into view N*); you can still
change it there.

* **Image**: shown in that viewport, with a colormap of your choice (or the modality default).
* **Fusion overlay**: fused with colormap and opacity. **Target:** *All views (keep the layout)* (default: fused on
  every view of the current layout, e.g. all MPR planes, without changing the layout or the images) or one chosen view.
* **Segmentation / label map**: attached to the image in the viewport (resampled if the grid differs), with label
  colors chosen as distinct colors, spread over any colormap, or a single color, plus opacity.

**Several files at once** (NIfTI, NRRD, MHA … , not DICOM): the *Load N files* dialog has one row per file:
* **Use as**: *Image*, *Fused on…* or *Segmentation of…*.
* **On image** (fused / segmentation): the image in the view, any loaded image, or another file of the same drop
  (loaded as an image; a segmentation can also go onto a file that is fused).
* **Study**: *as in the file*, any loaded study, or a new study: type its name (and a date, empty = today) next to
  *➕ New study*, press *Create*, then choose it (★) for the files; files without a study go into it at once.
* **Nickname** (a segmentation: its name).

File names with seg / label / mask / roi / contour start as segmentations. Script: `multidrop file|role|on|study|nickname; …`
(role image / fused / seg; on view, row:<k>, image:<index>; study keep, new:<name>, existing:<image index>; `dialog;`
first opens the dialog instead).

Shortcuts: **Shift + drop** = overlay, **Ctrl + drop** = segmentation (every file the same role). Tick "Don't ask again" to always use
your last choice, and turn the question back on in *Tools → Settings*. Existing segmentations can be recolored
in the Segment tab (🎨 Recolor labels).

### Overlay sync & roles

* **⊕ Sync overlay** (toolbar, Image tab, key `O`, on by default): the fusion overlay and its opacity are the
  same in every view of the same image (all MPR planes). `,` and `.` lower or raise the overlay opacity.
* **Change role after loading:** right-click an image → *🔁 Change role* (image / overlay on a viewport /
  segmentation of another image). In the Segment tab, ⋯ next to a segmentation converts it to an image or moves /
  copies it to another image. Python: `v.set_role(1, "seg", 0)`.

### ✚✚ Two MPRs side by side

Layout *Two MPRs side by side*: two images, each with axial, sagittal, coronal and 3D. Right-click an image →
**✚✚ Two MPRs side by side** → *Show in the left / right MPR* (switches to the layout) or *Fuse on the left / right
MPR*. A thumbnail dropped on any view of one MPR goes to all four of its views (as the image, or with Shift / the
fusion role as a fusion overlay on that MPR only); the other MPR stays as it is.

### 🖼 Hanging protocols

A hanging protocol arranges the screen for a kind of study: layout, which image goes where, fusion, view
direction, colour maps and windows. Apply one from the Layout menu, or switch on *Apply automatically after
loading*: the first enabled protocol whose rule matches is then applied after each load (a short message names it).
This is off by default: a DICOM folder with several series shows its **first series alone in the MPR layout**
(axial, sagittal, coronal, 3D); the other series wait in the image list, ready to be dragged onto a view or fused.

Built-in protocols:

| Protocol | Needs | Screen |
|---|---|---|
| PET/CT | PT + CT | 2×2: CT, PET, fusion axial, fusion coronal; CT soft-tissue window, PET hot iron |
| SPECT/CT | NM + CT | 1×3: CT, SPECT, fusion |
| PET/MR | PT + MR | 1×3: MR, PET, fusion |
| CT | CT | MPR (axial, sagittal, coronal, 3D) |
| PET | PT | axial, coronal, sagittal with inverted grey |

**Use and manage them:** Layout menu (toolbar) or View → **🖼 Hanging protocols**: apply one by hand, switch the
automatic application on or off, or open **⚙ Manage protocols…**:
* **➕ Save current screen as protocol** stores the current layout, views, fusion, colours and windows.
* Each protocol has a **rule**: the modalities that must be loaded (`PT+CT`) and an optional text the image or
  series name must contain (`PSMA`). The list order is the priority (⬆ ⬇); ✔ marks protocols that match now.
* Per viewport: image modality, fusion-overlay modality and view; per modality: colour map and a fixed window
  (or automatic).
* Protocols are saved in `%APPDATA%\ORCA-MI\hanging_protocols.json` (📂 *Open file* to edit by hand).

Protocols are not applied while a reading session runs, to workspaces you open, or to images loaded by scripts /
the Python API. Script / Python: `hanging`, `hanging PET/CT`, `hanging auto=0`, `hanging save=My PET/CT`;
`v.hanging_protocol("PET/CT")`.

### 3D view

* **CT colours** (3D tab → *Renderer*, CT images only): colour and opacity per HU range instead of the window /
  colormap: **Bones**, **Bones B/W**, **Bones and skin 1 / 2**, **Bones, muscles and skin**, **Angio** (contrast
  vessels in red), **Airways and lungs** (glass-like cyan air / tissue borders), **Skin B/W**, **MIP B/W** and
  **MIP B/W inverse** (white background). Choosing one switches to DVR (or MIP); *Off* goes back to the usual
  rendering, and changing the mode turns it off. Hover a preset for what it shows. Script: `ct3d <preset>|off`.
* **Quality presets:** 3D tab → *Renderer* → *Quality* **Low** / **Balanced** / **High** set the samples along the
  ray, the CPU / GPU resolution and the shading together (hover a preset for its values). *Low* (½ samples,
  128 / 256 voxels, no shading) for slow computers or laptops on battery; *Balanced* (the default: 1×, 256 / 512,
  shading); *High* (2×, 384 / 1024, shading) for a good GPU (≥ 6 GB). Moving a slider gives *custom*. Script:
  `quality3d low|balanced|high`.
* **Several 3D views:** 3D tab → *Several images in 3D*: tick 2–4 images → *Show in 3D side by side* (MIP, DVR …).
  🔗 links rotation and zoom of all 3D views.
* **3D editing** (second toolbar row of a 3D view showing a segmentation — its own or another image's, e.g. after a registration): **✂ Remove object** deletes the
  connected object you click; **⌫ 3D eraser** erases a sphere (radius in mm) where you paint on the surface. The
  eraser's sphere follows the mouse at its true size, with its radius (*r 15 mm*): **orange** over a segmentation
  (a click erases there), **blue** elsewhere. Shift+drag still rotates, Ctrl+Z undoes. Script: `tool3d 0|1|2`, `erase3d <mm>`.
* **Opacity on the image:** every 2D view with a fusion overlay or segmentation shows ◐ Fusion / ▦ Seg sliders in
  its header, so you don't need the Image tab.
* **Segmentation opacity per view:** the ▦ Seg slider of a view changes the segmentations' opacity **in that view
  only** (e.g. strong on the CT views, faint on the PET view); the other views keep theirs. **↺** next to it goes back
  to the segmentation's own opacity (Segment tab). The same slider is in the view's right-click menu, under *Show
  segmentation*. Saved with workspaces. Script: `viewsegopacity <0..1|own>[|vp=<i>]` (`segopacity` still sets the
  segmentation's own opacity, for every view).

### 3D view: image and segments on / off

Every 3D view has **🖼 Image** and **▦ Segments** checkboxes (second toolbar row).
* Untick *Image* to see only the segmentation surfaces. This is also much faster.
* Untick *Segments* to see only the image.
* **✚ Crosshair** shows where the crosshair of the 2D views is: a yellow point, lines through it along the three
  image axes and the outlines of its axial, coronal and sagittal slices. Untick it to hide them. The 3D tab has the
  same switch (**✚ Crosshair in 3D**) and the style: **Lines + slice boxes** or **Lines only** (script
  `crosshair3d boxes|lines|off`).

Python: `v.show_3d(image=False, segments=True)`.

**◩ Image in segments** (organ-based view; also in the 3D tab): the image is rendered only inside the segments shown
in 3D. Show only the liver (its 3D eye in the segment list) to see the liver's PET or CT alone; add the kidneys and
their MIP appears too. Untick *Segments* to see the image without the surfaces. Script: `view3dmask on|off`.

### Colormap gamma and colorbar

Image tab → *Colormap* → **Gamma** (as ITK-SNAP's contrast curve): the window position *t* (0…1) is shown with the
colour of *t*^gamma. Below 1 it spreads the low values (more contrast in faint uptake or soft tissue), above 1 the high
values. The small curve under the slider shows the mapping; **1** resets it. It applies to the 2D views, fusion
overlays, thumbnails and the 3D rendering. Script: `lutgamma 0.5`.

Every 2D and 3D view shows a **colorbar** with five values and the unit, and a second one for a fusion overlay.
When the mouse is over a segment or lesion on a 2D view, its name is shown next to the cursor (every segmentation
shown on that view); *View → Segment names under the mouse* turns it off.

It follows the window and the gamma. Each image's colorbar can be shown or hidden on its own: *Image tab →
Colormap → Colorbar on the views*, *Fusion overlay → Overlay colorbar*, or right-click on a view → *Colorbar of …*
(image or overlay). *View → Colorbar* turns all of them off or on. Script: `colorbar on|off`, `colorbar off overlay`,
`colorbar all off`.

**Using the colorbar with the mouse** (as in the cardiac splash view): **drag the top half** of a colorbar up or down
to change the window's maximum, **drag the bottom half** to change the minimum (the grip you hold is highlighted),
and **click** the bar to choose the image's colours. With a fused image there are two bars: each changes its own
image (the base image or the overlay). A hidden colorbar (see above) has none of this. Script (tests):
`colorbars [view]` lists the bars with their window and colours.

The colormaps include 3D Slicer's PET tables, defined exactly as in Slicer (vtkMRMLPETProceduralColorNode):
**PET-DICOM** (the DICOM PET colour palette, PS3.6 B.1.2), **PET-Heat**, **PET-Rainbow**, **PET-Rainbow2** and
**PET-HotMetalBlue**. *More: 3D Slicer tables* adds Slicer's other colour scales, taken from 3D Slicer 5.11 itself
(identical tables): FullRainbow, Iron, Ocean, Desert, ReverseRainbow, Cyan, Magenta, RedGreenBlue, Warm1–3, Cool1–3,
WarmShade1–3, CoolShade1–3, WarmTint1–3, CoolTint1–3, fMRI, fMRIPA, dGEMRIC-1.5T / 3T, ColdToHotRainbow,
HotToColdRainbow, DivergingBlueRed and SlicerRT's Dose and Gamma tables. Viridis, Magma, Inferno, Plasma and
Cividis use Slicer's exact 256-entry tables.

A grey PET / SPECT used as a fusion overlay starts in Hot Iron (that becomes its own colormap, so its thumbnail and
its 3D rendering use the same colours). A CT or MR fused on a PET keeps its grey. The fused image is always drawn in
the colormap chosen for it in the Image tab, Grayscale included; untick *Transparent below window* there to see a
fused CT in full (otherwise values below its window, e.g. air, are transparent).

### 📈 Line profiles

Tool **📈 Line profile** (key **L**): drag a line on any axial, coronal or sagittal view, in any direction, or click the
start and then the end. The line is drawn on the 2D views that contain it and on the 3D views. The **Line profile**
window shows the values along the line:

* **Images and legend:** tick the images to compare (default: the images on the views; they may have different grids
  and are sampled in world coordinates through their registration). Each legend entry can be renamed. Title and axis
  labels can be changed too.
* **step** (0 = half the smallest voxel), **linear** or **nearest** interpolation.
* **Gaussian fit (FWHM):** least-squares Gaussian (with or without a constant baseline) per curve, drawn dashed;
  the table gives the fitted FWHM, the FWHM measured on the curve (half-maximum crossings), the centre, amplitude and R².
  Tested against scipy `curve_fit`.
* **CSV:** one row per point with the distance, the x, y, z world (LPS) coordinates, then for every image its value and
  voxel coordinates. The header lines give the line ends, length, step, and for every image the legend, name, unit,
  file and the fit results.
* **Editing a line:** with the 📈 tool, click a line (or its number in the window) to select it; its ends get square
  handles. Drag an end to rotate and resize the line (hold **Shift** to keep its length), drag the middle to move it.
  The curves follow while you drag.
* **figure** sets the plot width (auto = the window width) and height; **text size** scales only the texts (axes,
  legend, information line and fit table). Both are used for the PNG and the SVG.
* **PNG** saves the title, the plot, the information line (length, points, step, interpolation) and the FWHM table
  as shown; **SVG** saves the same as a vector figure on a white background, for papers.

**Where and how long:** the view shows the length next to the line number (*profile 1 · 63.2 mm*) and, for the
selected line, the voxel of each end. Under the plot the window lists both ends in world coordinates (LPS, mm) and
in the voxels of every sampled image.

Several lines can be kept: choose one with the numbers at the top of the window. Python:
`v.command("profile a=x,y,z|b=x,y,z|images=0,1|legend=0:CT;1:PET|font=1.5|csv=line.csv|svg=line.svg")`.

### 📍 Values of all images at the crosshair

Image tab → **📍 Values of all images at the crosshair** (open at the top): click a point on any view and it lists
every loaded image with its value there (unit, frame of a 4D image), its voxel, and the labels of its segmentations
at that voxel; *outside this image* where the point is not covered. The point is mapped through the registrations
(as the fused views show it); the value is that of the nearest voxel in the current frame. The active image is in
bold. **⧉ Window** keeps the list in a floating window on every tab; **📋 Copy** puts it on the clipboard as CSV.

Script / Python: `probe` (at the crosshair) or `probe x,y,z` (world LPS, mm) prints one `[probe] index=…|name=…|
voxel=i,j,k|value=…|unit=…|labels=…` line per image; `probe window` opens the window.

### 🌫 Filters and denoising

Image → **🌫 Filter / denoise** → choose a filter. The dialog shows the parameters of that filter, with defaults
from the image (the noise-related values from its intensity range):

| filter | parameters |
|---|---|
| Gaussian | FWHM (mm; σ shown) |
| Median, Mean (box) | window 3, 5, 7 or 9 voxels |
| Bilateral (edge preserving) | spatial σ (mm), range σ (image units: differences larger than ~2σ are edges and kept) |
| Anisotropic diffusion (Perona–Malik) | iterations, conductance K (image units), time step |
| Non-local means | h (strength, about the noise SD), search and patch radius (voxels) |
| Butterworth (low pass) | cut-off (cycles/cm, shown as a fraction of Nyquist), order |

* **2D: each slice alone** — no smoothing between slices (thick slices).
* **Result:** a **new image** (default) or **replace this image**. The new image is named after the image, the filter
  and its parameters, e.g. *PET · Gaussian FWHM 6 mm*, *CT · median 5×5×5*; the name follows the parameters until
  you edit it. It keeps the display settings and the registration of the original, and takes its place in the views.
* Every frame of a 4D image is filtered. The job runs in the background (progress, cancel). Slow settings (large
  NLM search) and the memory needed by the 3D Butterworth are warned about.

Script: `filter gaussian|fwhm=4`, `filter median|window=5`, `filter bilateral|sigma=2|range=50`,
`filter diffusion|iter=10|k=30|dt=0.06`, `filter nlm|h=20|search=2|patch=1`, `filter butterworth|cutoff=0.8|order=5`,
plus `|2d=1`, `|new=0` (in place), `|name=…`, `|image=<i>`.

### ▦ Resampling to a spacing

Image → **▦ Resample to a spacing…** gives the image a new voxel spacing, e.g. 1 mm isotropic, or 1×1×3 mm.
* **New spacing:** one value (*isotropic*) or x, y, z; the buttons 0.5 … 5 mm, *in-plane ×, z kept* and *as now*.
  The dialog shows the current spacing and voxels and the size of the result (voxels, MB).
* **Interpolation:** **nearest** (keeps the original values: label maps, masks), **linear** (trilinear, no overshoot)
  or **B-spline** (cubic, as `sitk.sitkBSpline`: the sharpest; it can overshoot next to sharp edges, so *clip to the
  original value range* is on by default, e.g. no negative PET values).
* The grid keeps the origin (centre of the first voxel) and the orientation, as SimpleITK does; the number of voxels
  is round(n × old spacing / new spacing). Inside the image the values equal SimpleITK's `Resample` with the same
  interpolator; a last row that falls past the last voxel centre but still inside that voxel takes the edge value
  (SimpleITK gives 0 there).
* Its segmentations are resampled too (nearest), if ticked. Every frame of a 4D image is resampled.
* The result is a **new image** (name e.g. *CT · 1.5 mm bspline*, editable) shown in the place of the original, with
  its display settings and registration. The job runs in the background (progress, cancel).

Script: `resample 1.5|interp=bspline`, `resample 1,1,3|interp=nearest|segs=0`, plus `|clip=0`, `|name=…`,
`|image=<i>`. (`resample` alone still resamples the moving image onto the fixed grid.)

### ⇄ Match space and ◩ masking to segmentations

*Image → Match space to another image…* resamples an image onto the grid of another (as `yazdan.image.match_space`;
identical voxels with linear or nearest interpolation): choose the reference, the interpolation, the value outside
(0, −1024 for CT…) and optionally bring its segmentations. Script: `matchspace image=0|ref=1|interp=nearest|default=0`.

*Image → Mask to segmentations…* (also **◩ Mask an image to it…** next to *Create body contour*) keeps an image only
inside the chosen labels of any segmentations (of any image: they are mapped onto the image's grid with nearest
neighbour). Outside value 0, the image minimum or any value; *keep outside* removes the segments instead; *crop*
cuts the result to the kept region. As `yazdan.image.mask_image_to_seg`, but without its loss of edge voxels (that
function resamples the label map with linear interpolation, which drops about 2 % of an LV mask on the same grid).
Script: `maskimage image=0|seg=0:1:1;0:1:2|value=0|invert=0|crop=0`.

### ✖ Scaling the values

*Image → Scale values by a factor…* multiplies every voxel (all frames) by a factor, as a new image or in place, and can
set the unit (e.g. 0.001 for Bq/mL → kBq/mL, a calibration factor). The window is scaled with the values.
Script: `scale 0.001|new=1|unit=kBq/mL`.

### ➕ ➖ Sum and subtraction of two images

*Image → ➕ Sum of two images…* / *➖ Subtract two images…* make a new image **A + B** or **A − B** (optionally with a
factor on B: A ± factor × B). The result is on the grid of A: when B has another grid or a registration, it is
resampled onto A (linear, with its registration); the unit, patient and colours come from A. Multi-frame images: frame by
frame when both have the same grid and frames, otherwise B's shown frame is used for every frame of A.
Script: `imagemath <A index>|<B index>|op=add|sub|factor=1|name=<name>`.

### ☢ Q.SPECT: quantitative SPECT with conversion factors

*Image → ☢ Q.SPECT: quantitative SPECT…* (also in the 🖼 Image tab → *PET / SPECT*) turns a reconstructed SPECT image (counts) into activity concentration
(e.g. Bq/mL) with a **conversion factor (CF)** from your own calibrations.

**The scanner library** (section *📚 Scanner library* of the window):

* **➕ New scanner**: a name, manufacturer / model (as in the DICOM header: an image of that model selects the scanner
  automatically), a comment, and what its acquisition time means: **time per projection** (conventional SPECT, the
  time per azimuth / view) or **total acquisition time** (systems such as StarGuide).
* **Reconstructions** of the scanner, one row each: the left box is its **name** (e.g. *OSEM 4i8s AC SC RR*), chosen in
  the *Reconstruction* list when converting, and each conversion factor belongs to one; the right box is a free
  **comment** (iterations, filters, corrections), shown as its tooltip and in the converted image's Info. The boxes
  grow with their text; a long one scrolls sideways.
* **Conversion factors**: one per **isotope and reconstruction**: the CF (activity concentration per voxel unit), the
  unit of the result, the **reference acquisition time** of the calibration (s per projection or s total), the date
  and a comment (phantom, source, method…).
* **📋 Scanners** lists every scanner with its reconstructions and CFs (✏ edit opens one).
* The library is saved at once in `%APPDATA%\ORCA-MI\qspect_library.json` (the previous version in
  `qspect_library.bak.json`). It belongs to you, not to the program: **updating or reinstalling ORCA-MI keeps it**.
  **⬆ Export JSON…** saves it for documentation or another PC; **⬇ Import JSON…** adds the scanners and CFs of an
  exported file (nothing is overwritten; a CF already there is not added twice).

**Converting:** choose the **image** (by default *Active image*, which follows the active view; or any loaded image,
☢ = NM / SPECT), the scanner, isotope and reconstruction, and enter the **acquisition time of the image**
(per projection or total, as for the scanner; filled in from the DICOM fields when they have it). Voxel values grow
linearly with the acquisition time, so a longer acquisition needs a smaller CF:

> CF used = CF × reference time / image acquisition time, and Q.SPECT = image × CF used.

Example: CF 0.5 Bq/mL per count calibrated at 20 s per projection; an image of 40 s per projection uses 0.25.
**☢ Convert to Q.SPECT** makes a new image *<name> QSPECT (isotope, reconstruction)* in the CF's unit. Its comment
and its *Info* list the scanner, isotope, reconstruction (with their comments), the CF, its comment and date, the
reference and image times and the CF used, so the result documents how it was made. No decay correction is applied.

Script: `qspectfactor scanner=Intevo|kind=projection|recon=OSEM 4i8s|isotope=Lu-177|cf=0.5|ref=20|comment=NEMA phantom`
(adds or updates a scanner, reconstruction and CF), `qspect scanner=Intevo|isotope=Lu-177|recon=OSEM 4i8s|time=40` (add `|image=<index>` for an image other than the active one),
`qspectlist`, `qspectexport <file.json>`, `qspectimport <file.json>`.

### ⏳ Decay correction

*Image → ⏳ Decay correction…* (also in the 🖼 Image tab → *PET / SPECT*). Choose the **radionuclide** from the list
(F-18, Ga-68, C-11, N-13, O-15, Rb-82, Cu-64, Zr-89, I-124, Sc-44, Tc-99m, I-123, In-111, Ga-67, Tl-201, Xe-133,
I-131, Lu-177, Y-90, Ho-166, Sm-153, Re-186, Re-188, Cu-67, Tb-161, Sr-89, Pb-212, At-211, Ac-225, Ra-223, Th-227,
Ra-226, Ge-68, Na-22, Co-57, Cs-137, with their half-lives) or enter your own half-life. For a DICOM image the
radionuclide and the acquisition time are filled in from the header.

**Times** are written as `yyyy.mm.dd hh:mm:ss` (e.g. `2026.10.31 14:05:00`; `yyyy-mm-dd`, no seconds, and DICOM
`yyyymmddhhmmss` are accepted too), picked with the 📅 calendar and the hour : minute : second boxes, or set with
*now*, *= acquisition*, *= injection* (from the DICOM header) and *⇅ swap*. Time 1 is the acquisition (reference) time,
time 2 the target time. The window shows Δt and the decay factor A(2) / A(1) = 0.5^(Δt / T½).

* **🧮 Activity calculator:** type the activity at time 1 *or* at time 2, in Bq, kBq, MBq, GBq, µCi, mCi or Ci; the other
  one is calculated, and both are listed in every unit (1 mCi = 37 MBq).
* **🖼 Decay-correct the image:** every voxel (all frames) × the decay factor, so the image shows the activity at the
  target time: a later target gives lower values (physical decay), an earlier one higher values (e.g. back to the
  injection time). As a new image *<name> decay→<target>* or overwriting the image. The comment and *Info* keep the
  nuclide, half-life, both times and the factor.

Script: `decay nuclide=Lu-177|from=2026.10.30 10:00:00|to=2026.10.31 10:00:00|new=1` (from: default the image's
acquisition time; `halflife=<s>` instead of a nuclide), `decaycalc activity=7.4|unit=GBq|nuclide=Lu-177|from=…|to=…|out=mCi`.

### 🔢 Data type, clipping, normalisation and percentiles

ORCA-MI keeps every image as **32-bit float** in memory, whatever its file type: uint16 / int16 DICOM and NIfTI values
are exact, and resampling, filters, scaling, SUV, Q.SPECT and decay correction all compute in float, so nothing is
rounded on the way. Saving as NIfTI writes 32-bit float, except a CT whose values are all whole numbers in the int16
range (int16, lossless) and an image converted with *Convert image data type* (that type).

*Image → 🔢 Values*:

* **Convert image data type:** float32 (single precision), float64 (double precision), int32, int16, uint16 or uint8.
  Integer types either **round and clip** to the type's range (the window reports how many voxels had decimals and
  how many were clipped) or **rescale** the image's min … max onto the whole range first (e.g. 0 … 255 for uint8).
  The type is used when the image is saved as NIfTI.
* **Clip image values:** a lower and / or an upper value (buttons for min, p1, 0, p99, p99.9, max).
* **Normalize image values:** source range = values you enter, the image's min … max, min … 99th percentile or
  1st … 99th percentile (exact, all voxels), mapped linearly onto a target range (default **0 … 1**, any range
  allowed), with or without clipping to the target range.
* **Histogram percentiles:** any percentiles (e.g. `67, 95, 99.5`) plus the 1st, median and 99th, exact (sorted
  voxels, interpolated as numpy), optionally ignoring voxels equal to 0 or over all frames. 📋 copies them.

Each makes a new image or overwrites the image. The histogram in the 🖼 Image tab marks the **99th percentile** (dashed
orange line) and lists the median and p99 below.

Script: `convertformat type=uint16|rescale=0|new=1`, `clip lo=0|hi=1000`, `normalize src=minp99|to=0,1|clip=1`,
`normalize src=manual|min=-1000|max=1000|to=0,1|clip=0`, `percentiles 67,95|ignorezero=1`.

### 🎯 NEMA IEC phantom analysis

*Tools → 🎯 NEMA IEC phantom analysis…*, the 🖼 Image tab → *PET / SPECT*, or *🎯 Send to NEMA IEC…* in the right-click
menu of an image opens the NEMA IEC body phantom tool (the *NEMA IEC CR Tool*, built into ORCA-MI) in its own window.

**Interface size of the NEMA window**: **🔍 100 %** next to its *🐋 ORCA-MI* menu (75 … 200 %), or Ctrl + / Ctrl − /
Ctrl 0 in that window, scales the NEMA window only; ORCA-MI's main window keeps its own size (View → Interface size).
It is remembered. When the window is narrow (or the size large), the header's buttons go to a second row.
Script: `nemazoom 1.25`.

**Sending several images at once:** with more than one image loaded, the *🎯 Send images to NEMA IEC* dialog lists them
all. Tick the images, choose each role (★ primary PET/SPECT — one, it defines the ROI grid —, additional PET/SPECT
for other reconstructions, CT — one) and the comment shown in the tool (e.g. the reconstruction), then *Send*. PET and
SPECT images are ticked by default, the active (or right-clicked) one as primary, plus the first CT. With *Keep each
image's ORCA-MI colormap and window* (on by default) every image keeps its colormap (shown as 🐋 in the tool's
colormap list; choosing another colormap there replaces it) and its window; the CT's window becomes the CT window.
More images can be sent later from the tool's 🐋 ORCA-MI menu → *Add several ORCA-MI images…*. Its calculations, reports and sessions are those of the standalone tool, so the results
are identical (checked on an EARL phantom with two reconstructions: every sphere and background value the same).

* **Images:** primary PET/SPECT (defines the ROI grid), more reconstructions as *additional* PET/SPECT (same ROIs,
  results side by side), an optional CT (fusion, air removal). Units: Bq/mL (PET) or counts (SPECT, with calibration).
* **ROIs:** the six spheres (37 … 10 mm), background ROIs (replicated per NEMA), lung insert; click to place, snap to
  the hot sphere, 3D spheres or 2D circles, hand painting (e.g. to cut an air bubble), label map import / export.
* **Setup:** sphere-to-background ratio (manual, from concentrations or from the syringe activities), peak radius,
  cold background (absolute recovery), decay correction of the expected concentration, SUV, report information.
* **Calibration:** SPECT calibration from a uniform phantom (total activity or mean in a uniform region), with
  decay correction → counts per voxel per Bq/mL.
* **Views:** ortho, side by side, 3D; **Smooth** (key **I**) switches between interpolated display and voxels as blocks
  (starts as ORCA-MI's *Smooth interpolation*; display only, the results do not change).
* **Results:** mean / max / peak contrast recovery, NEMA QH, background variability (COV), recovery curves.
* **Export report:** PDF, Excel (re-importable), session, label map, figures (axial, ortho, fused, side by side, MIP,
  3D segments) and GIFs.

The **🐋 ORCA-MI** menu of the window links it to ORCA-MI:

* **Add as primary / additional PET/SPECT / CT:** any image loaded in ORCA-MI (no second loading of the files).
* **Send ROIs to ORCA-MI as a segmentation:** the ROIs become the segmentation *NEMA ROIs* of the primary image
  (labels 1–6 spheres, 7 background, 8 lung), shown and editable on every ORCA-MI view.
* **Use an ORCA-MI segmentation as ROIs:** e.g. spheres corrected or drawn in ORCA-MI, or a registered template.
* **Save the calibration as a Q.SPECT conversion factor:** the calibration becomes a CF of the Q.SPECT scanner
  library (CF = 1 / calibration factor, reference = the calibration's acquisition time; for a scanner with times per
  projection, enter the number of projections).

Script: `nemawindow`, `nemaadd [keep=0]` (send the loaded PET/SPECT and CT with the default roles), `nemaseg`,
`nemasend`, and headless `nema session=<file.json>|out=<folder>|reader=orca` (calculates
a saved session and exports the full report; `reader=nema` uses the tool's own DICOM reader).

### 🧠 Brain PET resolution (EIR, EARL)

*Tools → 🧠 Brain PET resolution (EIR, EARL)…* or the 🖼 Image tab → *PET / SPECT* opens its own window, the same
calculation as `yazdan.Brain_EARL.calculate_curve_and_resolution`, for the effective image resolution (EIR) of a
brain PET (e.g. a Hoffman phantom):

1. choose the **PET** and the **grey matter** and **white matter** segmentations (any segmentation of any image, one
   label or *every label*; e.g. masks from an MRI or a CT registered to the PET: they are put on the PET grid by nearest
   neighbour, with the registration). Segmentations named grey / white matter (GM / WM) are chosen for you;
2. a digital reference object (DRO) is made on the PET grid: white matter 0.25, grey matter 1.0 (adjustable);
3. for every FWHM from 0.1 to 15 mm in steps of 0.1 mm (adjustable) the DRO is smoothed with a Gaussian (SimpleITK
   *DiscreteGaussian*: same kernel, error 0.01, width 32, variance in mm²), scaled to the PET by least squares inside
   grey + white matter, and the **mean absolute difference** to the PET is recorded;
4. the FWHM with the smallest difference is the **EIR** (red); the largest difference is also given.

The window shows the curve (hover for the values; click to show that FWHM), and the PET next to the smoothed DRO at
any FWHM and axial slice (the EIR is marked ★). **💾 Save results…** writes a report folder: Excel with the sheets
*curve* (fwhm_mm, difference, scale) and *summary* (eir, min_difference, max_difference, fwhm_at_max, settings) as in
the yazdan file (so `yazdan.Brain_EARL.plot_scanner_comparison` / `plot_from_excel` read it), CSV, the plot as PNG /
SVG, HTML and JSON. **➕ DRO at the EIR as an image** adds the smoothed, scaled DRO as a new image on the PET grid.

Checked against the Python function: same EIR, minimum and maximum, every curve point within 3·10⁻⁷ (relative), on
two phantoms (masks on the PET grid and on a 1 mm grid); about 10× faster (0.5 s for 150 kernels).
Script: `braineir pet=0|gm=0:0:0|wm=0:1:0|min=0.1|max=15|step=0.1|gmv=1|wmv=0.25|out=<folder>|dro=1`
(`gm` / `wm` = image index : segmentation index : label, 0 = every label; prints `[braineir] eir=…`), `braineirwindow`.

### Loading: role, nickname and comment

**Layout when images are opened** (File → ⚙ Settings): the layout used when nothing is shown yet and images are
opened by double-click, drag & drop or File → Open: **MPR** by default, any other layout, or *keep the current
layout*.

**Nickname from the header** (Info tab → Nickname & comments): tick **modality**, **date** and **scanner**, press
**✏ Name from header**: the nickname becomes e.g. `CT--2018-11-15--Symbia Intevo 16` (series / study date, scanner
model); you can still type your own. Script: `nickname auto[=modality,date,scanner]`.

Dropping a file (or opening one file with File → Open) asks how it is used (image, fusion overlay, segmentation),
in which view (the view under the mouse is preselected; an empty view gets "image"), and lets you give a
**nickname** (shown instead of the file name; for a segmentation, its name) and a **comment**. *Don't ask again*
keeps the settings; Shift + drop = overlay, Ctrl + drop = segmentation.

When closing, ORCA-MI also warns about running jobs (AI, downloads, registrations) and about images registered since
the last workspace was saved.

## 3. Segmentation and measurements

### 📅 Studies in the image list

**Where each image is shown:** small badges under an image's card give the views showing it in the current layout:
*1 Ax*, *2 Sag*, *3 Cor*, *4 3D* (view number and kind), **MPR** when it fills the MPR layout (*MPR left* / *MPR right*
in Two MPRs), and an orange *⊕2 Sag* when it is the fusion overlay of a view. The badge of the active view is filled.
Hover a badge for the details.

Each image's **segmentations are listed under it** (View → *▦ Segmentations in the image list* switches it off):
colour, name, number of labels and 👁. Click one to make it the active segmentation; **double-click** it (or
right-click → **✏ Rename**) to rename it in place: the name is selected, type the new one, **Enter** keeps it, **Esc**
cancels. Right-click also exports it, shows it on the other images, its statistics, adds the image to the export
basket or deletes it.

**Give a segmentation to another image** (and so to that image's study):
* right-click it → **➡ Attach to another image…** (moved) or **⧉ Copy to another image…** (kept here too); the
  images are listed by study;
* or **drag it** onto the other image's card (the card is outlined: *drop: attach here*). A window says what will
  happen (which image it leaves and joins, whether it is resampled because the grids differ) with **Move**,
  **Copy** and **Cancel**, so an accidental drag changes nothing.

It is resampled onto the new image through world coordinates (nearest label). Script:
`relink seg=<image>:<k>|to=<image>[|copy]`.

**Move an image to another study:** drag its card onto that study (its bar or its images; outlined, *drop: move
to this study*), or onto *No study*. A window names both studies and the number of segmentations that go with it
(they belong to the image), with **Move** / **Cancel**. The image takes the study date, description and UID (in
ORCA-MI; the files on disk change only when you save or export). Script: `relink image=<image>|study=<image of
that study>|none`.

Info tab → Nickname: **✏ Name all images of this study** / **✏ Name all loaded images** give every image its nickname from its header (the modality / date / scanner parts ticked there).

Right-click a study bar → **✏ Rename study** changes the study's name (description) for all its images; they stay in it. Right-click a study bar → **❌ Close this study** (then *Yes, close N images*) closes all its images at once.

**Showing the segmentations of one study.** Right-click a study bar → **🙈 Hide other studies' segmentations**: the
segmentations of every other study are hidden, those of this study stay as they are. The same button is on the
right-click menu of a segmentation in the image list (it keeps that image's study), together with **🙈 Show only this
segmentation** (every other segmentation hidden) and **👁 Show all segmentations**. In the Segment tab, **🙈 Hide all
segmentations** (above the list of segmentations) hides every segmentation of every image, and **👁 Show all** brings
them back; one segmentation is shown again with its own 👁. Script: `segshow all|none|otherstudies <image>|only
<image>:<seg>`.

The image list on the left groups the images by **study** (DICOM Study Instance UID), as RadiAnt does: each study
has a bar with its **date** and description (*📅 2024-06-12 · PET/CT follow-up*), the patient and the number of
images below it; click the bar to fold the study. The studies are in date order, oldest first; images without a
study (NIfTI, NRRD, …) are in *📁 No study* at the end. The patient name is hidden during blinded reading.

**A study for NIfTI and other files:**
* when loading (the *How should this image be used?* dialog) → **Study**: *as in the file* (none), one of the
  loaded studies (by date and description), or **➕ a new study** with its date (YYYY-MM-DD) and a description;
  every file of one load goes into the same new study;
* later: right-click an image → **📅 Study…**, right-click a study bar → *📅 Study of these images…*, or drag the
  image onto a study (with a confirmation).

Put into a loaded study, the image takes its study date, time, description and UID, and its patient (when the file
had none). DICOM export then writes it into that study.

Script: `study` (lists the studies: `[study] date=…|desc=…|uid=…|images=0,2`), `study <i>|of=<j>` (image i into
the study of image j), `study <i>|new=2024-07-01|desc=Dosimetry`, `study <i>|none`.

### ▦ Segmentations on every image (as in 3D Slicer)

**3D Slicer segmentations (.seg.nrrd):** segments that overlap are saved by Slicer in several layers; ORCA-MI merges the layers into one label map, each segment with its own value and name (an overlap goes to the later segment; the count is in the image's Info as *Slicer layers merged*).

A segmentation is created on a **reference image** (its voxel grid), but it is **shown and edited on every
loaded image** that covers the same place: CT, PET, MR, a resampled copy … Each voxel of a view is mapped through
world coordinates and the reference image's registration (the same mapping as fusion overlays).

* **Segment tab → Segmentations** lists every segmentation of every image (*on CT …*, *on PET …*). The selected one
  (●) is the **active segmentation**: the brush, eraser, polygon, region growing, threshold, morphology,
  nnInteractive and the 3D tools change it, whichever image's view you work on. **➕ New on [image]** creates one
  on the image you choose.
* **⇄** shows a segmentation on the other images too (on by default); 👁 hides it everywhere.
* Region growing and threshold use the values of the segmentation's reference image. Region growing: **Shift+R**
  (R alone resets the views), click a seed; *grow ±* is the tolerance around the seed's value.
* **Morphology & cleanup** has its own **Segmentation** and **Label** choice (any loaded image's segmentation; the
  active label, one label, or *every label*): erode / dilate / open / close, fill holes, keep largest, remove small,
  split components and slice interpolation work on that choice (one undo step). A warning shows when the label is
  not in the segmentation.
  **👆 Keep the object I click** / **👆 Remove the object I click**: press one, then click an object on any 2D or 3D
  view (an object = connected voxels of one label). *Keep* keeps it and removes the other objects of its label (with
  *every label* chosen: every other object of the segmentation), then switches off. *Remove* deletes each object you
  click until you press the button again or Esc. A banner on the views says what the next click does; each click is
  one undo step (Ctrl+Z). Script: `objpick keep|remove|off [x,y,z]` (with a voxel of the active image: applied at once).
* **Statistics** measure the active segmentation on any image (*Values from*), e.g. lesions drawn on the CT measured
  on the PET, without copying or transferring them. Tested: identical to SimpleITK resampling (421.3 vs 421.3 HU).
* Drawing order: other images' segmentations below, the image's own above, the active segmentation on top.

**Showing / hiding labels is instant:** the 2D views change at once; the 3D view is rebuilt in the background and
keeps the previous picture for the moment it takes (it used to freeze the window on large images).

**Per-view visibility.** Each label has **A S C 3D** buttons (next to 👁 and 🔒): show it in axial, sagittal,
coronal and/or 3D views, e.g. a body contour in 2D but not in 3D. *Show in: A S C 3D* above the labels switches
all labels at once.

**⋯ next to a label:** *Clear the voxels of this label* (the label stays, empty) or *Delete the label* (its voxels are
cleared and it leaves the list; the next label becomes the active one). Both can be undone with Ctrl+Z.

Script / Python: `segtarget <image index>[|seg=k]`, `labelview <label>|a=1|s=1|c=1|3d=0`, `newseg` (makes the new
segmentation active).

### 🎯 nnInteractive: progress and inference region

**SPECT preprocessing** (AI tab, nnU-Net and image-to-image models; ticked by itself when the model's name contains "SPECT", e.g. LowCountSPECT-Bone / -DatScan): the input is divided by the 99th percentile of its non-zero voxels (0 … p99 → 0 … 1, not clipped), as in training; an image-to-image result is multiplied back to the input's units. **CT localizer** models (name with localizer / topogram / scout): the input is always clipped to −100 … 200.

**Layout MPR no 3D** (Layout menu, script `layout mprno3d`): axial top-left, sagittal bottom-left and a large coronal view on the right, without the 3D view (lighter on laptops).

**Start:** Segment tab → nnInteractive → ▶ *Start* (or pick a 🎯 tool in the toolbar). Then click (point), drag a
box, scribble or lasso on the object. Left = include, Ctrl + left = exclude, Enter = next object.

**🧊 Point clicks on the 3D MIP (PET / SPECT)** (option in the nnInteractive section, off by default): with the
**Point** tool, a click (without dragging) on a 3D view showing the **MIP** of a PET or SPECT image adds a point at the
**brightest voxel along that line**, i.e. the voxel the MIP pixel shows, found on the full-resolution image (and
refined to the local maximum). Ctrl+click excludes. The crosshair jumps to that voxel, so you can check on the 2D views
that the click took the lesion and not a hotter organ behind it (bladder, brain, kidney): rotate the 3D view if
something hotter hides it. A hint at the bottom of the 3D view shows when the option is active. Dragging still rotates;
the 2D views, boxes, scribbles and lassos work as before; other 3D modes (volume rendering, iso-surface) and CT are not
used. Script: `nnmip on|off`.

**Speed** (nnInteractive section, before the start and while it runs; hover a button for its description; changing
it does not restart nnInteractive):
* **🎯 Accurate** (default, as before): when the object reaches the edge of the block nnInteractive looks at, it zooms
  out (up to 4×), predicts again and refines the result at full resolution. Best for large organs; the slowest.
* **⚡ Fast**: no automatic zoom-out, and at most 2× zoom-out for a large box: one prediction around the prompt,
  then refined. Faster for large objects; a large organ given by a point, or a box wider than twice the block, can
  be cut at the block's edge: add a box or more clicks.
* **🐇 Ultra fast**: one network pass, no zoom-out and no refinement, the result is limited to one block around the
  prompt. The fastest, good on the CPU and for small lesions; **not accurate** for large objects (an orange warning
  is shown when it is chosen).

nnInteractive has no tile step like nnU-Net (it predicts a block around each prompt, not a sliding window over the
image); a small *Inference region* (below) also makes each prompt faster. Script: `nnispeed accurate|fast|ultrafast`
(prints `[nnispeed] …`).

**Several objects (e.g. lesions) with the same label:** nnInteractive takes every prompt of a session as one object,
so a second box used to replace the first object. Now **each new box = a new object** (on by default): a new
including box keeps what is already segmented and starts a new object with the **same label** (draw it after the
previous prediction is shown). Points, scribbles and lassos still refine the current object; Ctrl + box excludes.
**✔ Next object keeps the label** (tick): Next object / Enter starts a new object with the same label instead of the
next label. Boxes are 2D (drawn on one slice). Script: `nnobjects boxnew=0|1|samelabel=0|1`.

**Model:** the official model is downloaded once (~400 MB) to `%USERPROFILE%\.nninteractive\models\nnInteractive_v1.0`
and used from there afterwards, also offline. The folder in use is shown under the nnInteractive section (📂 opens it).

**GPU memory:** on *cuda*, ORCA-MI first checks the free memory of the graphics card. With less than about 6 GB free
(e.g. while an AI training runs) it does not start and offers *Start on the CPU*, *Start on the GPU anyway* or
*Cancel*: loading the model on a full card can make the graphics fail. If that still happens, ORCA-MI stops
nnInteractive, starts again by itself and offers to restore the session (autosaved just before nnInteractive
started).

**Segment on:** the image nnInteractive looks at: *the image I click on* (default) or a chosen image. You can
click on the views of any image (e.g. click on the CT while nnInteractive segments the PET); the result goes into the
active segmentation, mapped into its grid when that is another image (tested: identical to SimpleITK nearest
resampling).

**You always see when it is working.** A banner on one view (the active one) shows *Loading nnInteractive…* while the model
loads, then *nnInteractive segmenting…* with a spinner, the elapsed time, the time left and a progress bar, and
the view's frame pulses. The time left is learned from the previous predictions on this computer.

**What it may overwrite:** *May overwrite* (Segment tab, next to the labels, and in the nnInteractive section)
decides which existing labels the brush, fill, threshold and nnInteractive may paint over: **all labels**,
**none** (only empty voxels), or **chosen labels** (tick any), or *only inside a label*. Locked labels (🔒) are
never changed.

**🛡 May overwrite (nnInteractive)** (nnInteractive section): nnInteractive's own setting. **same as the Segment tab's
May overwrite** (default, the shared setting above), **all labels**, **none — only empty voxels of this
segmentation** (lesions or organs already segmented are kept; the new object only fills voxels without a label), or
**only these labels** (tick them; empty voxels too). Locked labels are never changed. It applies to the next
prediction. Script: `nnoverwrite shared|all|none|only=2,3` (prints `[nnoverwrite]`).

**🔗 Combine all labels into [label] ▶ Combine** (Labels section): every label of the active segmentation becomes the
chosen label (e.g. all lesions segmented so far as one label), the other label entries are removed, locked labels
stay as they are, and **↶ Undo** reverts it. An nnInteractive object in progress is kept first; if its label was
combined away, the next nnInteractive object gets a new label. Typical use: segment a lesion with nnInteractive,
combine, set nnInteractive's May overwrite to *none*, and segment the next lesion without touching the first ones.
Script: `combinelabels [label]` (default the active label; prints `[combinelabels] target= changed= removed=`).

**Inference region** (Segment tab → nnInteractive → *Inference region*): what nnInteractive gets to see.

| Choice | What happens | When to use |
|---|---|---|
| **Box around the first prompt** (default, size in mm) | only a box around your first click / box / scribble is sent; the next prompts of the same object use the same box | most work; faster, especially without a GPU |
| **Region I draw** | press *⬚ Draw region* and drag a box on a 2D view (it reaches *depth* mm across the slice; draw again on another view to set the other directions). **The object is kept inside this box.** | to stop the object leaking into neighbours, or to work on one part of a large scan |
| **Whole image** | the full image is sent | very large objects |

* The region is shown as a dashed box on the 2D views (cyan = region in use, orange = drawn region).
* A region is never smaller than the network's input (192 voxels per side, or the whole image along a short
  axis), and it is normalised with the intensity statistics of the whole image, so a click gives the same result
  as on the whole image. (Tested: identical object, Dice 1.000, on a 512×512×78 CT.)
* **Grows by itself:** a prompt outside the box, or an object that reaches an inner edge of the box, enlarges the
  box and the object's prompts are replayed (*Grow the region…*, on by default).
* Speed on that CT: GPU 0.41 → 0.28 s per click; CPU 28 → 19 s per click. Larger scans (whole-body CT/PET)
  gain more.

Script / Python: `nnregion whole`, `nnregion auto 160`, `nnregion x0,y0,z0,x1,y1,z1` (voxels), `nnregion grow=0`;
`nnwait` waits until every prompt is answered and prints the region, voxels and timing.

### Live threshold

Segment tab → **Threshold → label**: with *Live* ticked (default), the active label is shown as you drag the
*lower* / *upper* sliders or type values (or press a preset such as *SUV ≥ 2.5*); the voxel count and volume are
shown. **✔ Keep** accepts it, **✖ Cancel** puts the segmentation back exactly as before (Ctrl+Z also undoes it).
*May overwrite* decides which other labels it may take. Untick *Live* for the classic *Apply* button.
Only moving the threshold changes the mask: choosing or adding another label (➕ *Add label*), another image or
another slice keeps what is there, and the next change of the threshold starts on the new label.

* **Into label / name:** choose the label the threshold goes into (or **➕ new label**) and type its name right there
  (e.g. *SUV ≥ 2.5*, *bone*). Without a segmentation yet, the name is given to the label the first threshold creates.
* **Live in:** *views only (fast)* (default) updates the 2D views while you drag and leaves the 3D view as it was
  until **✔ Keep** (or ✖ Cancel); *views and 3D* rebuilds the 3D view at every change too (slow on large images).
The iterative segmentation updates live too: drag its threshold slider or the volume–threshold curve.

Script / Python: `thrlive 300,3000`, `thrkeep`, `thrcancel`, `overwrite all|none|2,5`.

**Brush size with the mouse:** hold **B** and turn the wheel over a view (selects the brush; Shift while painting still erases), or hold **Alt** and turn the wheel (brush or eraser tool); about 10 % per notch, 0.3 … 128 mm; on a 3D view with the 3D eraser, Alt + wheel changes the eraser's radius.

**Brush / eraser only in a value range** (Segment tab → Manual tools → *Only where the values are in range*): up to four images, each with its own lower and upper value; the brush and the eraser change only voxels where every image is within its range (images on other grids are resampled), e.g. CT −100 … 300 HU and PET ≥ 2.5.

**Threshold → label inside / outside segments:** *Limit inside / outside* with one or more segmentations (each with one label or every label; the region is their union): only voxels inside (or outside) them are thresholded.

### Double threshold (two images, AND / OR)

Segment tab → **Double threshold (two images, AND / OR)**: a label made from two images at once, each with its own
range, e.g. *PET SUV ≥ 2.5* **AND** *CT 0–200 HU* (uptake in soft tissue only, not in bone).

* **Image A** and **Image B**, each with **from** / **to** (both included). They start at the image's window;
  *use window* and *full range* set them again.
* **Combine:** **AND** = inside both ranges, **OR** = inside at least one.
* **Limit:** keep the result only **inside** or **outside** a segment chosen from the list: any segmentation of any
  image (one label or every label), e.g. the *body* contour or the bones; it is placed on A's grid.
* **Into label:** the result is always **one** label of **image A's** active segmentation: choose an existing label
  or *➕ new label*, and type its **name** (empty: a name from the images, ranges and limit). Applying again
  replaces that label's voxels, so it always equals the last result. A segmentation that is created for the result
  uses its first label (no extra empty label).
* **current slice only:** only the slice shown in the active view.
* *May overwrite* applies and Ctrl+Z undoes it. Image B is placed on A's grid with the registration (linear
  interpolation); outside B counts as 0. A and B may also be the same image, e.g. for two ranges of one image with OR.

Script / Python: `dualthr a=0|b=1|alo=2.5|ahi=100|blo=0|bhi=200|op=and|name=PET soft tissue|label=<value>|limit=<image>:<segmentation>:<label>|limitmode=inside`
(without `label=` a new label; label 0 in `limit` = every label; prints `[dualthr] voxels= volume_ml= label= labels=`).

### 🧍 Body contour

Segment tab → **Body contour → 🧍 Create body contour**: the patient's outline on a CT, by Yazdan Salimi's
`yazdan.image.body_segment`:
1. threshold −300 … 2000 HU (the upper limit drops metal),
2. closing (1 voxel),
3. holes filled in every axial slice (lungs, bowel gas),
4. objects up to 10 mL removed and the largest object kept (the table and the cables go).

**Image:** the section's *Image* list chooses the image the contour is computed on (CTs are marked *(CT)*), so it is
clear with several images loaded (e.g. PET + CT); *the active image* (default) follows the image you select. The
contour is added to that image's segmentations. Script: `body …|image=<index>`.

The result is a new segmentation *Body contour* (label *body*), or, with *Add as label 'body'*, a label in the
active segmentation (following *May overwrite*). All values are adjustable under *Settings*.

**Engine:** *built-in* (default) is a port of `body_segment` to Rust that gives exactly the same voxels as the
Python function (0 differing voxels on three CTs) in under a second; *yazdan package* runs the function itself in a
Python that can `import yazdan` (30–60 s, mostly Python start-up and the slice-by-slice loop).

Script / Python: `body -300,2000|min=10|close=1|largest=1|engine=builtin|label=0`; `v.body_contour()`.

### Measurements: volume, SUVmean, SUVmax, SUVpeak, TLG

Segment tab → **📊 Statistics in segments**:
* **Values from:** measure on any loaded image, e.g. a lesion mask drawn on the CT measured on the **PET**.
  The PET is resampled through world coordinates and any registration.
* **Each connected lesion separately**, or per label.
* **Columns** (named the SUV way for SUV images): MTV (mL), SUVmean, SUVmax, **SUVpeak**, and **TLG** = SUVmean × MTV, plus std, min and median.
  SUVpeak is the highest mean in a 1 cm³ sphere placed anywhere in the lesion (PERCIST style).
* **Totals and export:** total MTV and TLG are shown under the table; *Export CSV* saves everything.
* Python: `v.stats(value_image=1, split=True)` returns dicts with `volume_ml, mean, max, peak, tlg, ...`.

### 📈 Iterative segmentation (XEOS method)

**Multi threshold:** the double threshold takes up to five images (➕ image: C, D, E), all combined with the same AND / OR, and its limit takes several segments (their union), inside or outside.

Segment tab → **Iterative segmentation (PET lesions)**. This is a port of Yazdan Salimi's XEOS iterative segmentation (3D Slicer); it gives identical results on a reference test.

For every region:
1. The lower threshold is raised step by step from the region's minimum.
2. The segmented volume is followed until it stops changing: the volume change stays below the plateau % for the chosen number of post-plateau steps.
3. That threshold is taken. If the volume drops below the minimum volume first, the previous step is taken.

* **Values:** the PET. Bq/mL images are used in kBq/mL, as in the original. The initial segmentation can be on the PET or on the CT (resampled to the PET grid).
* **Region per:**
  * **connected lesion**: every pre-segmented lesion;
  * **label / segment**;
  * **box around each lesion** with a margin in mm: a rough box is enough.
* **Initial lesions** if you have none: *Otsu on the PET* (small objects removed, dilated, one label per object), and *% of lesion max* (e.g. 41 % and 30 % of each lesion's maximum).
* **Parameters** (defaults as in XEOS): plateau 2 %, 10 post-plateau iterations, 500 maximum iterations, step 0.1 (or automatic), minimum volume, keep the largest object, only inside the initial region, 5 mm crop margin.
* **Results:**
  * a segmentation named *Iterative segmentation* on the PET;
  * for each lesion, the **volume–threshold curve** (plateau points in green, current threshold in orange);
  * click or drag on the curve, or use the slider, to change a lesion's threshold live; *↺ auto* returns to the plateau value;
  * a table of all lesions;
  * *Export CSV* writes the lesion table plus every iteration.
* Python: `v.iterative_segmentation(value_image=1, seg_image=0, mode="lesions"|"labels"|"boxes", box_margin_mm=10, plateau_pct=2, post_plateau=10, step=0.1)` and `v.iterative_threshold(lesion, threshold or "auto")`.

### ✂ Crop

Toolbar ✂, File → *Crop images*, or the Image tab.

**To segments + margin:**
* Tick any labels, e.g. *lung left*, *lung right* and *liver*.
* Set a margin in mm for each direction: R, L, A, P, I, S.
* Choose which directions are cropped at all. Untick L–R and A–P to crop only head–feet.

**Manual box:** a voxel range per axis. The first box is placed around the body by a quick threshold (as the 3D view
removes the table: CT above −500 HU, other images above 5 % of the 99.5th percentile) and is always a little inside
the image edges, so it is easy to see and grab. **🧍 Fit to the body** places it there again, **⬜ Whole image** takes
the full image, and *use the visible area of the active view* takes what the active view shows. Drag the box edges
on the views to adjust it. Scripts: `cropwindow manual`, `cropbox [image]`.

**Options and preview:**
* **Crop all loaded images** (CT, PET, dose …) to the same physical box, so they stay aligned.
* Keep or replace the originals. Segmentations are cropped too.
* The box is previewed as a dashed yellow line on every 2D view while the dialog is open (outside it is darkened).

Python:
* `v.crop_to_segments(["lung", "liver"], margins={"S": 20, "I": 10}, axes="SI")`
* `v.crop_box(x=(…), y=(…), z=(…))`

## 4. Dynamic PET and multi-time-point imaging

### Time-activity curves, Patlak, half-life

Tools → **📈 Dynamic PET / time-activity curves…** (or *Time-activity curves per segment* under the frame slider of
a 4D image).

**1 · Images**
* **One dynamic (4D) image:** a dynamic PET series (DICOM frames or 4D NIfTI). Frame start times and durations
  are read from DICOM (*Frame Reference Time*, *Actual Frame Duration*).
* **Several time points:** separate 3D images, e.g. SPECT/CT at 4 h, 24 h and 72 h after a therapy. Tick them in
  time order. Times are read from the acquisition date/time, in hours after the injection when the injection time
  is in the header, otherwise after the first scan.
* **Reference** frame / time point, and **ROIs = segmentation of** an image (default the reference): its labels
  are the regions. Draw them on the reference image or on the CT acquired with it.

**2 · Registration (optional)** — *Register all to the reference*: rigid registration of every frame (patient
motion during a dynamic scan) or of every time point (different days, different positioning). For frames,
*from frame #* leaves the first, low-count frames alone. The largest shift is shown; *Motion-corrected copy* adds
the corrected 4D image. For time points the registration is stored on each image, so the fused display uses it.

**3 · Times** — edit the start and duration of every frame / time point and the unit (min, h …).

**4 · Time-activity curves** — *Compute curves*: mean, max and total (mean × volume) per label and time, sampled
through the registration in world coordinates (different grids work). Plot with a legend; *Save CSV* / *Copy
table*.

**Patlak** (needs an input-function label, e.g. a VOI in the aorta or left ventricle): Ki, V0 and r² of every other
label from the points after t*; **🗺 Ki map** adds a voxel-wise Patlak Ki image.

**Kinetics** (time points): effective half-life from a mono-exponential fit of the last *n* points, and the
time-integrated activity (TIA): first value held from time 0, trapezoids between the scans, analytic exponential
tail after the last scan, with the tail fraction. Use images in activity concentration (Bq/mL) so *total* is
activity; TIA × S-value or a dose kernel gives the absorbed dose (see the Dose tab for voxel dose maps).

Tested on a synthetic dynamic PET with a known answer: Ki 0.04997 vs 0.05 /min, V0 0.302 vs 0.3, patient motion
of 4.5 mm found and corrected, TACs within 0.1 %.

Python:
```python
r = v.dynamic_tac(frames=0, reference=18, register=True, register_from=12,
                  input_label=1, t_star=10, csv="tac.csv", ki_map=True)
r["patlak"]     # [{'label': 2, 'name': 'tumour', 'ki': 0.04997, 'v0': 0.302, 'r2': 1.0, ...}]
r = v.dynamic_tac(images=[0, 1, 2], times=[4, 24, 72], time_unit="h", register=True, tail_points=2)
r["kinetics"]   # effective half-life and TIA per label
```

### Named registrations: apply them to other images

Every registration result (align centres / centres of mass, rigid / similarity / affine, Demons, or a manual
transform with *💾 Keep as named registration*) is kept under the **name** typed at the top of the Register tab (or
"moving → fixed (kind)").

**Your layout is kept.** After a registration (align centres, rigid, Demons, applying a saved one) the views stay as
you arranged them: a view of the moving image follows the crosshair of the fixed image *through the registration*,
so the two can be compared side by side. Results that are new images (Demons, resampling, *new image*) replace the
image they come from in its views; no hanging protocol re-arranges the screen. Tick **Show results fused on every
view of the fixed image** (Register tab, off by default) to get the moving image fused on the fixed one instead.
Script: `regfuseall 0|1`, `cursorinfo`.

Right-click any image (view or thumbnail) → **🔗 Apply a registration…**: choose the registration and
* **in place**: the image follows the registration without resampling (e.g. the PET acquired with the moving CT is
  then shown aligned on the fixed CT), or
* **new image** resampled onto the fixed grid, with an editable name (default "image (registration name)"),
  optionally with its segmentations. Demons registrations are always applied by resampling.

The *Saved registrations* section of the Register tab lists, renames, applies and deletes them.

**📉 Loss curve** (Register tab) shows the metric of the last registration step by step, one colour per pyramid level
(lower is better: mutual information and NCC are shown negated; Demons: mean squared error). It follows a running
registration live.

**Combine steps into one transform:** tick two or more saved registrations (in the order they were made; **☑ Select
all** ticks every one) and press **⧉ Combine the ticked into one**. The result is a new saved registration (e.g. *moving → fixed (centres + rigid +
affine)*) that you apply in one go to a new image.
* Steps of the same pair build on each other: rigid starts where centring ended, affine where rigid ended, so each
  step is counted once (the latest step alone already contains the earlier ones; the combined entry makes it
  explicit). A step started from scratch (e.g. after resetting the transform) is added on top.
* Steps can also be chained across images: *CT1 → CT2* then *CT2 → MR* gives *CT1 → MR* (the moving image of
  each step must be the previous step's fixed image).
* A deformable (Demons) step can only be the last one.

Script: `regname <name>`, `reglist`, `regapply image=2|tf=0|new=1|name=…`, `regcombine 0,1,2|name=…`.

**Fusion:** the ✖ next to the fusion slider of a view, right-click → *Remove the fusion from every view*, the
thumbnail menu *Remove all fusions* and the Image tab *Remove all fusions* take fused overlays off all views at once
(script `removefusion`).

### Interactive registration: live preview, mouse, segments, landmarks

Register tab:
* **Manual / interactive → Live preview on the moving image's views** (on): when you type or drag the translation,
  rotation or scale, the views showing the moving image show it **in the fixed space**, as it appears fused, in its
  own colours (*preview: … in the fixed space* on the view), even when *Show moving fused on fixed* is off. They go
  back to the moving image when you leave the Register tab, untick the option or press *end preview*.
The manual section offers **two methods** (both change the same transform; **↶ Undo move** steps back through the
last mouse moves and button steps):

* **Method 2 · 🎮 Arrow buttons** — light on any computer: pick the **plane** (Axial, Coronal, Sagittal) and the
  **step** (mm), then press the cross: ▲ ▼ ◀ ▶ move the moving image on that plane, labelled with the patient
  direction it moves to (axial: ▲ A, ▼ P, ◀ R, ▶ L; coronal: ▲ S, ▼ I, ◀ R, ▶ L; sagittal: ▲ S, ▼ I, ◀ A, ▶ P), and
  ⊙ / ⊗ move it through the plane. **Rotate:** pick the step (°) and press **⟲ −** (anticlockwise) or **⟳ +**
  (clockwise, as seen on the plane's standard view) to turn it in that plane about the crosshair. Script:
  `regturn axial|coronal|sagittal <deg>`, `regundo`, `regnudge dx,dy,dz`.
* **Method 1 · 🖱 Move / rotate the moving image with the mouse** (as in ITK-SNAP; the views are redrawn while you
  drag, which can be slow on a laptop without a strong graphics card): on the fused or preview views a circle with
  four handles is drawn around the crosshair, with a **grid fixed to the moving image** (its own axes, through the
  crosshair; it moves and turns with the image; *grid* untick hides it). Press **inside** the circle and drag to move
  the moving image in the view plane; press **on the circle** (or its handles) and drag to rotate it
  about the crosshair (the axis is the view's normal: use the axial, coronal and sagittal views for the three
  rotations). Outside the circle the usual tool works (a click there no longer turns the image), a few pixels of
  hand movement at the press are ignored, and the drag always ends when the button is released. The drag starts
  where you press (also on the colour bars). The translation / rotation values in the
  table follow while you drag. Wheel, zoom and pan still work. Typically: match the centres by
  hand, then run the automatic registration from there. The mouse works also with *Live preview* off (the views of
  the moving image then show it in the fixed space). A new transform turns about the centre of the fixed image (the
  mapping is unchanged, only the numbers), so a small rotation no longer comes with a large translation.
* **Size of the moving image (all axes)**: a scroll bar under the Scale values, 50–200 %, scales the moving image
  about the rotation centre (scale = 100 / size on x, y and z); *100 %* puts it back. The per-axis Scale values stay
  for anisotropic changes.
* **▦ Dual MPR**: the fixed image in the left MPR, the moving image in the right one (crosshairs linked). While you
  move / rotate it (mouse or values) the right MPR shows the moving image in the fixed space, with the circle of the
  mouse tool; while you pick points it shows the moving image itself.
* **Centering → On segments:** choose a segment on the fixed image and on the moving image (e.g. the liver on both,
  or the bladder) and press **◎ Align the centres of these segments**. The same choices then constrain the automatic
  registration (see below).
* **Centering → On anatomical points (1 to 10 pairs):** press **📍 Pick points**, click a landmark on a view of the
  fixed image, then the same landmark on a view of the moving image (side by side, e.g. ▦ Dual MPR); the next pair
  follows. The points are marked with their number (blue on the fixed image, pink on the moving one). **⌖ Align on n
  point pair(s)**: 1 pair = translation; 2 or more with *rotate too* = rigid least-squares fit. Three or more pairs,
  spread out, give the best accuracy. **Refine the points by image matching** (on by default): before the fit, each
  moving point is moved (up to 8 mm) to where a 2 cm cube around it best matches the fixed image (normalised
  cross-correlation), then the fit is redone; best for the same modality, a point keeps its click when nothing
  matches. The distance left is shown per pair and as RMS (test: clicks 2 mm off → 0.96 mm RMS without, 0.18 mm
  with refinement). Each result is a saved registration (*point(s)*, *centres of segments*). The layout and the fusion stay
  as they are (unless *Show results fused on every view of the fixed image* is ticked): side by side, the crosshair
  of the moving view follows the fixed one through the new registration, so both show the same landmark; show or
  hide the fusion yourself.

Script: `regpreview 0|1`, `regmouse 0|1`, `regnudge dx,dy,dz` / `regnudge rot=z,5` (what the mouse does),
`regpoint fixed|moving x,y,z [pair 1-10]`, `regpoints [rotate=0|1][|refine=0|1]`, `regdualmpr`, `regcentermask <img>:<seg>:<label>|<img>:<seg>:<label>`.

### Registration constraints: masks and a focus sphere

**Focus area: sphere or box** (*in an area around the crosshair*): *sphere* (radius in mm) or *box* (x, y, z in mm, ⌖ *Around the crosshair*; its orange edges are dragged on the fixed image's views, as in Crop). Only that area is compared; nothing is cropped. The centre is the crosshair of a view of the fixed image; an area with (almost) nothing of the fixed image in it falls back to the whole image, and a registration that fails keeps its start transform (an undefined result is never applied or combined, which could give an all-zero image).

Register tab → *Automatic rigid / affine* → **Constraints**: the similarity (MI, NCC or MSE) is computed only
* inside a segmentation of the **fixed** image (any labels, of any segmentation mapped onto it),
* where the transformed point falls inside a segmentation of the **moving** image,
* inside a **sphere around the crosshair** (radius in mm; the circle is shown on the views while the Register tab is
  open) to emphasise one region, as in Hermes.

Useful when organs move differently (e.g. register on the liver only, or on a lesion). Tested on two objects moving
in opposite directions: each constraint makes the registration follow the object it selects.

## 5. Dosimetry

### Dosimetry (☢ Dose tab)

* **⏱ Single time point dosimetry (Hänscheid / Madsen)** — Lu-177 PSMA / DOTATATE and other therapies, from one
  quantitative SPECT (or PET), local energy deposition:
  * choose the image (the injection and scan time, unit, radionuclide and decay correction are read from the DICOM
    fields when present; *⟳ header* reads them again), the radionuclide (physical half-life and mean electron energy
    per decay: Lu-177 159.5 h / 0.1479 MeV, Y-90, I-131 or your own values), the injection and scan start time, the
    scan duration (the reference time is the middle of the scan), the factor to Bq/mL (Bq/mL, kBq/mL, MBq/mL buttons;
    convert counts first with Q.SPECT), whether the values are the activity **at the scan** or **decay corrected to
    the injection** (then undone with the physical half-life) and the tissue density (1.0 g/mL);
  * **Hänscheid**: TIA = A(t) · 2t / ln 2 for every voxel (the effective half-life is taken equal to t), dose = TIA ·
    E / mass. **☢ Compute STP dose** adds the **dose map (Gy)**, which becomes the dose image of this tab (DVH,
    constraints, isodoses, lesion dose with spill-out correction), and the **TIA map (MBq·h/mL)**;
  * the tab shows the range of effective half-lives for which Hänscheid at this scan time stays within ±10 %
    (estimate / true = 2x / 2^x, x = t / T: exact at T = t and T = t/2, at most +6 %; e.g. 96 h → 39–126 h) and warns
    for scans before 24 h;
  * **per segment** (tick the segmentations; every label is a row): volume, activity at the scan, Hänscheid mean dose
    and max voxel dose; type the **population effective half-life** of the organ / lesion (h) for **Madsen**: TIA =
    A(t) · e^{λt} / λ, λ = ln 2 / T, shown next to Hänscheid (Madsen / Hänscheid ratio). A T above the physical
    half-life is flagged; when Hänscheid is off by more than 10 % for the T typed, the row says so. No population
    values are built in: use those of your radiopharmaceutical / centre.
  * CSV / copy of the table. Estimates for research (single time point: typically 10–30 % for organs, more for lesions).
  References: Hänscheid H et al., J Nucl Med 2018;59:75–81 (TIA ≈ A(t)·2t/ln 2; single SPECT/CT at ≥ 96 h for
  Lu-177 DOTATATE / DOTATOC, larger errors at 24–48 h); Madsen MT et al., Med Phys 2018;45:2318–2324 (TIA =
  A(t)·e^{kt}/k with the population clearance rate k = ln 2 / T_eff; least sensitive to the patient's own T_eff when
  the scan is near the mean life 1.443 · T_eff).
  Script: `stp img=<i>|hours=<h>|nuclide=Lu-177|factor=1|decaycorr=0|density=1|energy=<MeV>|halflife=<h>|duration=<min>|segs=<img>:<seg>;…|teff=<segment / label>=<h>;…`.
* **Dose image:** RTDOSE (auto-detected) or any absorbed-dose map, e.g. from voxel dosimetry. Use *× scale to Gy*
  for cGy or mGy. Set the prescription / reference dose (or use = Dmax).
* **DVH (dose–volume histogram)**, one section: first the **structures** (the organs / lesions the DVH is
  computed for): any segmentation or RTSTRUCT on any image (for example the CT), ticked ones included. The dose is
  sampled at every structure voxel through world coordinates, so different grids and registered doses work. Then
  ▶ Compute DVH: cumulative or differential, % or cc, click legend entries to hide curves, hover for read-outs, and a
  resizable large plot. Metrics: volume, Dmin, Dmean, Dmax, D98%, D95%, D50%, D2%, D2cc.
* **DVH constraints:** rows of *structure* (part of a label name, e.g. `kidney` matches `kidney_left` and
  `kidney_right`) plus an *expression*: `Dmax < 45`, `Dmean < 23`, `Dmin > 50`, `D95% > 95%Rx`, `D2cc < 60`,
  `V20Gy < 30%`, `V5Gy < 100cc`. Templates are provided for radionuclide therapy (PRRT/RLT), Y-90 SIRT and EBRT
  (QUANTEC examples), and you can save / load your own. Results show PASS / FAIL.
* **Isodose lines:** absolute (Gy) or percent of the prescription or the maximum dose, drawn on every 2D view
  with a legend. **Dose image of the lines**: any image (*the dose image above* by default), with its own *× scale to
  Gy* when it is not the dose image; the percent reference (maximum) is that image's maximum. *Show dose as colour wash* fuses the dose (jet) on the structure image; **✖ Remove colour wash**
  puts the dose image's colormap and window and the views back as they were.
* **Image in Gy:** *➕ new image* adds the dose × the scale as an image in Gy (for statistics, profiles, comparisons);
  *✎ overwrite* scales the dose image itself (the scale becomes 1).
* **Export:** one CSV with DVH metrics, constraint results and the cumulative DVH curves. Every section has its
  own **💾 CSV…** (single time point, SIRT, DVH, constraints, lesion dose, isodose levels). At the top of the tab,
  **📊 Export all (Excel)…** writes one workbook with a sheet per section that has results (Summary, Single time
  point, SIRT, DVH metrics, DVH constraints, Cumulative DVH, Lesion dose, Isodose levels), **📄 Export all (CSV)…**
  the same in one CSV (sections one after the other). Script: `doseexport <file.xlsx | file.csv>`,
  `isoimage <image index | dose>|scale=<factor to Gy>`.
* **🎯 Lesion / organ dose (spill-out correction)** — NM / SPECT / PET / theranostics: choose the **NM / dose image**
  (any image: SPECT, PET, a dose map; *the dose image above* by default — its values × the scale in Gy, any other image
  in its own unit), the lesion or organ (any segmentation and label), set the dilation in mm (−1 mm / +1 mm), press
  **🧮 Calculate lesion dose**. Two values:
  1. the **mean** of the image in the original segmentation (and its max);
  2. the **spill-out corrected** value = sum of every voxel of the dilated region (the segmentation grown by the
     dilation) ÷ number of voxels of the **original** segmentation: the counts spilled out of the lesion by the
     partial volume effect are added back, the volume stays the original one.
  For an image in Bq/mL (kBq/mL …) the total activity in the original and in the dilated region is shown too.
  **Outline on the views** (on): while the tab is open, the segmentation (yellow) and the border of the dilated
  region (thick cyan, with *dilated +n mm*) are drawn on every 2D view and follow the dilation at once;
  **blinking** makes the border pulse (only the outline is redrawn: fine on small laptops). *Add the region as a
  segmentation* adds *Spill-out region* (1 original, 2 dilated) on the measured image when you calculate.
  Script: `lesiondose img=<i>|dose=<i>|seg=<i>:<seg>:<label>|mm=3|scale=1|show=1|outline=1|blink=0`.
* NIfTI label names embedded by TotalSegmentator, and the `.labels.json` sidecar written by ORCA-MI, are read
  automatically.

Python: `v.dvh(dose=1, structures=(0, 0), rx=23)`, `v.constraints(preset="rlt", add=["kidney: V23Gy < 10%"])`,
`v.isodose([30, 50, 80, 100], percent=True)`.

### DVH metrics

Dose tab → *Metrics*: any comma-separated list, e.g. `D95%, D2cc, D10ml, V20Gy, V5Gy cc, Dmean`.
`Dx%` = minimum dose to the hottest x % of the volume, `Dxcc` / `Dxml` = to the hottest x cc,
`VxGy` = % of the volume receiving ≥ x Gy, `VxGy cc` = cc receiving ≥ x Gy. The metrics are shown in the table and
exported to the CSV. Python: `v.dvh(metrics="V20Gy, D20%, D10ml")` (keys `V20Gy`, `D20%`, `D10cc`).

### ⚛ Dose point kernel (coming soon)

Dose tab → **Dose point kernel (DPK)** announces the next method: a dose kernel of the radionuclide moved over the
time-integrated activity map (each voxel gets the sum of the kernel contributions of all source voxels), the deposited
energy divided by each voxel's mass from a density map (CT, HU → g/cm³). It is not computed yet.

### 🧪 SIRT Y-90 dose: local deposition method (LDM)

Dose tab → **SIRT Y-90 local deposition** (as `yazdan.RT.sirt_dose_calc`). Choose the post-therapy SPECT (or PET), the
whole-liver segmentation and label, the body contour (or the whole image), the injected activity, the lung shunt
fraction and the residual activity. Two dose maps (Gy) are added:

* **liver calibrated:** A · (1 − LSF − residual) distributed over the counts in the liver;
* **body calibrated:** A · (1 − residual) distributed over the counts in the body contour (the lungs must be in the
  field of view).

Dose per voxel = activity × T½/ln 2 × 0.9267 MeV / voxel mass (liver density 1.05 g/cm³), T½ = 64.1 h. The table
gives the mean, median, min, max and percentiles in the liver, the body and every label of the chosen segmentations,
for both calibrations; CSV export. The dose maps work with the DVH and isodose tools above. Optional dilation of the
liver (and body) mask, negative SPECT values set to 0.

Note: ORCA-MI maps the masks onto the SPECT grid with nearest neighbour. `yazdan.image.segment_stat(force_match=True)`
resamples them with linear interpolation and casts to integers, which drops about 2 % of the mask voxels even on the
same grid, so the Python doses differ by 1–2 %. With the same masks the results are identical.
Script: `sirt spect=0|liver=1:0:1|body=1:1:1|activity=2800|lsf=5|residual=2|regions=1:2`.

## 5b. CT dose, patient size and density

Right panel → **🩻 CT dose** (for a CT; load it from DICOM for the exposure data).

**Exposure (DICOM headers), per slice:** kVp, pitch, tube current (mA), exposure time, mAs (*Exposure*, else
mA × time), rotation time and **CTDIvol**. The CTDIvol curve is
* *per slice from the DICOM headers* when the scanner writes one per slice (e.g. Philips), or
* *estimated per slice* = series CTDIvol × slice tube current / mean tube current, when only one CTDIvol is written
  and the tube current is modulated (the tab says so), or
* missing when the headers have no CTDIvol (e.g. many Siemens series): the tab says *CTDIvol not in the DICOM header*
  and offers **manual CTDIvol (mGy)**: type the CTDIvol of the scan (dose report). It belongs to the mean tube
  current of the scan, so each slice gets CTDIvol × its tube current / mean tube current (*calculated*, marked in
  orange), as CTDIvol is linear in the tube current.

**Table height** (DICOM 0018,1130) is shown with the exposure values (and as a curve): the patient's AP position.

**Patient size per slice** — *📏 Compute size per slice*: Yazdan Salimi's
`yazdan.personalized_ct.DW_centerpoint_from_CT`: water-equivalent diameter (DW), mean HU, body area, AP and lateral
diameter, equivalent and AAPM effective diameter, and the body centre (AP / lateral, RAS voxel as the Python
function, and as offset in mm). It uses the body contour (a label named *body*, e.g. from Segment → Body contour);
**without one, the body contour is computed on this image and a warning says so.** The built-in version gives the
same numbers as the Python function (tested on every slice); tick *with the yazdan package* to run the Python
function itself. **SSDE** = CTDIvol × AAPM conversion factor for DW (32 cm body or 16 cm head phantom).

**Curves:** tick water-equivalent diameter, AAPM effective diameter, centre line lateral, centre line AP, CTDIvol,
SSDE, tube current, mAs, rotation time, table height; for each, tick **coronal** and / or **sagittal** to draw it on
those views; style *line*, *dots* or *line + markers*; x axis in mm or slice number. **Show on the coronal / sagittal
views**: the **lateral centre line** is drawn at its real position on the coronal views, the **AP centre line**
(patient height on the table) on the sagittal views, the other curves as profiles along the slices (while the tab is
open). **Export**: **💾 Results CSV…** / **📊 Results Excel…** = everything the tab calculated: a summary (CT,
CTDIvol source, SSDE phantom; mean / min / std / max / slices of CTDIvol, SSDE, tube current, mAs, table height, kVp,
pitch, exposure time and the patient size), the **regional** statistics between the limits, and the per-slice
values; **💾 Per-slice CSV…** only the per-slice values (with the AP offset and the table height). Script:
`ctexport <file.xlsx | file.csv>`.

**Regional CTDIvol** (right after the patient size, on by default): *Region between two slice positions*, then set the **upper** and **lower** limit (mm) or
drag the dotted lines on the coronal / sagittal views. The tab gives the mean, min, standard deviation and max of the
**regional CTDIvol**, regional SSDE, regional tube current and regional mAs between them (from the headers, or
calculated from the manual CTDIvol, which the tab then says). A value that cannot be computed shows — and why (e.g. *no
CTDIvol: enter it below*, *compute the size first*); *whole scan* takes every slice. Limits left from another CT are
reset to the middle half of the new scan. A CT without exposure headers (e.g. NIfTI) takes the manual CTDIvol on
every slice. Dragging: a press on (or within 12 px of) a dotted line takes it and it follows the mouse until you
release the button (the pointer tool does not take over). **🖱 move the limits with the mouse** (tick): a press
anywhere on a coronal / sagittal view of the CT takes the nearest limit.

**Arms position:** *arms up* / *arms down* for the CT, saved with the scores (the Scores tab offers
*➕ Arms position* as a criterion for reading sessions).

### Density map

CT → density, as `yazdan.personalized_ct`: **clip** the HU range first (default −1000 … 3000 HU), then
* **Classes** (`ct_to_desnity_map`): 12 HU intervals → g/cm³ (editable table, *↺ yazdan defaults*),
* **Bilinear** (`ct_to_density_map_bilinear`): HU > 0 → 0.00069·HU + 1.03107, else 0.00108·HU + 1.02351
  (coefficients editable),
* **μ-map 511 keV** (`ct_to_umap`): kVp-dependent bilinear attenuation (cm⁻¹) for PET attenuation correction
  (kVp from DICOM with one click).

Output in g/cm³ or g/L as a new image. Tested identical to the Python functions.

Script / Python: `ctdose size|engine=builtin|phantom=32|csv=<file>|ctdi=<manual mGy>|region=<upper>,<lower>`, `density classes|bilinear|umap|clip=-1000,3000|unit=g/L|kvp=120`.

### 📦 Batch tab: inputs by pattern, output names and folders

**DICOM RTSTRUCT output** (Batch tab, output extension *.dcm (DICOM RTSTRUCT)*, segmentation models): every DICOM series of the list gets an RTSTRUCT inside its own folder, referring to its original slices (same patient, study and frame of reference), with the label names as structure names. With the patient database: filter by modality (e.g. PT), then Batch → 🏥 From database search, choose the model and Run.

**Inputs → 🔎 Search with a pattern (glob)** finds image files (e.g. NIfTI converted from DICOM) below a folder, like
Python's `glob(os.path.join(source, "*", "**", "*.nii.gz"), recursive=True)`, but in ORCA-MI itself:

* **Source folder** and the **pattern** below it, parts separated by `/` or `\`: `*` = any text inside one name
  (`*RAW*`, `*.nii.gz`), `?` = one character, `**` = any number of folder levels (also none). Upper / lower case are
  not distinguished. Examples: `*/**/*.nii.gz` (at least one folder down), `**/ct.nii.gz` (every level),
  `Patient*/CT/*.nii.gz`. Only files are found (no DICOM folders).
* **Exclude files whose name contains** and **Exclude files in folders whose name contains** (any folder level below
  the source): comma-separated texts, e.g. `seg, mask` and `old, backup`.
* **🔎 Search** (runs in the background, *Stop* to end it) shows how many files were found, in natural order, each
  with a tick box: untick the ones you do not want (*all* / *none*), then **➕ Add N selected to the inputs**.

**Output:**

* **name = prefix + input + suffix** and the extension, e.g. prefix `pre_`, suffix `_seg` → `pre_ct_seg.nii.gz`.
* **in folder** + **keep the folder structure of the inputs**: the inputs' folders below a base folder are made again
  in the output folder (`<base>\Patient01\CT\ct.nii.gz` → `<output>\Patient01\CT\ct_seg.nii.gz`). The base is the
  search's source folder, or the folder typed, else the common folder of the inputs. **levels kept**: *all*, or only
  the first levels below the base (1 = `<output>\Patient01\ct_seg.nii.gz`).
* When several inputs would get the same output file (e.g. every patient has `ct.nii.gz` and all go into one folder),
  a warning says how many, with a button to keep the folder structure; *Run* asks before overwriting.

Script / Python: `batchsearch source=D:\data|pattern=*/**/*.nii.gz|exfile=seg|exfolder=old|add=1` (prints
`[batchsearch] found=` and one `[batchfound]` line per file), `batchout folder=D:\out|prefix=|suffix=_seg|keep=1|levels=1`
(prints `[batchout] duplicates=` and `[batchoutput] input -> output`), `batchclear`.

### 💪 Arms position (batch)

Batch tab → *Task* **💪 Arms position (CT)**: add CT files or DICOM folders and run. No model is needed: the body is
found with HU thresholds (a padding value outside the field of view is ignored), each axial slice is split into the
trunk / head and separate limbs, the trunk is the longest run of large slices, and each arm is judged on its own:
beside the trunk = down, above the trunk (beside or over the head) = up. Result per scan: **ArmsUp**, **ArmsDown**,
**OneArmUp** or **UnKnown** (with a note, e.g. head-only scans where the arms are outside the field of view), the side
results and the lengths measured.

The rule of `yazdan.image.arm_position_detector` on the MOOSE body segmentation `<name>--moose_body--yzdnn.nii.gz`
(1 legs, 2 trunk, 3 head & neck, 4 arms) is computed too (extra columns). **Generate the MOOSE body segmentation
first when a CT has none** (on by default): choose the folder of the MOOSE body nnU-Net model once (e.g.
`…\moose\moose_body`, or an AI-tab model named *moose_body*); it runs on the CTs without one and writes the
segmentation next to each CT. Organ models of the AI tab can be ticked too (outputs
`<name>--<model folder>--yzdnn.nii.gz`). A Python with nnU-Net is needed (AI tab). The rows are appended to `arms_position.csv`
(next to the inputs, in the output folder, or a file you choose); optionally a `<name>--armposition.csv` next to each
input. On 218 CTs the built-in method agreed with visual reading in 217 (the other was a corrupted image); the
MOOSE rule gave the same result as the Python function in 218/218 but disagreed with the images in several cases
(arms visibly up called down, head-only scans called arms up).

Script: `armsfile <path>` (one scan), `arms` (active image), `armsbatch <CT>;<CT>…|csv=<file>|gen=1|moose=<folder>`.

## 5c. Cardiac: short axis, 17 segments, bull's-eye

Right panel → **🫀 Cardiac**. Works on PET, SPECT, CT or MR. The tab has three sections:
* **🫀 Short axis and 17 segments (with an LV segmentation)**: steps 1–5 below.
* **🔄 Short axis from the image only (no segmentation)**: see *Image only* below.
* **▦ Splash view (SA · VLA · HLA)**: see *Splash view* below.

1. **LV segmentation**: choose the segmentation (any image) and the label of the LV myocardium.
2. **Short axis**: tick the images to reorient with the same rotation (PET, CT, a second tracer...).
   For a scan with a different origin (for example FAPI next to FDG), tick **other scan** and choose
   whose origin to use; the shift is the origin difference, as in the Python pipeline.
   * **🎯 Automatic** gives a starting estimate of the long axis (a line through the centres of the
     myocardium rings). Always check it: on the test patient it was about 12° from the expert angles.
   * Fine-tune with **x (tilt)**, **z (axial angle)** and **roll**. x and z are the same angles as the
     `x` / `z` columns of *names + rotations.xlsx*, so existing angles can be typed in. **Roll** turns the heart
     about the long axis: the pink axis does not move, but the short-axis slices turn, and with them which wall
     (septum, anterior, lateral, inferior) falls into which of the 17 segments. The blue (**0° lateral**) and
     yellow (**90° anterior**) spokes at the LV centre on the original views turn with the roll; the short-axis
     images and the bull's-eye follow when you let go of the slider (*live*) or with *Create / update*.
   * The dashed pink line on the views of the LV image shows the long axis (base → apex). Move it with **shift**
     (x, y, z in mm; 0 = through the LV centre).
   * Or with the mouse: switch on **🖱 Correct the axis with the mouse**, then on the views of the LV image drag the
     **base** or **apex end** of the pink axis to rotate it (the x / z angles follow; the tilt out of the view plane is
     kept), anywhere else to move it in the view plane. While it is on, zoom, pan and the crosshair are off on those
     views; switch it off to navigate again. With **live** on, the short axis is updated when you let go.
   * **Create / update short axis** makes "<name> short axis" images, with their segmentations.
     With **live** on, they update when you let go of a slider (and the 17 segments are recomputed).
   * **Show SA · HLA · VLA** puts the short-axis image in a 1×3 layout.
   * **Crop around the heart** (on, margin 30 mm): the short-axis images cover only the heart, so they update much
     faster while you correct the angles and are easier to look at.
   * **Axis shown on**: the image whose views show (and let you drag) the long axis, e.g. the CT while the LV
     segmentation is on the PET; the bull's-eye values can come from another image (step 4).
   * **⟲ Reset rotation**: start from scratch; removes the short-axis images, the 17 segments and the bull's-eye,
     angles, shift and segment angles back to their defaults (the LV segmentation is kept).
3. **17 segments**: base → apex cuts (default 29 / 58 / 87 % of the LV length), crop margin,
   numbering **1 = apex** (as the pipeline) or **AHA** (1–6 basal, 7–12 mid, 13–16 apical, 17 apex).
   Tested against the pipeline on P1: 99.5 % of voxels identical. The sector angles are measured in **mm**: with
   non-square pixels (e.g. CT 0.98 × 3.75 mm) angles in pixels made the anterior / inferior segments much smaller
   than the lateral / septal ones (square pixels with the standard angles: exactly the pipeline).
   **Segment angles (manual correction)**: choose *Apical* (4 segments), *Mid* or *Basal* (6), then change the **width**
   of a segment (−5° / +5° or type it): a wider segment takes the degrees from both neighbours, half each (anterior
   +10° = anterolateral and anteroseptal −5° each), so the ring always covers 360°; each segment keeps at least 5°.
   *from* moves only a segment's start angle (0° lateral, 90° anterior, 180° septal, 270° inferior): the previous
   segment grows, this one shrinks. *rotate ring* turns the whole ring, *standard angles* puts it back.
   **live** (on by default): the 17-segment segmentation and the bull's-eye values follow while you change an angle
   (a few times a second during a drag); the 17 segments already transferred to other images follow when you let go.
   Live off (saves computation on large images): change the angles, then press **✔ Apply to the segmentation** (shown
   while changes are not applied yet). Each segment name has a swatch in the colour of its label in the
   *LV 17 segments* segmentation (also in the table), and the names are never cut. Script: `cardiac17 width=mid:1:80` (segment 1 of the mid ring, from 0, to 80°).
4. **Bull's-eye**: mean, max, % of max or volume per segment of any image, or **segment colours** (each sector in its
   label colour, to match the segmentation on the views) (anterior at the top,
   septal on the left). Hover a segment for its values.
5. **Save and transfer**: save the short-axis images and segmentations, the 17 segments in the
   original space, the rotation (`short-axis-transform.tfm`), a CSV table and a log.
   **Transfer** maps the 17 segments onto a non-reoriented image.

Script / Python: `cardiac seg=0|label=1|auto=1|angles=17.7,27.9|images=0,1|other=1|shiftref=1`,
`cardiac17 percents=29,58,87|margin=1|numbers=aha|bounds=apical:315,45,135,225;mid:0,60,120,180,240,300`,
`cardiacbull value=0`, `cardiactransfer 0`, `cardiacsave <folder>`, `cardiacreset`; `cardiac …|crop=1|cropmm=30`.

**Image only (no segmentation).** Press *🔄 Use the image only*, choose the image, then set the **LV centre**:
*🎯 Automatic guess* (the brightest myocardium around the crosshair, or around the image centre: the voxels within
70 mm above half of the 99.5th percentile there; their centre and long axis are the guess), or click the middle of
the LV cavity on the views and press *📍 At the crosshair*. Then the **Short axis** block is the same as above
(images to reorient, crop, axis angles, roll, shift, mouse correction, *Create / update short axis*, *Show SA ·
HLA · VLA*). The guess is a starting point: on a test FDG PET its centre was 11 mm from the segmentation's and its
axis about 15° off, so always check it on the long-axis views. No 17 segments or bull's-eye in this mode (they need
the segmentation); *🫀 Use the LV segmentation* switches back. Script: `cardiacimage image=0|auto=1` (or
`centre=x,y,z`), then `cardiac images=0`.

**Splash view.** The classic cardiac display: **short axis** slices (apex → base; anterior up, septal left, lateral
right), **vertical long axis** slices (septal → lateral; base left, apex right, anterior up) and **horizontal long
axis** slices (inferior → anterior; shown **apex up, septal left, lateral right**). Reorient each image first (stress
and rest, or up to four images, each with its own axis, in either section above), then in the splash section choose
up to **four short-axis images**, one per row, with a **left and right comment** per row (only for this view, not
the image's nickname or comment). Each view shows its rows on top of each other (e.g. stress above rest), with
*N* slices evenly spread over the LV (default 12), an optional **slab** (mm, averaged around each slice), the tile
resolution, and the colormap (each image's own, or one for all). Every image is scaled to its own myocardial maximum
(0–100 %; the 99.5th percentile within 70 mm of its LV centre); its colour scale and maximum are at the end of each
row. *▦ Open the splash view* opens it in its own window (move it to another screen, maximise it), in ORCA-MI's
theme and interface size. Its toolbar has the number of **slices** (odd, 3–31: the middle slice is the LV centre), slab, resolution,
the colours of all rows (each image's own, grey, hot iron, …), *⟲ Reset zoom, pan and slices* and **💾 Save PNG…**
(the whole view: three views, every row, comments, colour scales and maxima, on white). On the images:
* **drag** = pan and **Ctrl + wheel** = zoom, per view (all rows of that view move together, so stress and rest
  stay aligned);
* **right-drag** = window: left / right = width, up / down = level;
* **click a slice** = it becomes the middle one: the slice next to the middle moves the range by one slice, the
  second by two, and so on (to the right or to the left; each image and each view separately, e.g. when the rest LV
  is longer than the stress LV). A **notch** on top of each view's first row and under its last row marks
  the middle slice (size and colour in ⚙ Settings);
* the **colour bar** (vertical, right of the row: maximum on top, minimum at the bottom): **drag its top half** up /
  down = maximum, **its bottom half** = minimum; **click** it to pick the colormap; **right-click** on the images =
  the colours of that row too (or set them in *Images and comments*). The heart drawing on the left is drawn in soft
  colours, in the middle of the view's rows. **☀ / 🌙** next to the title = light / dark background of the window
  (⚙ Settings → *Background*: ORCA-MI theme, light or dark).

The left comment is written above the first slice of each row, the right comment above the last one. All rows
start in **PET-DICOM** colours (*Colours* in ⚙ Settings: one colormap for all, or each image's own).

* a small **heart drawing** left of each view names the walls (SA: septal left, anterior up, lateral right,
  inferior down; VLA: base left, apex right; HLA: apex up, septal left, lateral right).

**Per row** (Cardiac tab or *Images and comments*): the image, left / right comment, colours, **gamma** (1 = linear),
a **segmentation** drawn filled (e.g. the LV 17 segments) and a **CT** underneath. The CT can be one reoriented
together with the PET (list *Reorient these co-registered images* in the short-axis block: each becomes a short-axis
image), or the usual **axial CT**, reoriented on the fly with that row's axis. The toolbar has:
* **🔒 Pan / zoom locked** (default): all rows of a view move together; unlocked, each image has its own pan and zoom;
* **Window**: *% of max* (min / max in % of each image's myocardial maximum, e.g. SPECT) or *absolute* (image
  units, e.g. SUV for PET); *sync all rows* = one min / max for every image, else each row its own window
  (colour bar or right-drag on its images); the **gamma** of each image is in ⚙ Settings;
* **Opacity** of the image over the CT and of the segments, and one **CT window** (HU) for every CT.

The images are sized so the three views fit the window (two images: no scrolling). The toolbar's first row
starts with the pan / zoom lock; **⚙ Settings** (next to *Images and comments*) holds the number of **slices**, the
**slab**, the **colours** of all rows, the **text size** of the window (applied when the slider is released), the
screen **resolution** (192 px per image by default) and the **paper** of the PNG: A4 (default, landscape), A3, A5,
Letter or *fit to the content*, landscape / portrait, dpi (600 by default, up to 900: A4 = 7016 × 4961 px). The view
is scaled to fit the page, centred across and placed from the top (one image: at the top of the page; several:
below each other from the top).

**◎ Bull's-eyes** (toolbar, on by default): a bull's-eye of each image right of the views (centre = apex, outer ring =
base; anterior up, septal left, lateral right), also in the PNG. They are made from the short-axis image itself, so
no segmentation is needed: a polar map (the maximum along each ray from the LV axis, apex → base) and the mean of
the polar map in each of the 17 segments (in % of the image's myocardial maximum in the *% of max* window mode, else
in image units), in the row's colours and window. Show *numbers* (segments coloured by their value, with the
values), *image* (the polar map) or *image + numbers*. The polar map is **interpolated** by default (⚙ Settings →
*Bull's-eye image*: blocks, interpolated or smoothed). Tick *Bull's-eye* per row in *Images and comments* to show
only some of them; they all have one size, set by the number of rows.

**Notes** under the bull's-eyes (bottom right): free text (comments, quantification…), editable in the splash
window; the PNG has the same box, with the text and room for handwriting.

Image-only short axis: the crop margin is **100 mm** by default (the heart is not cut in the splash view). Choosing
another image there clears the ticks of the images reoriented with it; *Only images of this study* (on by default)
lists only that image's study. *Axis shown on* is only in the segmentation section. *Show SA · HLA · VLA* shows the
short axis of the image the axis was made on (with a segmentation: the bull's-eye value image if one is chosen).

Script: `splash rows=2,3|left=Stress;Rest|right=…|n=12|slab=0|zoom=1.5,1,1|shift=<row>:<view>:<k>|cmap=<row>:<name>|gamma=<row>:<g>|wl=<row or all>:<min>:<max>|wlmode=pct|abs|wlsync=1|lock=0|rowzoom=<row>:<view>:<z>|seg=<row>:<image>:<seg>|ct=<row>:<image>|ctwl=-160,240|opacity=0.6|segopacity=0.4|notes=<text, 
 = new line>|fontscale=1|paper=a4|a3|a5|letter|fit|orient=landscape|portrait|dpi=300|bull=1|bullmode=numbers|image|fused|bullinterp=blocks|interpolated|smoothed|click=<row>:<view>:<slice>|bg=light|dark|theme|notch=<size>:<colour>|rowbull=<row>:0|1|png=<file>|open=1`
(rows and views from 0; views 0 SA, 1 VLA, 2 HLA).

## 5d. Image comparison: errors, gamma index, noise power spectrum

Right panel → **⚖ Compare**. Choose the **reference** and the **evaluated** image (the evaluated one is resampled onto
the reference grid when they differ), an optional clipping range, an optional **mask** (statistics inside the mask,
or outside set to the minimum as in yazdan) and an optional **regions** segmentation.

* **Bias map** (evaluated − reference) and **% bias map** (100 · bias / reference, 0 where the reference is 0) are
  added as images (CoolWarm colormap, symmetric window).
* **Compute metrics** (as `yazdan.image.image_match_eval`): ME, MAE, RMSE, MSE, MPE %, MAPE %, SSIM (3D, 7³ window,
  as scikit-image, on min-max normalised images), PSNR and Pearson r; and per region label: volume, reference and
  evaluated mean / median / SD, ME, median shift, RE % and RAE % per region and per voxel. Tested equal to the Python
  function. (yazdan reports SSIM × 100; ORCA-MI gives 0…1.)
* **Gamma index:** value criterion in % of the reference maximum (global) or in image units, distance to agreement
  (mm), low-dose cut-off, sub-voxel search (1/2, 1/3, 1/5 voxel with interpolation), signed gamma. Standard gamma
  (Low 1998) or **as yazdan.RT.gamma_evaluation** (both images compared at the shifted voxel). The gamma map is added as
  an image; pass rates are given for the evaluated voxels, the mask and every region label. Note: the Python function
  applies the spacing in x, y, z order to z, y, x arrays; ORCA-MI uses each axis' own spacing.
* **Noise power spectrum:** axial square ROIs (16–128 px, optional 50 % overlap) entirely inside a mask (a phantom,
  liver, fat…) or anywhere; mean or plane detrending; 2D NPS radially averaged. The plot shows NPS vs spatial
  frequency (1/mm); the noise variance (∫ NPS), mean ROI SD, peak and mean frequency are given. *keep curve* overlays
  several NPS (e.g. two reconstructions).
* **Save CSV / Copy:** everything in one table.

Script: `compare ref=0|eval=1|mask=0:1:1|regions=0:0|clip=0,1e9`, `comparemaps percent=1`,
`gamma dd=3|percent=1|dta=3|cutoff=10|sub=2`, `nps image=0|mask=0:1:1|roi=32|overlap=1|detrend=plane`.

## 5e. Lesion tracking: RECIST, PERCIST, TMTV

Right panel → **🎯 Lesion tracking** follows the lesions of a patient over up to **10 time points**: a baseline and
up to 9 follow-ups (**➕ Add follow-up**; ✖ next to a follow-up removes it). With one follow-up everything below is
the same as in the original two-time-point tool (names, tables, CSV, report).

1. Register **each follow-up onto the baseline** (Register tab: fixed = baseline, moving = follow-up; for PET/CT
   register the CTs and apply the registration to the PET in place, see *Named registrations*).
2. Choose, for the **baseline** and **each follow-up**, the PET (the values) and the **lesion segmentation** (any
   segmentation, e.g. a threshold, an AI result or one drawn by hand; *every label* or one label).
3. Choose, for each follow-up, its **registration**: the follow-up image's own (as set in the Register tab) or a saved
   one.
4. **🎯 Find lesions and suggest links**: each connected region of one label (26-connected, or 6-connected with
   *joined only through faces*; larger than *ignore below*, e.g. 0.1 ml) is one lesion — two lesions with different
   labels stay apart even where they touch. With *every label*, labels named *liver* are not lesions. ✂ next to the
   lesion segmentation first **separates** it: every connected region becomes its own label ("<segmentation> 1, 2…",
   also in the Segment tab → *✂ Separate connected regions*), useful after nnU-Net or a threshold. Each lesion is numbered largest first: **B1, B2…** on the baseline, **F1, F2…** on the follow-up (with
   several follow-ups **F1.1, F1.2…** on follow-up 1, **F2.1…** on follow-up 2 …). Each time point is linked to **the
   one before** (baseline ↔ follow-up 1, follow-up 1 ↔ follow-up 2 …): its lesions are moved through the registrations
   and paired with the closest lesion of the next time point within *link within* (mm), one to one. So a lesion that
   appears at follow-up 1 is followed at the next follow-ups (it is *new* once, not again at every follow-up).
5. Confirm the suggestions **one by one** (✔ link; 👁 puts both views on the two lesions), or all at once, or link
   two lesions by hand (with several follow-ups, first choose the pair of time points in **link**, e.g.
   *Follow-up 1 → Follow-up 2*): **🖱 Link by clicking** — a blue banner on the baseline view says *Step 1 of 2: click the
   lesion on the BASELINE image*; after the click it moves to the follow-up view (*Step 2 of 2: B1 chosen …*); both
   lesions are shown and you answer *Link* or *Try again* — or choose B… ↔ F… in the lists. ✖ unlinks.
6. Check the table, then **✅ Approve linking** (below the lesion table; it names how many lesions are linked, new
   and gone). The **📈 progress plots** and **📁 Save report…** need an approved linking; suggestions not decided
   when you approve stay unlinked. A green banner shows the approval; **✏ Change the links** (or any link, unlink or
   new search) withdraws it, approve again when done.

Linked lesions — a lesion followed over two or more time points — are renamed **L1, L2…** (those of the baseline
first) and get the same colour on every image (the colour of the lesion where it was first seen; a *Lesion tracking*
segmentation on each PET, and their number drawn on the 2D views while the tab is open). Lesions keep the colours and
names of their labels. Baseline lesions left unlinked are **gone** (B…), follow-up lesions left unlinked are **new**
(F…). The table shows each value over the time points (*34 → 26 → 18*; from 4 time points *first → … → last*, every
value on hover); ✖ removes every link of that lesion.

**Per lesion:** longest axial diameter (mm), volume (ml), SUVmax, SUVmean, SUVpeak (mean in a 1 cm³ sphere around
the maximum), TLG, and their change.

**Response:**
At **every follow-up**, against the baseline:
* **RECIST 1.1**: up to 5 target lesions ≥ 10 mm at baseline (largest first), sum of longest diameters (SLD).
  CR: all targets gone; PD: SLD +20 % and +5 mm from the **nadir** (the smallest SLD so far, the baseline at the
  first follow-up), or any new lesion (not seen at the baseline); PR: SLD −30 % from the baseline; SD otherwise.
  The 2-per-organ limit, lymph-node short axis and non-target lesions are not applied: check the targets.
* **PERCIST 1.0**: SULpeak of the hottest lesion at each time point (it may be another lesion).
  CMR: no lesion left; PMD: +30 % and +0.8 SUL, or a new lesion; PMR: −30 % and −0.8 SUL; SMD otherwise. With a
  liver segmentation, the baseline lesion must reach 1.5 × liver mean + 2 SD to be measurable. PERCIST is defined
  on SUL: convert the PET first (Image → SUV → SUL); a warning is shown otherwise.
* **TMTV** (total metabolic tumour volume, sum of the lesion volumes) and **TLG** (sum of mean × volume) at both
  time points, with their change.

**💾 CSV / 📋 Copy:** the lesion table and the responses.

**📈 Progress plots:** one line per lesion over the time points (baseline, follow-up 1, 2 …) for the chosen measure (volume, longest
diameter, max, mean, median, peak, TLG), with the change in % in the legend. Tick lesions to show or hide them;
lesions on one time point only are single points (*baseline only*, *new*). Below, the **all lesions** plots, each on
its own scale: the average of the measure over the lesions ± SD, the total volume (= TMTV, ml), the total TLG and
the number of lesions, each shown or hidden. *📋 copy table* puts every series on the clipboard as CSV.
Script: `lesionplot 1`.

**📁 Save report…:** see *Report folders* below (lesion table, responses, curves and box plots per measure, totals).
With several follow-ups: one table per measure with a column per time point, the response at each follow-up (TMTV,
TLG, SLD, nadir, RECIST, PERCIST), the lesions of each time point, and curves over time (each lesion, TMTV, TLG,
number of lesions, SLD).

**🆕 New and disappeared lesions** (under the lesion table, for every pair of time points — baseline → FU1, FU1 → FU2 …): the lesions **new** at the later time point (no link from the earlier one) and those that **disappeared** (seen at the earlier time point, no link to the later one) are listed as chips; click one to show it, right-click to **✔ confirm** it (new lesion / disappeared, treated). *Mark as new at …* / *Mark as disappeared at …* mark any lesion, also a linked one: its link between these two time points is removed and it is not suggested again (the approval of the linking is withdrawn, approve again). So a lesion can appear at FU2 and disappear at FU3. Script: `lesionmark new|gone <pair> <lesion> [off]` (pair 0 = baseline → FU1; lesion = 0-based index at the later (new) or earlier (gone) time point).

Script: `lesiontrack base=0|bmask=0:0:0|fu=1|fmask=1:0:0|bliver=…|fliver=…|tf=<saved k>|dist=25|minml=0.1`
(prints `[suggest] B1|F2|mm`); more follow-ups with `fu2=2|fmask2=2:0:0|tf2=…` up to `fu9`, `n=<time points>` keeps the
first n (suggestions of the later pairs print `[suggest] pair=2|F1.1|F2.2|mm`); `lesionlink pair=2|1,3` links F1.1 with
F2.3; `lesionlink 1,2` / `lesionlink all` / `lesionlink unlink 1` /
`lesionlink goto 1`, `lesionlink approve` / `lesionlink unapprove`, `lesionreport` (prints `[lesion]`, `[recist]`, `[percist]`, `[tmtv]`),
`separate <image>:<seg>:<label>|conn6=0|minml=0` (connected regions → a new segmentation).

## 5e2. Prognosis (coming soon)

The **📈 Prognosis** tab will hold machine learning models to predict the treatment response (from the images,
segmentations, dosimetry and lesion measurements of a patient). Coming soon. Script: `tab prognosis`.

## 5f. Report folders: lesion tracking, segment statistics, image comparison, segmentation comparison

**📁 Save report…** (Lesion tracking tab, Compare tab, Segment tab → 📐 Compare segmentations, and *📁 Report…* next to *Export CSV* in the Image tab's
segment statistics) writes one folder (`<folder>/<report name>`, default *Documents/ORCA-MI reports*, name with the
patient and the date). Choose what to save:

* **tables (CSV)** and one **Excel workbook** (one sheet per table, an *Information* sheet and a *Charts* sheet with
  the pictures);
* **charts** as **PNG** (2× resolution) and **SVG** (vector, for papers);
* **summary (HTML)**: information, every table and every chart in one page (opens in any browser, prints to PDF);
* **information (JSON)** and a **log** (the settings and this session's ORCA-MI log).

Every report holds the date and local time, ORCA-MI version, computer, Windows user and time zone, the reader name,
the **patient** (name, ID, birth date, sex, age, weight, height, institution) and the **images** (name, modality,
unit, grid, study / series, scanner, registration, filters, file). *Anonymise* leaves out the name, ID, birth date and
file paths (always on during blinded reading).

| report | tables | charts |
|---|---|---|
| Lesion tracking | each lesion (linked / gone / new) with LD, volume, max, mean, median, peak, TLG at both time points and their change, centres; response (RECIST 1.1 SLD, PERCIST 1.0 peak, TMTV, TLG, counts); all baseline and all follow-up lesions; the plotted values | per chosen measure: each lesion baseline → follow-up, and a box plot over the lesions of each time point; TMTV, total TLG and number of lesions |
| Segment statistics | every region: voxels, volume, mean, SD, min, p5, Q1, median, Q3, p95, max, peak, sum, TLG, centre, extent; total | box plot of the values in each region; mean / median / max and volume per region |
| Segmentation comparison | per label: Dice, Jaccard, sensitivity, specificity, precision, volumes, volume difference / similarity, Hausdorff, HD95, ASSD, MASD, surface Dice, centroid distance, TP / FP / FN, with the **mean over all labels** as the last row (voxel counts summed); every value in a long table | Dice and Jaccard per label |
| Image comparison | whole-image metrics; regions (means, medians, SD, ME, MAE, RE / RAE %, percentiles of both images and of the voxel error); gamma; NPS | box plots of the reference and evaluated values in each region and of the voxel-wise error %; relative error per region; NPS curve |

Lesion tracking settings and criteria (registration, link distance, minimum volume, connectivity, the RECIST and
PERCIST rules applied) are listed in the information. Box plots: box Q1–Q3, line median, dot mean, whiskers
5th–95th percentile.

Script: `report lesions|stats|compare|segcompare|folder=<dir>|name=<name>|csv=1|xlsx=1|png=1|svg=1|html=1|json=1|log=1|anon=0|measures=volume,max,mean`.

## 6. AI: segmentation, enhancement, training

### Installing on a new PC (no Python)

**Offline PCs (no internet, or a firewall that blocks the installation):** on a PC where the AI works, open *Install AI environment* and use **📦 Export for PCs with an NVIDIA GPU…** (the environment as installed, about 5–8 GB; with its CUDA build of PyTorch it also runs on a PC without a GPU) or **📦 Export CPU only…** (a copy with the CPU build of the same PyTorch, about 2–3 GB; needs internet on the exporting PC). Carry the zip (USB disk) and on the offline PC use **📥 Import environment zip…** in the same window: it is unpacked into ORCA-MI's Python folder (an environment already there is kept as `orca-mi.old`), checked, and used for the AI models. Models are downloaded or copied separately (model library).

The viewer itself needs nothing. AI features need Python + PyTorch. On a PC without them:

1. Tools → **🧰 Install AI environment (Python + PyTorch)…** (the AI tab shows the same button when no Python is
   found).
2. The dialog detects an NVIDIA GPU and picks the matching PyTorch build (CUDA 12.8 / 12.6 / 12.4 / 11.8, or CPU).
   Choose the packages: nnU-Net v2, nnInteractive, MONAI and optionally TotalSegmentator.
3. **⬇ Install** downloads Miniforge, installs it privately (no administrator rights, nothing added to PATH or the
   registry) into `%LOCALAPPDATA%\ORCA-MI\python`, creates a Python 3.11 environment and installs the
   packages. Progress is shown in the job bar and every line goes to the log. It takes about 10–30 minutes and
   needs ~3 GB (CPU) or ~8 GB (CUDA). When it finishes, every model preset uses the new Python automatically.
   (Conda refuses folders with spaces; if the user name has one, the default becomes `C:\ORCA-MI-Python`.)
4. Already have an environment? *Use an existing Python…* picks its `python.exe`.

**Tested versions:** the installer (and *Install … into this Python*) installs the Python package versions ORCA-MI
was tested with, not the newest ones, so a new release of nnU-Net, nnInteractive or MONAI cannot break a new
installation. PyTorch: the tested version is tried first for each CUDA build, then the newest one. A Python that
already has PyTorch and numpy keeps them. If pip cannot install the tested versions (e.g. another Python version
without those packages), it installs the newest ones instead (written in `ai_setup.log`). The author can change the
tested versions without a new ORCA-MI release (they come with the model list).

Script / Python: `installenv auto` (or `cpu`, `cu126`, `cu128`). Image-to-image models run on such a PC through the
built-in MONAI runner; your `yazdan` package is used only when it can be imported.

### Inputs of multi-channel models: which image is which

Every input (0000 included) is suggested an image of the modality its channel name in the model's `dataset.json`
asks for (CT → a CT, PT / PET / SUV → a PET, MR / T1 / T2 → an MR, NM / SPECT → a SPECT; whole words, each image
used once), again whenever the model or the loaded images change; your own choices stay until then. An input whose
image type differs from its channel shows ⚠ and the button becomes *Run anyway*.

For an nnU-Net model with several inputs the AI tab shows **Inputs: which image is which**: one row per channel,
named from the model's dataset.json (e.g. *0000 CT*, *0001 PET*). Choose the image of each: input 0000 is the active
image unless you pick one. Images are suggested by modality, and ⚠ marks an image whose modality does not match
the channel name. The other inputs are resampled onto input 0000 through their registrations. The log of each run
records which image went to which input. The same mapping is set for database segmentation (*Model inputs*).

### AI inference details

* **Progress bars:** nnU-Net, image-to-image and batch runs show the tqdm progress of the Python process
  (step, %, time left) in the job bar; *Cancel* stops the whole process tree.
* **Default models (Yazdan Salimi):** low-dose CT enhancement, all-organs CT, PET PSMA / FDG lesions, PET/CT
  organs (fewer classes), low-dose PET and low-dose bone SPECT enhancement. Download links are filled in when the
  models are published; until then set the model folder by hand.
* **Model information:** `dataset.json`, `plans.json` and any `README` / `model_info.json` in the model folder
  are read and shown before running (labels, channels, spacing, description). **🔄 Load model information** (first
  button of the section) reads the folder again at once: labels and input channels (the *Output labels* table),
  configurations, folds and checkpoints on this PC; it says what it found. A nnU-Net model folder set one level too
  high (the dataset folder holding `nnUNetTrainer__nnUNetPlans__3d_fullres`) is resolved to the trainer folder for the
  information, the folds and the run. Script: `modelinfo [preset]`.
* **nnU-Net without MONAI:** some checkpoints keep MONAI objects (e.g. a loss in the saved trainer settings, or the
  configuration written as MONAI's `NNUNETMode`) although inference does not use MONAI. Without MONAI installed,
  ORCA-MI reads such a checkpoint with stand-ins for MONAI during the load only (log: *checkpoint read without
  MONAI*); values such as the configuration (`3d_fullres`) are kept. Trainer modules that need MONAI are skipped in
  the trainer search.
* **Mirroring (TTA)** is off by default (AI tab → Configuration → *Mirroring TTA*): several times faster with nearly
  the same result. Tick it for a model when you want the last bit of accuracy.
* **Speed** (AI tab → Configuration, nnU-Net): **🐇 Ultra fast (CPU)** = 1 fold, no mirroring, step 0.95, input
  cropped to the body — the fastest and **not accurate** (rougher borders): meant for a quick result when nnU-Net runs
  on the CPU (a computer without a suitable GPU); an orange warning is shown while it is chosen; **⚡ Fast** = 1 fold,
  no mirroring, step 0.7, input cropped to the body; **⚖ Balanced** = every fold on this PC, no mirroring, step 0.5;
  **🎯 Accurate** = every fold, mirroring, step 0.5.
  Changing any of them by hand shows *custom*. **One fold by default:** a model runs its first fold on this PC unless
  you tick more folds (or choose Balanced / Accurate); the models already in the list were set to one fold once.
* **Workers** (nnU-Net): the processes that prepare the image and write the result next to the GPU. *auto* (0) picks
  them for this PC, model and image: the model's spacing, patch size and number of classes (plans.json /
  dataset.json) and the image size give the memory each worker needs (e.g. a many-class model such as Bones (CT) on a
  whole-body CT is heavy), the free RAM and the CPU cores give how many fit (1–8). The line under it says why
  (e.g. *heavy run: 24 classes, 85 M voxels … ~4.1 GB per worker, 40 GB RAM free, 32 cores → 6 workers*). When the
  class scores would not fit on the GPU next to the network, they are kept in RAM (slower, but no out-of-memory).
  The log shows the numbers used (`[ai] … workers used: n`).
* **🧹 Post-processing** (AI tab, below the model information; each step has **↶ Undo**):
  * **Segmentation**: the one to clean (default: the active segmentation).
  * **✂ Remove outside the body**: every voxel outside the **body contour** is set to 0. The default body contour
    is the image's own *Body contour* (Segment tab → Body contour; never the MOOSE body segmentation); choose another
    segment, or **➕ Create** it here.
  * **🧩 Combine low-dose CT organs (5 sets)**: the five low-dose CT organ models (*uldct_set_1 … 5*, LR or HR) of
    the image → one segmentation *ULDCT 22 organs (LR / HR)* with the 22 organs of
    `yazdan.oar_new.combine_uldct_five_Sets` (organ by organ, a later organ wins a voxel claimed twice).
  * **🧩 Combine FDG organs (3 sets)**: the three FDG PET organ models (*organs · FDG (PET) · set_1_bones*,
    *set_2_soft_hot*, *set_3_soft_cold*) → one segmentation *FDG organs (ULDCT values)* with the **same organ values
    as the low-dose CT map** (Adrenal glands = 1, Aorta = 2, Brain = 3, … Heart = 22), so FDG and low-dose CT maps can
    be compared label by label. The FDG sets have 20 of the 22 organs (no Erectus spinae, no Small Bowel).
  * **remove organs in the arms (MOOSE body)** (both buttons; **off** by default): every organ voxel inside the arms of
    the MOOSE body segmentation (label 4) is removed. Labels are matched by name, or by the sets' own tables when the
    files have no label names; missing sets and unknown labels are reported.
  * **Only some of the sets?** Both buttons work with any of the sets: every organ found gets its fixed value (the same
    as the Python functions), the organs of the missing sets stay empty and the result names the missing sets. Run the
    missing models later and press the button again: the combined segmentation is rebuilt from all the sets now there
    (↶ Undo returns to the previous one).
  Scripts: `postbody [target=<img>:<seg>]|[body=<img>:<seg>:<label>]`, `postuldct [img=<i>]|[arms=0|1]`,
  `postfdg [img=<i>]|[arms=0|1]` (prints `[postfdg] …`), `postundo`.
* **Folds (nnU-Net and image-to-image):** most models were trained five times (folds 0–4) and the result is the
  average of the folds you use. AI tab → *Configuration* → **Folds** shows check boxes 0–4: only the folds on this PC
  can be ticked (hover over a grey one: it is not downloaded). Fewer folds run faster and are a little less accurate.
  The log shows the folds used (`[ai] folds: 0,2`); ticked folds that are not on the PC are skipped. Image-to-image
  models use their `fold_N` / `fold--N` folders the same way. Outputs are resampled back onto the input grid, so
  they are never cropped or shifted.
* **GPU memory is released after every run:** nnU-Net and image-to-image models (MONAI) run in their own Python
  process, which frees the GPU memory and ends as soon as the results are written; if it does not end within 20 s
  ORCA-MI stops it (log: *stopped to release the GPU memory*). Only nnInteractive keeps its model on the GPU while
  the Segment tab uses it (**⏹ Stop** in its nnInteractive section frees that memory).

### Distributing models (download links)

Tools → **⬇ Model library** lists every model with its status, its download link and an **Install / Update**
button. Models are downloaded only there: the AI tab shows no download link and no install button.

**Download only some folds:** each fold of a model is about 250 MB. The row of a model from the author's list has
fold check boxes (**✔** = already on this PC, hover for the size of each fold): tick the folds you want, then
**⬇ Download (n folds, size)**, later **⬇ Add fold …** for more, or untick downloaded folds and **🗑 Remove fold …**
to free the space. *Folds to download by default* (above the list) sets which folds a new download gets, also for
*⬇ Download all in this folder*. **⟳ Update** downloads the ticked folds again. Script:
`installmodel <name>|folds=0,1`. The files are downloaded into folders nested like the library, e.g.
`%LOCALAPPDATA%\ORCA-MI\models\organs\Bones (CT)` or `…\models\lesions\FDGPanCancer (PETCT)\PET`, and the preset is
pointed at the right folder automatically. Models downloaded by earlier versions (one flat folder each, e.g.
`organs___Bones__CT`) are moved into their nested folder once when ORCA-MI starts (nothing is downloaded again).
Each model folder holds a small `.orcami-model` file; deleting or updating a model never touches another model in a
folder below it.

The window has a bar on top, **🔄 Check now for new models** (fetches the author's list at once; only the version
number is sent), and four sections you can fold: **📚 Models** (the tabs), **📁 Model folder**, **🌐 Online model list
and library file** and **🧰 AI setup**.

* **📂** next to a model opens its folder (the downloaded folder, or the folder a local model points to);
  **📂 models folder** at the top opens the folder of all downloaded models.
* **💻 local** marks a model set up on this computer in the AI tab (➕ nnU-Net, ⧉ duplicate, a folder of your own),
  not one from the online (Google Drive) list. **✖** on its row removes it from ORCA-MI's list (after a confirmation);
  its folder and files stay on the disk (add it again with ➕ in the AI tab or *Model folder → Scan*). Script:
  `modelremove <index | name>`. 🗑 instead deletes a *downloaded* model's files.
* AI tab → **⧉ duplicate** asks for the name of the copy (proposed: *name (2)*); a name in use is refused.

**How to package a model:** zip the folder you would normally select in the AI tab:

* nnU-Net: the trained model folder holding `dataset.json`, `plans.json` and `fold_0 … fold_4`
  (`checkpoint_final.pth` inside each fold). Optional `model_card.json` with indication, modality, version and citation.
* Image-to-image: the folder holding `fold_0 … fold_N` (or the single checkpoint).

**Where to upload:** any public link works.

| Host | Notes |
|---|---|
| **GitHub Releases** | Recommended: direct links, files up to 2 GB, versioned |
| **Zenodo** | Gives a DOI (good for papers), up to 50 GB |
| **Hugging Face** | `…/blob/…` links are converted to downloads automatically |
| **OneDrive / SharePoint** | Share as *Anyone with the link*; the viewer converts the share link to a direct download. If a link only opens a web page, the viewer reports it, and GitHub / Zenodo / Hugging Face are the safer choice |
| Google Drive, Dropbox | Share links are converted automatically |

**Changing links without a new release:** fill in `dist/models.json` (one entry per model: `name`, `kind`
`NnUnet` / `Regression`, `url`, `description`) and host that file publicly, for example in a GitHub repository.
Enter its address once in the Model library (*Online model list → 🔄 Check*): new models are added and links
updated. Script / Python: `modelmanifest <url>`, `installmodel <index or name>[|url]`.

### 🧠 Downloadable models (Google Drive links)

When the trained models are published, each gets a download link in the model library (`model_library.json` or
`models.json`). **Google Drive** share links work directly: share the zip as *Anyone with the link* and paste the
normal share link (`https://drive.google.com/file/d/<id>/view?usp=sharing`); ORCA-MI converts it to a download and
handles Google's "large file" confirmation. Tools → **⬇ Model library → Install** downloads, unzips and selects
the model.

### Model library file (your future models)

Tools → *Model library* → **📝 Edit model library file** opens `model_library.json`. It's one entry per model:
* `name` (required)
* `kind`: nnunet / regression / command
* `url`: download link to a zip
* `model_path`: local folder
* `indication`
* any other fields you like: modality, input, output, version, citation, author, contact, licence, notes. They're all shown in the AI tab.

Save the file, then press **🔄 Reload** (it is also read at every start).
A `models.json` next to `ORCA-MI.exe` is read as well, for distributing a list with the program.
Fields you write update existing models; nothing else is overwritten, so an installed model keeps its folder.

### 🏋 Train tab: your own nnU-Net and fine-tuned nnInteractive

> 🔒 **Training stays on your PC.** Your training data, the models you train or fine-tune, their evaluation and the
> training logs are never uploaded or shared with the author: not with the usage statistics (which only count how
> often a tool was used) and not with a bug report (training log lines are left out of its *recent errors*).
> Share a model only if you choose to, by copying its folder yourself.

Both use training data in the nnU-Net layout:

```
my_data/
  imagesTr/  case001_0000.nii.gz  (one file per channel: _0000, _0001 …)
  labelsTr/  case001.nii.gz
  dataset.json   (optional; created automatically from the labels if missing)
```

**Train your own nnU-Net** (official nnU-Net v2):
pick the folder, give the model a **name**, and choose:
* the configuration (3d_fullres, 2d or 3d_lowres),
* the network (standard U-Net, or ResEnc M / L for larger GPUs),
* the epochs (1 … 8000; 1000 is the nnU-Net default),
* the folds (any of 0–4, or all data),
* the **device**: GPU (CUDA) or CPU, with the free GPU memory next to it. The Train tab has its own device, so the
  Segment tab's nnInteractive device no longer changes the training.

**▶ Start training** then:
1. links the data into a private nnU-Net workspace (`%LOCALAPPDATA%\ORCA-MI\nnUNet`),
2. plans and preprocesses,
3. trains the folds.

When it finishes, the model appears **under its name in the AI tab**, ready to segment, with its labels read from `dataset.json`.

**Fine-tune nnInteractive**:
same data layout. Prompts (clicks, 2D boxes, lassos, scribbles and corrective clicks on the model's own mistakes) are simulated from your labels and fed in exactly the format nnInteractive uses.
Before and after training, the real nnInteractive is scored on held-out cases (one click and one 2D box per object). The new weights are kept only if they score better.
The model is saved under its name. Choose it in Segment tab → nnInteractive → **Model**.
This is experimental: the nnInteractive authors have not published their training recipe. The weights inherit the CC BY-NC-SA 4.0 licence (non-commercial use only).

Speed settings (Fine-tune nnInteractive → **Speed**):
* **data workers**: processes that load the cases, cut and resize the patches and simulate the clicks while the GPU
  trains (default: a quarter of the CPU threads, at most 8). When the GPU load jumps between 0 and 100 %, more
  workers help.
* **batch**: patches per training step (default 2; 3–4 fill a 24 GB GPU at 128³, lower it if the GPU runs out of
  memory).
* **cases in memory**: cases kept loaded by the workers together (fewer disk reads; each takes about 4 × its file
  size of memory).
* **checked cases**: validation cases scored with the real nnInteractive before training and at each check (default
  30; 0 = all). Scoring runs the whole nnInteractive on each case and is slow: 20–50 cases are enough to compare.
* **skip the check of the original model**: training starts at once.

On a 24 GB GPU this is about 2–3 × faster than before (0.64 → 0.24–0.31 s per 128³ patch on test data).
While the original model is checked the run shows *baseline check: case k / n*.

**A checkpoint after every epoch** (`<model folder>.partial`, removed when the model is saved): a run that was
stopped, failed or interrupted (PC restart) shows **▶ Continue**, which resumes after the last finished epoch;
*⟳ Run again* starts from the beginning.

**Final evaluation: original vs fine-tuned model** (Speed → *final evaluation*: on / off, *all validation cases*).
After training, the original and the fine-tuned model segment the same validation cases (the checked cases, or all
of them) with the same prompts: **every lesion** (26-connected region of each label) gets one click at its centre,
and, separately, one 2D box on its middle slice; the lesions of a case are put together into one mask per prompt type.
ORCA-MI then compares the masks with the references and shows **📊 Evaluation: original vs fine-tuned model** under
the run (green = better, red = worse):
* **segment comparison metrics** (as in the Compare tab): Dice, Jaccard, sensitivity, specificity, precision, volumes
  and relative volume difference, volume similarity, Hausdorff, HD95, ASSD, MASD, surface Dice at 2 mm, centroid
  distance, TP / FP / FN voxels;
* **lesion matching** (as `yazdan.image.lesion_match_eval`): each reference lesion is paired with the predicted lesion
  of best Dice (metrics per lesion; no overlap = missed); a predicted lesion touching no reference is a **false
  positive** (ids and volumes per case); lesions detected / missed, lesion sensitivity, false positives per case. An
  empty reference with an empty prediction counts as Dice 1.

*📂 Results* opens `<model folder>\evaluation`: `results\` (Summary, Per case, Per lesion as Excel, CSV, HTML, JSON)
and the predicted masks of both models (`original\point`, `originalbox`, `finetuned\…`, one NIfTI per case,
on the reference grid) to look at in ORCA-MI. *⟳ Recompute* computes the metrics again. Each lesion costs four
nnInteractive runs (2 models × click and box), so a final evaluation of many lesion-rich cases takes a while; it is
part of the run (▶ Continue resumes it).

**Training runs** (in the same tab):
* **Progress:** live progress bar with the time left, plus train/validation loss and Dice curves (hover for values).
* **Buttons:** Stop / Continue (resumes from the last checkpoint) / Run again / Log / Folder.
* **Export (zip):** writes a shareable model file.
* **Keeps running when the viewer is closed:** training is a separate process. Closing ORCA-MI while a training runs
  asks: **▶ Keep training in the background** (ORCA-MI closes, the training goes on and is shown again in the Train
  tab when you open ORCA-MI) or **■ Stop the training and close** (▶ Continue resumes it later), or Cancel.
* **Messages in ORCA-MI's log:** the lines of a running training are also written to the log window (bottom right,
  *log*), as `[train <name>] …`. 📜 Log opens the whole training log.

**Load a trained model by name:**
*📥 Load a trained model by name* imports a zip exported here, any nnU-Net results folder, or an nnInteractive model folder under the name you choose. The Model library can also install zips from a link.

Script / Python:
* `train <folder>|name=Liver CT|epochs=250|folds=0,1,2,3,4|network=resenc_m`
* `finetune <folder>|name=…|epochs=20|device=cuda|workers=8|batch=2|cache=64|checked=30|skip_baseline=0|eval=1|eval_all=0`
* `trainings`, `trainstop <k>`, `traincontinue <k>`, `traineval <k>` (k = 0 for the newest run), `logsearch <text>`
* `presets`
* `ai <model name>`
* `nnmodel <name>` (or `official`), `nnmodel list`, `nnmodel download <name>` (a fine-tuned nnInteractive model of
  the author's list)

### AI troubleshooting on another PC

**Missing packages:** ORCA-MI uses the Python set in the AI tab, which can be one of your own conda environments.
* **Before nnInteractive starts**, ORCA-MI checks that nnInteractive and PyTorch are in that Python. If one is missing, the nnInteractive section offers two options:
  * **⬇ Install nninteractive into this Python**, via pip. Your PyTorch and numpy versions are kept, but other packages of that environment may be updated. After the install the nnInteractive model is downloaded and nnInteractive starts.
  * **🧰 Separate ORCA-MI AI environment** (recommended): a private Python only for ORCA-MI, so your research environments stay untouched.
* **AI tab → Python packages** shows ✔ / ✖ for PyTorch, nnInteractive, nnU-Net, MONAI, SimpleITK and nibabel, with an *Install missing* button.
* When a new AI environment is installed, presets that already use a working Python keep it. Only presets without a working Python are moved to the new one.
* Python: `v.command("packages")` and `v.command("installpackages nninteractive")`.


* **🩺 Check AI setup** (AI tab or Model library) opens a **package versions** window: Python, PyTorch,
  torchvision, numpy, SciPy, SimpleITK, nibabel, nnU-Net (and its dynamic_network_architectures, batchgenerators,
  acvl_utils, blosc2), nnInteractive, MONAI, einops, huggingface_hub and TotalSegmentator, each with the
  **installed** version, the version ORCA-MI was **tested** with, and ✔ or **⚠ differs** (a version that differs
  usually works; if a model fails, reinstall the AI environment, which installs the tested versions). 📋 copies the
  table, 📄 opens the full report. It writes `ai_diagnostics.txt` (the versions table first). It covers:
  * Python version and every AI package, with the actual import error,
  * PyTorch, its CUDA build and a GPU test,
  * internet access to Hugging Face, PyPI and PyTorch, and proxy settings,
  * the nnInteractive model folder (writable? which models are present?), and free disk space.

  It also includes the end of the installer log (`ai_setup.log`). Send the file if something fails.
* **The installer now:**
  * tries PyTorch CUDA builds from the newest the driver supports down to older ones, then the CPU build;
  * pins the installed PyTorch so later packages cannot replace the CUDA build;
  * pre-downloads the nnInteractive model;
  * installs to `C:\Users\Public\ORCA-MIPython` when the user name contains spaces.
* **nnInteractive model download:** if nnInteractive's own download fails, the viewer tries a direct Hugging Face download, then any model already on disk. The error message says what to do (proxy, or download the folder by hand and pick it as the model).

### If the window blinks or stutters while AI runs

* **Priority:** AI processes (nnInteractive, nnU-Net, image-to-image, training) run at below-normal priority, and nnInteractive leaves two CPU cores free, so the viewer stays responsive on laptops without a GPU.
* **Small GPUs:** with nnInteractive running on a GPU of 8 GB or less, 3D views automatically use a smaller volume (256³) to leave graphics memory for the AI. Running out of graphics memory makes Windows reset the driver, which looks like the whole window blinking.
* **If it still blinks:** untick *🖼 Image* in the 3D view, or switch the 3D renderer to CPU (3D tab). Then send `ai_diagnostics.txt` (🩺 *Check AI setup*).

Python: `v.command("python C:/path/to/python.exe")`, `v.command("nndevice cpu")`.

### AI models: folders, several models at once, progress

The AI tab lists the models as the author's folders (category → task → models); *only models on this PC* hides
those not downloaded. Tick several models (or *tick all* of a task, e.g. the five low-dose CT sets) and press
**▶ Run the ticked models on the active image**: they run one after the other, a model already run on the image is
skipped. Running a model again on an image that already has its segmentation asks first. The running model shows a
large progress bar (with Cancel) in the AI tab and in the status bar; the images can be used meanwhile. The result is
shown at once: the image becomes active and its new segmentation the one shown in the Segment tab, 2D and 3D views
(a warning tells when a model found nothing).

The model library shows the same folders, with **⬇ Download all** per folder or task, the download progress in each
row, ⏳ queued / ✔ downloaded / 🗑 delete, and *coming soon* for empty folders. The author's models are named
"YS · …".

### ⚡ Faster inference: crop to the body and to a z-range

*AI tab → Run* and *Segment tab → nnInteractive → Inference region* have the same settings:
* **crop to the body contour** (+ margin): the image's body segmentation if it has one, else the body contour of a
  CT, or the largest region above 5 % of the maximum of a PET, SPECT or MR;
* **limit the z-range**: two dashed lines appear on the coronal and sagittal views (and as dotted planes on the 3D
  views); drag them, or type the positions (mm). They are world positions, so they apply to every image. A press on
  (or within 12 px of) a line takes it and it follows the mouse until you release the button. **🖱 move the lines
  with the mouse** (tick): a press anywhere on a coronal / sagittal view takes the nearest line.

The panel shows the size of the input (e.g. 38 % of the voxels). nnU-Net and image-to-image models get only that
box; the segmentation comes back on the whole image (zero outside). nnInteractive gets its region clipped to it.
Keep the whole organ (with a margin) inside the z-range: on a lung-lobe model the body crop alone (17 % of the voxels,
3.5× faster) gave the same lobes (Dice 0.98–0.997), but a z-range cutting through the lungs changed the lobe labels
also away from the cut. Script: `aicrop body=1|margin=10|z=-950,-700`, `aicrop off`.

### 🗂 Model folder (e.g. Google Drive)

*Tools → Model library → Model folder*: choose a folder organised as

```
segmentation/nnUNET/<organs|lesions>/<Task>--<Modality>/<trainer__plans__config>/fold_k/checkpoint_final.pth
segmentation/nnUNET/<organs|lesions>/<Task>--<Modality>/<model>/<trainer__plans__config>/...   (several models)
image-to-image/<group>/<Task>/...   (fold_k folders or a checkpoint)
segmentation/nnInteractive/<model>/...
```

and press **Scan and add** (empty folders are listed as *coming soon*). Image-to-image folders below the task are their
own levels in the lists, e.g. `image-to-image/LowCountNM/LowCountPET-no-segment/QuadraSiemens/10%/<model>` is shown
under *LowCountNM → LowCountPET-no-segment › QuadraSiemens › 10%*; a model folder named
`model--weights--…--patch--3D` (e.g. `swin--light--2.0mm--96--15703K-3D`) is shown as *swin · light · 2.0mm · 96 ·
15703K · 3D*. A model already downloaded (also under an earlier name, after the author renamed or moved it: the same
files with the same sizes) is recognised and not downloaded again. Every trained folder (with `dataset.json` and `plans.json`) becomes a model:
*organs · LungLobes (CT)*, *organs · LowDose-fivesets-HR (CT) · uldcthr_set_1_bones*, … When one task has several
trained folders (other trainer or plans) these are added to the name, e.g.
*lesions · FDGPanCancer (PETCT) · PET [4000epochs · PlannerResEncM_32 · 3d_fullres]*. `PET+CT` in the modality (or
the channels of `dataset.json`) gives a two-input model. nnU-Net folds count only with `checkpoint_final.pth`: a
fold still training is left out and the model runs with the finished folds. Scan again after uploading more.
On Google Drive for desktop the first run of a model downloads its checkpoints; keep the folder available offline to
avoid that. Script: `modeltree <folder>`.

### 📣 News and new models from the author

The model library shows the models in four tabs, **Segmentation**, **Image-to-image**, **Other** and **nnInteractive**, with their
status: *downloaded* (with its size and a 🗑 button that deletes it from this PC to free space; it can be downloaded
again), *local folder* (your own models, never deleted by ORCA-MI), *available* (⬇ Download) or *coming soon* (a
folder of the author's list that has no model yet). *edit links* shows the download links.

The **✋ nnInteractive** tab lists the official nnInteractive model, the fine-tuned nnInteractive models of the
author's list and your own (fine-tuned in the Train tab or added from a folder). Hover over a model to see how it was
trained and its final evaluation (Dice, lesions detected and false positives, original → fine-tuned). **⬇ Download**
first shows the licence: these models are made from the nnInteractive checkpoint (CC BY-NC-SA 4.0), so they are for
non-commercial use only. **✔ Use** makes a model the one nnInteractive runs (the *Model* list of the Segment tab; a
running nnInteractive restarts with it). **🗑** deletes a downloaded model, **✖** removes your own model from the list
(its folder stays on the disk).

At the first start ORCA-MI asks (after the statistics question) whether the user wants to be notified. With yes, it
checks the author's list at start and every 6 hours, sending only its version number, and shows new messages and
new AI models (*Help → News and updates*, where it can also be switched off or checked now). New models appear in the
model library; **Install** downloads their files from the author's Google Drive.

Script: `checkupdates [endpoint]`.

## 7. Export

### 🏥 Export to DICOM / PACS (images, SEG, RTSTRUCT, SR)

File → **🏥 Export to DICOM / PACS…** writes DICOM files that any PACS, viewer or treatment-planning system can
import. Choose the image; its active segmentation is exported with it.

**What can be written** (tick any):

| Item | File | Contents |
|---|---|---|
| Image series | `images/IM00001.dcm …` | the image as a new DICOM series (CT, PET, MR …), one file per slice |
| DICOM SEG | `SEG.dcm` | the segmentation as binary DICOM segments with names and colours |
| RTSTRUCT | `RTSTRUCT.dcm` | the segments as contours (exact voxel outlines) for radiotherapy systems and most PACS viewers |
| Measurement SR | `SR_measurements.dcm` | a structured report (TID 1500) with volume, mean, max, peak and TLG per segment |

**Attach to the original study** (when the image was loaded from DICOM): SEG, RTSTRUCT and SR join the original
study, use its frame of reference and point at the original slices. The PACS then shows them under the same
patient and study, on top of the original images. Otherwise a new study is created with the exported images.

**Header fields you can change:** patient name, patient ID, birth date, sex, accession number, study description,
study ID, referring physician, institution, operator, study date and time, and the series description and number
of every item. **Anonymize** sets the name to ANONYMOUS, a new ID, no birth date, and a new study.

**The values in the SR** come from the image chosen in *Statistics in segments → Values from* (e.g. the PET when
the lesions were drawn on the CT), in its units (SUVbw, Bq/mL, HU …).

**Into the PACS:** import the folder with the PACS's DICOM import (or drag it onto a DICOM node tool such as
the PACS upload page, Horos/OsiriX, or `storescu`). The files have been checked with the DICOM standard
validator (dicom-validator), pydicom, highdicom and rt-utils, and sent to a test PACS by DICOM C-STORE.

Python:
```python
v.export_dicom(r"D:\out\patient01", items=["seg", "rtstruct", "sr"], attach_to_original=True)
v.export_dicom(r"D:\out\anon", items=["images", "seg", "rtstruct", "sr"], anonymize=True,
               study_description="Lesion study", series_description="CT lesions", series_number=901)
```

> RTSTRUCT contours follow the voxel edges, so the volume is exact. Programs that rasterise contours by filling
> every pixel the outline touches (e.g. rt-utils) show the structure about one voxel larger.

### 📸 Export images & GIFs

Toolbar 📸, File → *Export images & GIFs*, or the Image tab. Tick what you want:

| Item | What you get |
|---|---|
| Whole layout as displayed | exactly the viewing area as on screen (2×2, several 3D views …) |
| Each view as displayed | one file per view |
| Axial / Coronal / Sagittal | clean, high-resolution renders of the active view's image with its fusion overlay, window, colormap and segmentations, correct aspect ratio |
| 3D views | every 3D view at high resolution with its current camera |
| 3D rotation GIF | all 3D views turning together, arranged as on screen |
| Axial / coronal / sagittal cine GIF | scroll through all slices |

A progress window shows what is being written (e.g. *file 2/3 · axial cine: drawing frame 190/312*), the time
left and *Cancel*.

Settings:
* **JPEG quality** (50–100 %) or lossless PNG.
* **Image size** (longest side).
* **GIF speed** (ms per frame), GIF size, frames per 3D turn, and slice step.
* **Output:** folder and file-name prefix.

Python: `v.export_images(folder, items=[...], quality=95, gif_delay_ms=60, ...)`.

### 🗂 DICOM curation & conversion (batch DICOM → NIfTI)

*Tools → 🗂 DICOM curation & conversion…* opens the *Yazdan DICOM* converter (dicom2nifti), built into ORCA-MI,
in its own window (tabs Convert, **Curate**, Rename, Options, dcm2niix, About). It converts whole folder trees: every subfolder with DICOM files becomes NIfTI files, with the
same names, files and log as the standalone dicom2nifti.exe (checked file by file on the test data: identical).

* **Convert:** drop folders or *Add folder*; results next to the DICOM files or in an output folder (the folder
  structure is copied); modalities CT / PET / NM-SPECT / MR or any; *Start conversion*, *Stop*, counters of images,
  geometry corrections, warnings and errors, coloured log, *Open output folder* / *Open log file*.
* **Outputs:** NIfTI (.nii.gz), PET also in **SUV**, Excel tables of the DICOM header (first slice, all slices,
  summary), `dicom2nifti_log.txt`.
* **Geometry:** tilted-gantry CT corrected, missing slices / uneven spacing resampled, NM whole-body options,
  enhanced multi-frame CT / MR, compressed DICOM (JPEG, JPEG-lossless, JPEG 2000, RLE). A multi-frame NM / SPECT
  whose *Spacing Between Slices* is negative (e.g. GE reconstructions, −2.46) is written with that spacing and
  direction (the frames go towards the feet), so it lies on its CT as in 3D Slicer (it used to get 1 mm, upwards).
* **Duplicate files:** a folder holding the same DICOM instance twice (same SOP Instance UID, e.g. a study copied
  twice into one folder) is read once; the log says how many copies were ignored. ORCA-MI's own DICOM reader does the
  same (the copies used to become extra slices or time frames: wrong volumes).
* **Appearance:** the window uses ORCA-MI's zoom, text sizes and spacing (View → Appearance) with its own colours.
* **Theme** (bottom of the sidebar): **☀ Light** or **🌙 Dark** for this window, whatever ORCA-MI uses; saved at once.
  Until one is chosen the window opens in ORCA-MI's current theme.
* **Scale** (bottom of the sidebar): **Auto** fits the window to the screen it is on (larger on big screens, smaller
  on laptops; the window is resized to match), or **−** / **+** in steps of 5 % (50–200 %). Text, buttons and the
  window size follow; the choice is saved (`scale = auto` or e.g. `scale = 0.9` in the settings file).
* **Rename:** clean file and folder names (é, ^, spaces, long names) before converting, with preview and undo.
* **dcm2niix:** optionally also run dcm2niix (e.g. for 4D series, or JPEG-LS files the converter cannot decode).
* **Options** are saved in `%APPDATA%\ORCA-MI\dicom2nifti_settings.ini` (same format as the standalone program).
* **File names** (Options → *File names*): the name is built from DICOM fields in the order you choose, e.g. the
  default *modality--study--series--0001--0000*. Fields: modality, study description, study date, study time,
  series description, acquisition date, acquisition time, patient age, patient sex, scanner model and reconstruction
  algorithm (*Reconstruction Method*, else the CT *Convolution Kernel*).
  * **Drag** the boxes to change the order; click or drag a field from *Available* to add it; **right-click** a box
    (*Remove from the name*) or drag it back to *Available* to remove it.
  * **Double-click** a box to set the number of letters it keeps (*all* = the whole value); the number shows on
    the box.
  * **Separator** between the parts (`--`, `_`, `-`, `.` or your own). The *Example* shows the result.
  * The series and direction numbers always end the name (they keep names unique). Missing values give *na*
    (*studyunknown* / *seriesunknown* for the descriptions, as before). *↺ default* gives the original names back.

Script: `dicomconvwindow`, `dicomconvert D:\study;E:\other|out=D:\nifti|modalities=ct,pt|workers=8`; for one run
with other names add e.g. `|pattern=series:6,acquisition_date:0,sex:1|sep=_` (field:letters, 0 = all; fields
`modality, study, study_date, study_time, series, acquisition_date, acquisition_time, age, sex, scanner, recon`;
times are written without the fraction of seconds, e.g. `081502`).

### 🗃 Curate a DICOM database

*Tools → 🗃 Curate a DICOM database…* (the **Curate** tab of the window above) organizes and converts data exported
from PACS (e.g. syngo.via): every file is read (header only, in parallel) and put into folders built from its DICOM
header, e.g. `DOE-JOHN--ANON54121 \ 20181115--Tumor-Imaging \ 2--C2S1D0-AbdRoutine-3-0-I31s-3`.

* **DICOM folders:** type or paste a folder address (Enter or *Add*), *Browse*, drop folders on the window, *Same as
  Convert tab*, or *Patient database (n)* = every folder of ORCA-MI's patient database. Every sub-folder is read.
* **Folder structure:**
  * **Build from DICOM tags:** one row per folder level, top first. Each level holds one or more tags (*+ tag* menu,
    or *Other tag*: any keyword such as `ProtocolName`, or a number such as `0018,1030`); several tags in one level are
    joined by the **separator** (default `--`). ↑ / ↓ move a level, ✕ removes a tag or a level, *↺ Default* =
    `PatientName--PatientID / StudyDate--StudyDescription / SeriesNumber--SeriesDescription`.
    Values are cleaned like on the Rename tab (é → e, ^ and spaces → -, at most 64 letters); empty = `unknown`.
    Two different values that give the same folder name (e.g. *Müller* and *Muller*) get `_2`, with a warning.
  * **Keep the folders as they are:** the converter's own behaviour: no DICOM file is copied or moved, NIfTI + Excel
    are written next to the DICOM files, in the same folders (as *Convert* with *Next to DICOM files*).
* **Where:** *Another folder* (the output folder; several inputs are merged into one tree) or *In place* (the tree is
  built inside each input folder).
* **DICOM files:** **Copy** (originals untouched; only to another folder), **Move** (old empty folders are removed) or
  **Leave where they are** (only NIfTI + Excel are written in the new folders).
* **Write NIfTI (+ Excel):** each new folder also gets the converter's NIfTI, SUV and Excel files, with the Convert
  tab's modalities and the Options tab (Excel, SUV, file names, workers): the files are identical to the Convert tab's.
* **Rename DICOM files** `<Modality>_<InstanceNumber>.dcm` (otherwise the names are kept; a name already taken in a
  folder gets `_2`).
* **Duplicates** (same SOP Instance UID) are written once; with Move the extra copies stay where they were.
* **Parallel:** headers are read on every core; *Copy / move workers* (Auto = 8, 4 on network paths `\\server\…`);
  NIfTI uses the converter's workers.
* **Preview** first: the folder tree with the number of files, and counts of patients, studies, series, files,
  duplicates and name clashes. **Run** works only on a preview of the current options. *Stop* stops after the files in
  progress.
* **Files written:** `curate_log.csv` (action, old, new: one line per copied / moved file), `curate_index.csv` (folders
  and their number of files), `curate_log.txt` (the log). **Undo last curation** moves the moved files back and deletes
  the copied ones (NIfTI and Excel files are kept).
* Not available in the trial (like the converter).

Script: `dicomcurate D:\export|out=D:\curated|levels=PatientName,PatientID/StudyDate,StudyDescription/SeriesNumber,SeriesDescription|sep=--|dicom=copy|nifti=1`
(`dicom=move|leave`, `inplace`, `keep`, `rename=1`, `workers=8`, `preview` = counts and tree only; `,` = same folder,
`/` = next level), `dicomcurateundo D:\curated`, `curatewindow [<folder>][|out=<folder>][|preview]`.

### 🎞 Picture viewer (GIF, PNG, JPEG)

Exported GIFs (cine and rotation) are pictures, not images for analysis: ORCA-MI shows them in its **picture viewer**,
a window of its own that also appears in session recordings. It opens with File → **🎞 View GIF / pictures…** (GIF,
PNG, JPEG, BMP), File → Open image files (GIFs go to the viewer, the other files load as images as before), drag and
drop of a .gif, and after 📸 Export when *Show the GIFs in ORCA-MI's picture viewer when done* is ticked (default).

* **▶ Play / ⏸ Pause** (Space), the **frame slider** (← → step one frame), **speed** 0.25× … 4×, **Loop**.
* **Fit** (the window) or **100 %** with a zoom slider; the size in pixels and the GIF's length are shown.
* Several pictures: **◀ ▶** go from one to the next; *✖ Close this picture*; *🗁 Folder* opens its folder.

PNG / JPEG still open as images (File → Open image files); use *🎞 View GIF / pictures…* to see them as pictures.
Scripts: `viewpicture <file>`, `picture next|prev|play|pause|frame <n>|speed <x>|close|status`.

### ⏺ Record a session (training video)

Tools → **⏺ Record session (training video)…** (or ⏺ in the toolbar's Output group) records ORCA-MI's own windows
into one **MP4** video (H.264 picture, AAC sound): the main window and every window ORCA-MI opens (popped-out tabs
and panels, NEMA, cardiac splash, Brain EIR, DICOM conversion). Each window is shown with its real size and place
(one scale for all, so the size ratios are kept); other programs and the desktop are never recorded. The mouse
pointer and a ring at every click are drawn in the video.

* **Quality**: *Low* (1280 px wide, 8 frames/s, voice 96 kbit/s, ≈ 19 MB per minute), *Standard* (Full HD,
  12 frames/s, voice 128 kbit/s, ≈ 46 MB per minute, the default), *High* (2560 px wide, 20 frames/s, ≈ 92 MB per
  minute) or *Ultra* (4K: 3840 px wide, 30 frames/s, ≈ 226 MB per minute, for 4K screens and a fast computer).
  High and Ultra always record the best sound Windows' encoder makes (AAC 192 kbit/s stereo, 48 kHz). The dialog
  shows the exact size.
* **Mouse pointer**: *Arrow* (the usual pointer, the default), *Circle* (a small ring) or *None*; *Rings at clicks*
  (yellow rings where you click) can be turned off.
* **⌨ Show the keys I press** (on by default): shortcuts (Ctrl + Z, Esc, arrows, F11, the view keys …) appear for 2 s
  *at the bottom* (default) or *at the top* of the window they were pressed in, on the screen and in the video. Text typed into a field is never
  shown (only shortcuts with Ctrl / Alt there).
* **Several windows**: every ORCA-MI window (main window, popped-out tabs and panels, NEMA IEC …) is shown side by
  side with its real size and place, the one you used last on top. The picture is kept steady: it zooms out at once
  when a window moves out of it, and zooms back in only after 2 s, smoothly. Windows of their own (NEMA IEC, DICOM
  conversion) keep being recorded even when nothing moves in them.
* **🔍 Follow the window I work in** (off by default): when the mouse stays 3 s in one window, the video shows that
  window alone, full size, until the mouse stays 3 s in another one.
* **Microphone** (🎙 *Record my voice*): off = the microphone is never opened; on = your voice is recorded and can
  be muted / unmuted during the recording. If Windows blocks it (Settings → Privacy → Microphone → let desktop apps
  use it), the video is recorded without sound and the bar says so. With several microphones, choose one in the
  list under it (*Windows default microphone* by default; ↻ lists the devices again).
* **Camera** (📷 *Include my camera*, off by default): your camera picture is drawn in a corner of the video
  (picture-in-picture), so the video stays one file that plays everywhere. Choose the camera when there are several,
  the corner (↖ ↗ ↙ ↘, bottom right by default), the size (small, medium, large: 18, 25 or 33 % of the video's height)
  and round or rectangle, and the **frame colour** around the picture (white, ORCA blue, yellow, orange, red, green,
  black or any colour); all of these can be changed during the recording too (⚙ on the recording bar).
  **✥ Move camera** (next to ⏹ Stop on the recording bar): the camera's box on the screen can then be dragged
  anywhere; press **✥ Done** when it is in place. The place is kept for the next recordings; click a corner to put
  it back in a corner.
  **Show where the camera is on the screen** (on by default): while recording, a dashed yellow box *📷 camera* on
  ORCA-MI's windows marks the part the camera picture covers in the video, so you know which clicks or information
  viewers cannot see; it lies under the camera picture, so the video does not show it.
  During the recording, 📷 on the bar hides and shows the camera (hidden: that corner shows the windows).
* **🏷 Watermark** (off by default): a text drawn in every frame of the video, e.g. *ORCA-MI · PET/CT fusion in
  2 minutes* for a YouTube channel: at the top (default) or the bottom, left (default), centre or right, small, medium
  or large, white letters on a translucent dark box. It gets its own band above (or below) the windows, so it never
  covers ORCA-MI's menus or toolbar. It can be changed during the recording (⚙ on the bar).
  Off = the camera is never opened. If the camera does not start (used by Teams, Zoom … or blocked in Settings →
  Privacy → Camera), the video is recorded without it and the bar says why.
  **Virtual cameras** (NVIDIA Broadcast with background blur or replacement, OBS, Logi Capture …) are in the camera
  list too, as in Zoom; their program must be running while you record.
* **Hide the patient name and ID on the views while recording** (off by default). You are responsible for
  anonymizing the images (see 🕶 Anonymize DICOM below); a note says so and must be acknowledged once.
* **Folder**: Videos\ORCA-MI recordings by default; file name `ORCA-MI session <date time>.mp4`. Recordings stay on
  this computer: ORCA-MI never uploads them and never puts them in bug reports.

While recording, a bar on top of the main window shows **● REC** and the time, the **quality**: the chosen size and
frames per second next to the frames really captured (green: as chosen, amber / red: the computer is busy, e.g. 3D or
AI; choose *Low* next time), the microphone (🎙 on / muted with its level), **⏸ Pause / ▶ Resume** (paused time is
not in the video) and **⏹ Stop**, the file size and **⚙** (pointer, click rings, keys, follow, camera place, watermark: changes apply at once;
it reads *🔍 one window* while a window is shown alone). When it is saved, a message gives the file.
Script: `record start|quality=low|standard|high|ultra|mic=0|1|micdev=<part of name>|cam=0|1|camdev=<part of name>|corner=0-3|camsize=0-2|round=0|1|pointer=arrow|circle|none|clicks=0|1|keys=0|1|keystop=0|1|follow=0|1|cambox=0|1|camcolor=r,g,b|mark=<text>|marktop=0|1|markalign=0-2|marksize=0-2|folder=…|hide=0|1`,
`record pause|resume|stop|mic 0|1|cam 0|1|follow 0|1|camplace <corner 0-3> <size 0-2> <round 0|1>|cammove 0|1|campos <x> <y>|mark <text>|devices|status`.
On Windows "N" editions the video encoder needs the free *Media Feature Pack*.

### 🕶 Anonymize DICOM

Tools → **🕶 Anonymize DICOM…** writes anonymized copies of DICOM files; the original files are never changed.

1. **Source**: add folders, or **🗄 The whole patient database** (every folder of File → Patient database), then
   **🔍 Find the patients**: the files are read and grouped by patient.
2. **Patients**: every patient gets a sample name and ID (`ANON^001` / `ANON001`, `ANON^002` …; change the prefix and
   press *↻ Number again*, or type any name / ID per patient). The original names are hidden (● ● ●): **👁 Show
   original names…** asks for your approval first.
3. **What is changed**: patient name and ID always; the **birth date** kept, year only (YYYY0101, the default) or
   removed; ticked fields emptied (other IDs and names, address, telephone, comments, accession number,
   institution, department, station, physicians, operators …); **private tags** removed (default). Weight, height,
   sex, age and the dates stay (SUV, dose and decay correction need them).
   **Replace the UIDs** is off by default: studies, series and the links between CT, PET, RTSTRUCT, SEG stay exactly
   as they are. On: every Study, Series, SOP instance and Frame of reference UID gets a new one, the same everywhere
   in the run, references inside RTSTRUCT / SEG / registrations included, so the images still belong together
   (SOP Class UIDs and transfer syntaxes never change).
4. **Output**: a new folder (not inside a source folder) with `<new ID>/<study date>_study<n>/<series>_<modality>/00001.dcm`
   (no names in the folder names), and the **decode file**: JSON always, CSV and Excel if ticked, with new ID, new
   name, original ID, original name, original birth date (and the old → new Study / Series UIDs when they were
   replaced). Keep the decode file apart from the anonymized images.

**🔑 Decode file**: *📂 Load a decode file…* (.json, .csv or .xlsx) lists its patients with the original names hidden
and marks the ones whose anonymized images are loaded; **👁 Show original names…** shows them after your approval
(it warns when a recording is running). Scripts: `anonymize src=<folder>|out=<folder>|prefix=…|uids=0|1|private=0|1|birth=keep|year|remove|decode=<file>|csv=0|1|xlsx=0|1`,
`anondecode <file>` (counts only: the log never holds names).

## 8. Sessions, workspaces and reader studies

### ♻ Autosave, crash recovery and workspaces

**Autosave:** every 2 minutes (when something changed) ORCA-MI saves the session: the images (by their file or
DICOM folder), window and colours, segmentations (as NIfTI), annotations, measurements, registrations, layout and
viewports. Images without a file (crops, AI results, resampled images) are saved as well. Saving runs in the
background and only writes segmentations that changed.

**After a crash** (or if the PC was switched off) the next start asks **Restore the last session?** with the time
and the images. *Restore* brings everything back; *Discard* deletes it; *Later* keeps it for File → *Restore
session*.

ORCA-MI also autosaves just before nnInteractive starts (loading the model needs much memory).

**Crash logs:** an internal error is written to `%APPDATA%\ORCA-MI\crash_logs\crash-<time>.txt` (message,
place in the program, backtrace; no image data). An error in the interface is caught: the program keeps running,
autosaves and shows the log. If ORCA-MI closed, the next start shows the log of that run. Help → *⚠ Crash logs…*
opens the folder; please send the log to the author.

**File → ♻ Restore session** lists the last session (saved on a normal exit too) and any unrestored session, and
sets the autosave interval (0 = off) and *Autosave now*. Reading sessions are never autosaved (blinding).

**Save before closing.** When you close ORCA-MI with segmentations that were created or changed (or annotations,
measurements, scores) and not saved, it asks first: *Save segmentations (NIfTI)…* (every changed segmentation
into one folder, with its label names), *Save workspace…*, *Close without saving* or *Cancel*. The result of an **AI
model** counts as not saved until you save it — an nnU-Net segmentation, and a new image made by an image-to-image
model (it exists only in a temporary folder until then). Exporting a segmentation or an image, *Save images…*,
saving a workspace or exporting to DICOM counts as saved. Script / Python: `unsaved` (lists what closing would ask
about).

Workspaces are saved as **`.orca`** files (older `.json` workspaces still open). The installer registers `.orca` with ORCA-MI, so a **double-click on a `.orca` file opens it in ORCA-MI** (portable copy: right-click the file → Open with → choose ORCA-MI.exe, *Always*).

**Workspaces:** File → *Save workspace…* saves the same information to a file you choose, with the segmentations in
the `<name>_files` folder next to it; *Open workspace…* restores it on any PC that can reach the images. You can
also **drag a saved workspace (.orca, or an older .json) onto the ORCA-MI window** (or open it with ORCA-MI): it opens as a workspace.
Other .json files (transforms, scoring databases, libraries) are not taken for workspaces.
Saving with copies of every image runs in the background with a progress bar (the window stays usable).

**File → 🗂 Save workspace with copies of every image…** is self-contained: a NIfTI copy of every loaded image (in its
data type), every segmentation and every saved registration (transform, Demons field) goes into `<name>_files`, so
it opens without the original files (another computer, files moved or deleted).

**💾 Save images, segmentations, registrations…** (File menu, or the 🛒 button of the toolbar): tick images, their
segmentations and the saved registrations, choose a folder and a format (NIfTI .nii.gz / .nii, NRRD, MetaImage) and
save them together; optionally also a self-contained workspace. Segmentations get a `.labels.json` with the label
names; registrations a JSON with the transform (fixed world → moving world) and the Demons field as a 3-frame image.
**🛒 Export basket:** right-click an image → *Add to the export basket* to collect images while you work; the toolbar's
🛒 shows how many, and File → *Export basket* opens the dialog with them ticked.

Data are kept in `%APPDATA%\ORCA-MI\autosave`. Script / Python: `saveworkspace <file>`, `loadworkspace
<file>`, `saveworkspacecopies <file>`, `basket add|remove <i>`, `basket list|clear`, `basket save <folder>`,
`autosave now`, `autosave 5`; `v.save_workspace(path)`, `v.load_workspace(path)`.

### Reading sessions (physician scoring)

Give each physician **ORCA-MI.exe + one session file**. They open it (Scores tab → *Reading session*,
Tools → *Open reading session…*, or `ORCA-MI.exe --session=file.json`), score case by case and press
**Save & next**; every case is saved immediately, so they can stop and resume later.

* **Session file formats:** JSON (complete), CSV / TSV, or Excel (`.xlsx`, `.xls`, `.ods`). Table columns:
  `path` (required: image file or DICOM folder), `id`, `overlay`, `seg`, `window`, `layout`, and in the first row
  `reader`, `title`, `instructions`, `output_mode` (`same_folder` / `folder`), `output_folder`, `pattern`,
  `randomize`, `blind`, `criteria` (`Noise; Sharpness; Artifacts` → 1–5 scales). An Excel file can have a
  `criteria` sheet with `name, description, kind (likert/slider/yesno/choice/text), min, max, options, required`.
* **Where results go:** next to each image or in one folder, named by a pattern with `{case} {reader} {title}
  {stem} {index} {date} {patient} {config}`. Each case is a JSON file (scores, comments, annotations, reading
  time) and `<title>_<reader>_summary.csv` is rewritten after every case.
* **Create session files:** Scores tab → *Create session files…*: add images, choose readers (one file per
  reader), output, order and blinding, then save JSON or CSV.

### Scoring a database (patients × configurations)

Tools → **📋 Score a database…** for a folder laid out as:

```
database/
  patient_01/
    reference/          image-1-pet.nii.gz  image-2-ct.nii.gz
    recon_A/            image-1-pet.nii.gz  image-2-ct.nii.gz  protocol.pdf
    recon_B/            ...
    history.pdf         (documents for every configuration of this patient)
  patient_02/ ...
```

* Each configuration folder can hold any number of images (sorted naturally: image-1, image-2, … image-10) and
  DICOM sub-folders. A PET/SPECT + CT/MR pair is shown fused (option).
* **Reference:** pick a configuration as the reference. It is shown on the top/left as **★ REFERENCE** next to
  every other configuration of the same patient, with linked slices and zoom. The criteria become *Similarity to
  reference*, *Confidence*, *Differences found* and *Comments*; mark the differing regions with 📌 Annotate (A),
  and those points are saved with the scores.
* **Blinding:** configuration folder names are hidden (images appear as *Case N · PET*), as are file paths in
  the Info tab and header view and the recent-files list. Documents are listed as *Document 1, 2 …* and open in
  their own window (system PDF viewer).
* **Order:** *patient by patient, configurations random* (optionally random patient order), *fully random*, or
  *in order*. The order is reproducible per reader.
* **Comment and description of the task:** a short **comment** (e.g. *Round 2 – blinded re-read*) and a longer
  **description** (what to do, criteria, contact). Both are saved with the database and in every reader's session;
  the comment is shown on top of the scoring panel during the reading, the description when the reader clicks
  **ℹ description**, and the comment is added to the names of the shortcuts (`Dr A - Round 2_ blinded re-read.orcascore`,
  Desktop: `ORCA-MI scoring - <title> - <comment> - Dr A`).
* **Readers:** one row per reader — name, description (experience or organization), an optional e-mail and
  **Desktop** (a shortcut for this reader on this computer's Desktop); ➕ *Add reader* / 🗑. Each reader gets a
  session and a shortcut. **Your name** (type it, or pick a reader) is the reader who starts now: *▶ Start scoring as
  <your name>* (a new name is added to the readers).
* **What the reader sees:** the **layout** — without a reference *MPR* (axial, sagittal, coronal + 3D; the default)
  or *one view*; with a reference *dual MPR* (reference MPR on the left, image MPR on the right; the default),
  *MPR of the image only*, *2 × 2* (axial and coronal of the reference and of the image) or *side by side*. When the
  reference itself is scored too, it has nothing next to it and is shown in MPR — the **colormaps** of PET / SPECT
  (default Hot iron) and of CT / MR (default Grayscale) — the **base image** (CT / MR with PET / SPECT fused on it,
  PET / SPECT with CT / MR fused on it, or PET / SPECT alone) and, in the MPR layouts, the image of the **3D view**.
* **Questions:** *✏ Edit the questions* edits the questions of this database (names, descriptions, scales, choices,
  required); start from the reference questions or from your Scores template. They are saved with the database, so
  every reader answers the same questions.
* **Start scoring** right away, or **Save the set-up, sessions and shortcuts**. Saved in the database folder:
  `scoredb.json` (the set-up: title, reference, order, blinding, questions, view, readers), `session_<reader>.json`
  for each reader, and **shortcut files** `<reader>[ - <comment>].orcascore` plus `Everyone - choose your name[ - <comment>].orcascore`
  (an older shortcut of the same reader is replaced when the comment changes). Scores go
  to `database/_scores/<patient>/<config>_<reader>.json` plus a summary CSV. Opening the dialog on a database set
  up before reloads its set-up.
* **Shortcuts for the readers:** give each physician the database folder. A reader double-clicks *their*
  `.orcascore` file (with the installer version of ORCA-MI) or drops it onto ORCA-MI, and their session opens. The
  *Everyone* shortcut, `scoredb.json` or any `session_<reader>.json` dropped onto ORCA-MI asks **who is scoring**:
  pick your name or type a new one; a new reader gets their own session, built from the saved set-up, and their own
  shortcut file. Tick *Put a shortcut for me on the Desktop* (or, in the dialog, *also on this Desktop*) for a
  Desktop icon; a Desktop shortcut can also be dropped onto ORCA-MI. The paths are relative, so the shortcut files
  keep working when the database is copied to another computer (Desktop icons point to where the database was).
* **Reviewing the results:** Results tab → *Load results folder…* (`database/_scores`) → **📌 Cases and
  annotations**: every saved case (reader · patient · configuration · number of marks), optionally only those with
  annotations. Click one: its images open in the database's layout with the reader's marks drawn on them, next to
  their answers and comments; click a mark to go to it; ◀ Previous / Next ▶ walk through the cases.
* **While reading:** each new case starts with the normal tool (the 📌 annotation tool is switched off), and the next
  case is read from the disk in the background, so *Save & next* is quick even on a slow (HDD) drive.
* **Marks in 3D:** annotations are also drawn in the 3D views (everywhere in ORCA-MI); the **📌 Marks** box in the 3D
  view's bar (shown when there are marks) turns them on or off.
* **Sharing the database:** copy or share the database folder (network drive, USB disk, cloud folder). Everything
  a reader needs is inside it — the set-up, their session (relative paths) and their shortcut — so they only
  double-click their shortcut in the folder; nothing to install or set up besides ORCA-MI with a licence.
* Script / Python: `scoredb <root>|reference=reference|reader=Dr A,Dr B|order=patient|layout=dualmpr|base=functional|view3d=anatomical|comment=…|description=…|save=1`,
  `scoring <file>`, `scoringpick <reader>`, `sessionnext`, `sessionend`, `resultsload <folder>`, `resultsshow <k>`.

### 🗂 Segmenting a database (studies × observers)

Tools → **🗂 Segment a database…** lets physicians segment every study of a folder, each under their own name:

```
database/
  study_01/      image-1-ct.nii.gz  image-2-pet.nii.gz      (files or DICOM folders)
  study_02/ ...
  patient_07/
    visit_1/     ...                                       (root / patient / study also works)
```

* **Comment and description of the task**, as for scoring: the comment is shown on top of the segmentation panel
  and added to the shortcut names, the description when the reader clicks **ℹ description**; both are saved in
  `segdb.json`.
* **Readers:** one row per reader — name, description, e-mail and **Desktop** (a shortcut on this computer's
  Desktop); ➕ *Add reader* / 🗑. *💾 Save the set-up and the readers' shortcuts* writes the set-up and a shortcut
  for each reader plus one for everyone; *▶ Start segmenting* does it too and starts. **Your user name** — type it or
  *pick a reader* — is the reader who starts now (a new name joins the readers).
* **Your user name** identifies the observer (required). Results go to
  `database/_segmentations/<study>/<user>.nii.gz` with `<user>.json` (observer, labels, time spent, volume per
  label) and `database/_segmentations/summary_<user>.csv` (one row per study, ml and voxels per label).
* **Continue later:** start again with the same user name; the studies you have done are skipped (another observer
  starts at the first study). ◀ *Previous* or the study list reopens a done study with your segmentation, to edit it.
* **Labels:** value, name and colour of each label (e.g. 1 *Lesion soft tissue* red, 2 *Lesion bone* green,
  3 *Reference* blue); ➕ adds one. The set-up (labels, options) is saved in `_segmentations/segdb.json` and read
  back when the next observer opens the database, so everybody uses the same labels.
* **Segment on:** the image whose name contains this text (e.g. `pet`) gets the segmentation; empty = the first
  image. It can be painted on any view of the study.
* **Anonymise** (on by default): patient names, IDs and file paths are hidden; studies appear as *Study 1, 2 …*.
* **Start from:**
  * *an empty segmentation*;
  * *another observer's segmentation*, to refine it (e.g. a senior correcting a junior). Only the studies that
    observer has saved are offered; when they are all done ORCA-MI says how many the other observer has not
    segmented yet. The result is saved under your own name (the other observer's file is not changed);
  * *an nnU-Net model* (from the AI tab), set up as in the AI tab: **Model**, **Configuration** (the model's
    configurations found beside its folder: 2d, 3d_fullres, 3d_lowres …, or the AI tab's), **Speed** (🐇 Ultra fast,
    ⚡ Fast, ⚖ Balanced, 🎯 Accurate, as in the AI tab), **Device**, and a **Reader name** (e.g. `nnunet-Liver-3d_fullres-fast`,
    named from the choices until you type one). The model is a **reader**: its segmentations are saved as
    `_segmentations/<study>/<reader name>.nii.gz` with a `<reader name>.json` (model, configuration, speed), so other
    readers can also *refine* them like another observer's. *Earlier* lists the nnU-Net readers of the database.
    It segments the studies you have not done **in the background**, the next ones first (the first study alone, so
    it is ready soon); **▶ Run on every study now** segments every study before anyone starts (e.g. before sharing
    the folder). A study opens with its prediction; if it is not ready yet the panel says *Please wait: nnU-Net is
    segmenting this study…* and loads it when it arrives (if you have started drawing, a button offers to load it
    instead). **Predictions already in the folder are used without the model**: a reviewer whose computer does not
    have it starts from them at once (studies without one start empty, with a message). Older databases keep their
    `_segmentations/<study>/nnunet__<model>.nii.gz` files; progress in `nnunet_<model>_progress.log`.
    Input channels are matched to the model's channel names (e.g. CT, PET) by file name, DICOM is converted and
    further channels are resampled onto the first. A warning shows when little GPU memory is free.
* **Display:** *PET / SPECT fused on its CT / MR*, *side by side*, or *only the image to segment*.
* **Layout and colormaps** (the reader's view, set once for everyone in `segdb.json`): *Layout* MPR (axial, sagittal,
  coronal + 3D, the default), one axial view, or automatic; *Main image* the image to segment with the other one
  fused on it (default), CT / MR under, PET / SPECT under, or PET / SPECT alone; *3D view* PET / SPECT or CT / MR;
  *Colormap PET / SPECT* (default Hot iron) and *Colormap CT / MR* (default Grayscale). Script: `segdb …|layout=mpr|
  base=segmented|view3d=functional|cmapf=Hot iron|cmapa=Grayscale`.
* **Tools:** every tool of the Segment tab works while segmenting a database (brushes, thresholds, region growing,
  morphology, nnInteractive …); the database panel sits on top of the tab.
* **✔ Normal scan — save empty & next:** nothing to segment in this study: an empty segmentation is saved, marked
  *normal* (`"normal": true` in `<user>.json`, column *normal* = yes in the summary CSV), and the next study opens. If
  something is already drawn, ORCA-MI asks before clearing it.
* **Shortcuts:** `<reader> - segmentation[ - <comment>].orcaseg` for every reader and `Everyone - segmentation
  (choose your name)[ - <comment>].orcaseg`, which asks who is segmenting (with the readers' descriptions, the
  comment and the description), in the database folder; on the Desktop as ticked (`ORCA-MI segmentation - <title> -
  <comment> - <reader>`). Double-click a shortcut (installer version) or drop it onto ORCA-MI to continue as that
  reader, from the same starting point.
* **Sharing the database:** share the folder (network drive, USB disk, cloud folder): the set-up, the shortcuts (no
  paths inside: they work wherever the folder is) and the nnU-Net predictions travel with it. The reviewer only
  double-clicks their shortcut; nothing else to set up (ORCA-MI with a licence; no AI model needed when the
  predictions are in the folder).
* **Earlier segmentations to refine** (e.g. a public dataset or an older manual segmentation): when preparing the
  database, save each study's label map as `_segmentations/<study>/<name>.nii.gz` with a small `<name>.json`
  (`{"user": "<name>", "study": "<study>", "start_from": "imported"}`); the example script
  `07_prepare_copy_segment_score_database.py` does it (`PRIOR_NAME`, `PRIOR_SEGMENTATIONS`). The readers then
  *start from* that observer and save their corrected version under their own name.
* **Studies found:** after a scan, the list shows every study with its images, their modality (from the DICOM header
  of a folder, else from the file name), the image that is segmented (✏ *Segment on*) and, with an nnU-Net start, the
  model input each image goes to (*→ input 0000 CT*). Studies that cannot be given to the model are flagged.
* **Model inputs** (nnU-Net start): for every input channel of the model (names from its dataset.json, e.g.
  *0000 CT*, *0001 PET*) choose the study image by name (a list of the file names found, with the number of studies)
  or type a part of the name; *auto* matches the channel name. Saved in the database set-up for every observer.
* **Score each study too:** the criteria (from the Scores tab template, or from the database set-up) are shown
  under the labels and saved with the segmentation; required ones (*) must be answered before *Save & next*.
* **⏸ Pause** (optional, ticked when you define the database: *Pause: show a Pause button to the readers*; for both
  *Segment a database* and *Score a database*): the reader's panel gets **⏸ Pause**; while paused a banner shows
  in the middle of the window and the clock stops, **▶ Resume** goes on. The paused time is never counted in the
  time spent on the study / case (e.g. a break with ORCA-MI left open).
* **Times and place:** each `<user>.json` keeps the local times the study was opened and saved (with the UTC
  offset), the time spent (all visits), the start point, the scores, and the computer (name, Windows user, OS, CPU
  cores, GPU, time zone, screen). `progress_<user>.log` gets a tqdm-like line per study:
  `time | [  12/120] 10.0% |██░░…| study | this 03:12 | mean 02:50/item | ETA 5:06:00`. Reading sessions (scoring)
  save the same information and a `<title>_<reader>_progress.log` next to their summary.
* Example script: `examples/05_segment_and_score_database.py` builds a segmentation and a scoring database from
  your files (or a synthetic demo), writes the shared set-up and starts a junior, a senior and an nnU-Net session.
* The panel at the top of the Segment tab shows the progress, the labels (click one to paint with it),
  **💾 Save & next** (saves, also an empty result = no finding, and opens the next study you have not done),
  *Skip*, *Save* and *End*. *Previous*, the study list and *End* save the study only if you changed it.
* Script / Python: `segdb <root>|user=Dr A|anon=1|on=pet|labels=1:Lesion soft tissue:#ff0000,2:Lesion bone:#00ff00`
  (`|score=1`, `|from=Dr Junior`, `|nnunet=<model name>`, `|channels=ct,pet`, `|view=fused|side|single`), `segdbnext`, `segdbskip`, `segdbgo <n>`, `segdbsave`,
  `segdbscore Image quality=4|Confidence=3`, `segdbend`, `segdbinfo`.

**🧠 Prepare nnU-Net training from a segmented database** (Tools menu, or the button at the bottom of the *Segment
a database* window) turns the saved segmentations into an nnU-Net v2 raw dataset, to train your own model:

* choose the **segmented database**, the **nnUNet_raw folder** (filled from the `nnUNet_raw` environment variable
  when set), a **dataset name** and a **number** (three digits: the folder is `Dataset012_CardiacLV`; the next free
  number is proposed, a number already used by another dataset is refused);
* **Labels:** from the database's label description, renumbered 1, 2, 3 … in the order of their values (nnU-Net
  needs consecutive labels; the window shows each database value → nnU-Net value). Values not in the description
  become background;
* **Segmentations of** (when several people segmented the database):
  * *every reader*: each reader's segmentation of a study is a case of its own (earlier combinations left out);
  * *the readers ticked below*: only the readers you choose (people and nnU-Net readers), each one a case;
  * *a combination: majority vote of the readers ticked below*: one case per study. Per voxel, a label is kept
    where more than half of the readers gave it (two readers: both must agree; three: two of three), else
    background. Give the combination a name (default *Majority vote*): it is saved in the database as a reader of
    its own (`_segmentations/<study>/<name>.nii.gz`, its `.json` says which readers it comes from), so it shows in
    the list, marked *majority vote*, and can be chosen again or compared later. The name of a person is refused
    (their work would be overwritten); *only the studies segmented by every ticked reader* (default on) leaves
    out the studies some readers have not done (else the vote is among the readers who did them);
  * optionally leave out the studies saved as *Normal scan*;
* **Input channels:** each channel is the study image whose name contains the text you type (empty = the image
  that was segmented), put on the label map's grid (linear interpolation); the channel name goes into
  `dataset.json` (`CT` = nnU-Net's CT normalisation, other names z-score). The window shows what the first study
  gives;
* written: `imagesTr/<Name>_001_0000.nii.gz` …, `labelsTr/<Name>_001.nii.gz`, `dataset.json`, `cases.csv` (case →
  study, reader, labels present), `splits_final.json` (5 folds; all cases of a patient / study in the same fold:
  copy it to `nnUNet_preprocessed/Dataset012_CardiacLV/` before training) and `README_ORCA-MI.txt` with the
  commands (`nnUNetv2_plan_and_preprocess -d 12 --verify_dataset_integrity`, `nnUNetv2_train 12 3d_fullres 0`).
  It runs in the background (Jobs); studies that cannot be read are skipped and listed.
* Script: `nnprep root=<database>|out=<nnUNet_raw>|name=CardiacLV|id=12|readers=Dr A,Dr B|channels=:PET,ct:CT|skipnormal=1|overwrite=1`
  (`|combine=Consensus` = majority vote of the `readers=` (or of every reader), `|allonly=0` = also studies not done by all)
  (`window=1` opens the window instead) → `[nnprep] done cases=… dir=…`.

### 📊 Results tab

The Results tab shows the **scores of reading studies** only: the answers every reader gave per case (Scores tab
during a reading session). Segmentation, AI, statistics and training results are in their own tabs. It stays empty
until you press *From current session* during a reading session (Tools → 📂 Open reading session…) or
*📂 Load results folder…*.

Load the results of the current session or of a whole folder (for example `database/_scores` with every reader).
Choose a criterion and a reader, group by configuration / reader / patient: bar chart of mean ± SD, table (n, mean,
SD, median, marks per case) and a patient × configuration heat map. *Export all results* writes one CSV with every
case and criterion. During a blinded session the Results tab stays hidden.

## 9. Automation: scripts and Python

### Automation / batch scripts

Any command-line argument that isn't an option is opened as a file or folder. Options run in order after loading,
and each one waits for running jobs:

```
ORCA-MI.exe ct.nii.gz pet.nii.gz --layout=mpr --fuse --mode3d=dvr
ORCA-MI.exe --script=steps.txt
```

`steps.txt` example (one command per line):
```
loaddicom D:/study/DICOM
select 1
suv
newseg lesions
threshold 2.5,1000
splitcomponents
stats
save_seg D:/out/lesions.nii.gz
nnstart
nnpoint max
save_seg D:/out/lesion.dcm
```
Available commands (also as `v.<command>(…)` in Python; `v.help()` lists them with their arguments):

| Group | Commands |
|---|---|
| Loading | `open loaddicom closeimage closeall listimages select nickname setrole segtoimage moveseg viewports showall fuseall image3d viewsegopacity measurements` |
| Database / PACS folders | `pacsadd pacsindex pacsopen pacsfilter pacsloadstudy` |
| Display | `layout hanging activevp view tab theme contrast window colormap cursor slice tool fuse overlayopacity overlaycolormap nooverlay syncoverlay sync snapshot` |
| 3D | `mode3d view3d show3d cpu3d gpu3d rotate3d removetable` |
| Segmentation | `newseg label threshold morph keeplargest fillholes splitcomponents segpalette segopacity segoutline iterative iterthreshold` |
| Measurement | `stats metrics printmetrics suv annotate score` |
| Registration | `regpair center translate rigid printtransform resample deformable` |
| Dynamic | `dynamic` |
| Dose | `dose dosescale rx structures dvh dvhwindow dvhmetrics printdvh constraintpreset addconstraint clearconstraints printconstraints isodose isomode isolevels dvhcsv colorwash` |
| AI | `python packages installpackages nndevice nnispeed nnoverwrite combinelabels nnmodel nnstart nnwait nnpoint nnneg nnnext aipreset aimodel ai presets installmodel installenv modelmanifest modellibrary modelremove aidiagnose train finetune trainings traineval trainstop traincontinue logsearch` |
| Export | `save_seg save_image exportdicom exportimages crop` |
| Sessions | `saveworkspace loadworkspace autosave session sessioncase sessionnext sessionsave sessionend scoredb results` |
| Other | `listen about shortcuts dropdialog wait quit` |


### Python API

`orcami.py` sits next to the exe and needs only the Python standard library (numpy only for arrays).

```python
import sys; sys.path.insert(0, r"C:\path\to\dist")
import orcami as om

# 1) one-shot launch with options
om.launch("ct.nii.gz", overlay="pet.nii.gz", overlay_colormap="hot iron", seg="organs.nii.gz",
          palette="turbo", layout="mpr", mode3d="dvr", theme="nord")

# 2) live control: starts the viewer (or connects to a running one) and returns results
v = om.Viewer()
v.load("ct.nii.gz")                                         # role="image"
v.load("pet.nii.gz", role="overlay", colormap="hot iron", opacity=0.6)
v.load(mask_array, role="seg", affine=nib_img.affine, palette="turbo")   # numpy / nibabel / SimpleITK
v.threshold(2.5, 1000); v.splitcomponents()
print(v.stats())                                            # [{'label': 1, 'volume_ml': ..., 'mean': ...}, ...]
print(v.metrics(0, 0, 1, 0, 1, 1))                          # Dice, HD95, ...
v.run_ai(preset=1, model=r"D:\nnUNet\...\3d_fullres")       # nnU-Net / regression presets
v.layout("1x2"); v.view("3d"); v.snapshot("view.png")
v.help()                                                    # every command
```

Every command in the list above is available as `v.<command>(args...)`. Commands run in order, and each call
returns when its background work (loading, AI, registration) has finished. The API listens on `127.0.0.1` only
(default port 47654). It starts with `--listen[=port]`, with `om.Viewer()`, or from *Settings → Python API*.

### Examples (folder `examples`)

* `01_quick_start.py` – load PET/CT + lesions, print MTV / SUVmax / SUVpeak / TLG per lesion, export figures and GIFs.
* `02_batch_tlg_table.py` – one CSV with MTV, SUVmean, SUVmax, SUVpeak and TLG for every patient and lesion.
* `03_batch_crop_and_figures.py` – crop every patient to lungs + liver (head–feet only, chosen margins), save the cropped CT, and export MIP figures, a 3D rotation GIF and a coronal cine for each patient.
* `04_dynamic_and_time_points.py` – dynamic frames and time points.
* `05_segment_and_score_database.py` – build a segmentation and a scoring database, then segment, refine and score them.
* `06_review_cases_one_by_one.py` – show a series of cases one by one with `view(image, fused, seg, colormap, window,
  layout, ...)`: per-case or common colormaps, windows, fusion opacity, segmentation colours / outlines and layout; the
  crosshair goes to the segmentation (`gotoseg`). In the console: Enter = next, b = back, s = save the screen, q = quit.
* `07_prepare_copy_segment_score_database.py` – prepare a self-contained copy of a segmentation and / or scoring
  database to give to several physicians: every image is copied into one target folder (originals untouched), with the
  shared set-up (labels, questions), one blinded reading-session file per physician (`scoredb …|save=1`, paths relative
  to the folder), a README for the physicians, a copy log and optionally a zip. The physicians need ORCA-MI with a
  licence; their results are written into the folder, which they send back.

## 10. Feedback and privacy

### 💬 Feedback, bug reports and feature requests

Help → **🐞 Report a bug**, **💡 Request a feature** or **💬 Comment / feedback**. Write a title and the message;
optionally your name and an e-mail address for a reply, the version / system information and, for bugs, the
recent error messages (folders are removed, only file names are kept). Please do not include patient information.

**📨 Send** delivers the message to the author (salimiyazdan@gmail.com) with one click: no e-mail program needed
(an internet connection is). *✉ by e-mail instead* opens your e-mail program with the message ready to send.

#### Anonymous usage statistics (opt-in)

At the first start ORCA-MI asks whether it may send anonymous usage statistics. **Nothing is sent unless you say
yes**, and you can change it any time in **Help → 🔒 Privacy & usage statistics** (or Help → Feedback). *Show exactly
what is sent* displays the report. At most once a day it contains: a random install number (made on this computer,
not derived from your name, licence or computer; strictly speaking pseudonymous), the version, the operating system, the number of starts
and how often each tool was used (e.g. `load_CT: 3, export_dicom: 1, tab_segment: 4, tool_brush: 2, threshold: 1`).
Never images, file or folder names, patient data or anything you type. The counts are kept on the computer as you
work (`usage.json`) and go with the next day's report.

**Your country** is a separate question at the first start (answer it independently of the statistics; both are
asked once). With yes, ORCA-MI sends **one time** the country of Windows' region setting (*Settings → Time &
language → Region*, e.g. `CH`), the version and the operating system — without the install number, so it cannot be
linked to the statistics, and never an IP address, a city or a location service. Change it in Help → Privacy & usage
statistics.

#### Usage statistics per user (a separate opt-in, licensed users only)

Licensed users are asked **once more, separately**: *“Usage statistics with your name?”*. You can refuse it and still
share the anonymous statistics, or the other way round; nothing depends on it (every tool works the same).

* **What is sent**, once a day at most (*Show exactly what is sent* displays it): your licence ID, name, institution
  and e-mail (from your licence), the version, the operating system, the **number of times you opened ORCA-MI** and
  **how often each tool and tab was used** since the last report. Never images, file or folder names, patient data or
  anything you type.
* **Why:** to see which tools each research group really uses, to support and improve them.
* **Who and where:** only the author (salimiyazdan@gmail.com), in the sheet *Usage per user* of the author's Google
  Sheet (Google's servers, possibly outside Switzerland and the EU). It is **kept apart from the anonymous
  statistics and not linked to them** (no install number is sent with it).
* **How long:** until you withdraw; rows older than 24 months are deleted automatically.
* **Your rights:** ask for a copy, a correction or the deletion of your data (e-mail the author), and withdraw any
  time: **Help → 🔒 Privacy & usage statistics** → untick *Link my usage to my licence*. Withdrawing stops it at once,
  clears the counts kept on this computer and asks the author's sheet to **delete every row of your licence**.
  **🗑 Delete my per-user statistics at the author** deletes them without withdrawing (the counts then start again).
  Without an internet connection to the author's sheet, the deletion opens a ready e-mail instead.

*Last report* (under the box) shows when the last report reached the author's sheet, or why it failed; a failed
report keeps its counts and is sent again at the next start.

The legal basis is your consent (GDPR art. 6(1)(a) and 7; Swiss nFADP). Script: `userstats 0|1|show|privacy`.

**Your own models stay private:** models you train or fine-tune (Train tab), their training data, evaluation and
logs never leave this computer. Bug reports leave out the log lines of training and of your own models.

#### Privacy and licences in the program

*Help → About* repeats the short privacy statement and opens this section (**🔒 Privacy details**) and the list of
the open-source libraries built into ORCA-MI with their licence texts (**📜 Third-party licences**,
`docs/third_party_licenses.html`). The installer shows the research-use notice, the privacy statement and the
licence notes before installing.

## 11. Roadmap

### Radiomics (planned)

Not included yet. Recommended approach: PyRadiomics, IBSI-compliant, on any segmentation (per label), with saved settings (bin width, resampling, filters), exported as CSV, plus batch mode over a database.
