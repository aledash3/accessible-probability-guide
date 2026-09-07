# 📘 Accessible Probability Guide

<p align="center">
  <a href="https://github.com/aledash3/accessible-probability-guide/actions/workflows/tests.yml">
    <img src="https://github.com/aledash3/accessible-probability-guide/actions/workflows/tests.yml/badge.svg" alt="Tests Status">
  </a>
  <img src="https://img.shields.io/badge/python-3.10%20%7C%203.11-blue.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
  <a href="README.es.md">
    <img src="https://img.shields.io/badge/lang-Espa%C3%B1ol-yellow.svg" alt="Leer en Español">
  </a>
</p>

An interactive, accessible desktop application built with Python for learning combinatorics and probability foundations (**factorials, permutations, and combinations**). It combines guided theoretical material, real-time interactive calculations, batch file processing, and robust accessibility features (Text-to-Speech synthesis, customizable UI contrast themes, dynamic font scaling, and keyboard shortcuts) within a modern desktop GUI.

> 🌐 **Language / Idioma:** English | [Leer documentación en Español](README.es.md)

---

## 📌 Overview

Understanding combinatorics and probability can be challenging without intuitive visual feedback and guided problem-solving tools. **Accessible Probability Guide** bridges this gap by providing an educational desktop software tailored for all learners, including users who rely on accessibility aids.

Users can study interactive lessons with visual demonstrations, calculate discrete combinatorics operations with strict mathematical domain validation, process batches of problems from external text files, and export structured CSV reports for spreadsheet analysis.

---

## 🎯 Key Objectives

- **Guided Pedagogy:** Explain factorials, permutations, and combinations through clear definitions, mathematical properties, and visual aids.
- **Mathematical Domain Validation:** Enforce strict mathematical constraints ($n \ge 0$, $0 \le r \le n$) with friendly error messaging.
- **Batch Processing Engine:** Parse batch `.txt` files containing operations, handling comments, whitespace, and providing precise line-level error reporting.
- **Tabular Data Export:** Generate structured CSV reports compatible with Microsoft Excel, LibreOffice Calc, and data science workflows.
- **Universal Accessibility:** Implement asynchronous Text-to-Speech (TTS), on-the-fly font scaling, high-contrast visual themes, and complete keyboard navigation.
- **Production Architecture:** Follow clean separation of concerns, comprehensive unit testing, automated CI pipelines, and standalone Windows executable builds.

---

## ✨ Features

### 🧮 Combinatorics Calculation Engine
- **Permutations:** $P(n, r) = \frac{n!}{(n - r)!}$
- **Combinations:** $C(n, r) = \frac{n!}{r! \cdot (n - r)!}$
- **Factorials:** $n! = \prod_{k=1}^n k$ (with $0! = 1$)
- Comprehensive mathematical domain validation preventing invalid inputs and logical overflows.

### 📂 Batch Processing & CSV Export
- Fault-tolerant parser for plain text operation files (`.txt`).
- Full support for comments (`#`), trailing whitespace, and blank lines.
- Detailed error diagnostics pointing directly to the offending line number.
- One-click CSV export formatted for academic review or grading.

### ♿ Accessibility & Universal Design
- **Text-to-Speech (TTS):** Non-blocking background narration of educational lessons via `pyttsx3`.
- **Dynamic Typography Scaling:** Dedicated controls to enlarge or shrink font sizes across all views.
- **Theme Customization:** Light mode, Dark mode, and High-Contrast mode for low-vision environments.
- **Productivity Keyboard Shortcuts:**
  - `Ctrl + Enter`: Calculate current inputs.
  - `Ctrl + R`: Toggle TTS narration.
  - `Ctrl + S`: Open file dialog for batch calculation.
- **Hardware Resilience:** Graceful fallback ensures full functionality even on systems without audio output devices.

---

## 🖼 Educational Visuals

| Factorial | Permutations | Combinations |
| :---: | :---: | :---: |
| ![Factorial Illustration](src/guia_probabilidad/recursos/factorial.png) | ![Permutations Illustration](src/guia_probabilidad/recursos/permutacion.png) | ![Combinations Illustration](src/guia_probabilidad/recursos/combinaciones.png) |

---

## 🏗 Project Architecture

The codebase adheres to modern Python packaging standards (PEP 517/518):

```text
accessible-probability-guide/
├── .github/
│   └── workflows/
│       └── tests.yml           # GitHub Actions CI pipeline
├── scripts/
│   └── build_windows.ps1       # PyInstaller PowerShell packaging script
├── src/
│   └── guia_probabilidad/
│       ├── __init__.py         # Package entry & version metadata
│       ├── __main__.py         # Module execution entrypoint
│       ├── app.py              # Tkinter GUI & accessibility controls
│       ├── archivos.py         # Batch file parser & CSV exporter
│       ├── calculos.py         # Combinatorics computation engine
│       ├── contenido.py        # Educational lessons & theoretical content
│       ├── voz.py              # Background TTS audio synthesis worker
│       └── recursos/           # Graphical and multimedia bundled assets
├── tests/
│   └── test_probabilidad.py    # Unit tests for calculations & parsing
├── Calculos_a_realizar.txt     # Sample batch input file
├── Exportacion_calculos.csv    # Sample exported output CSV
├── pyproject.toml              # Build system, metadata & CLI entry points
├── LICENSE                     # MIT License
├── README.md                   # English technical documentation
└── README.es.md                # Spanish educational documentation
```

---

## 🛠 Tech Stack

- **Core Language:** Python 3.10+
- **GUI Framework:** Tkinter & CustomTkinter
- **Image & Media Handling:** Pillow, pygame
- **Speech Synthesis:** pyttsx3 (SAPI5 / NSSpeechSynthesizer / espeak)
- **Packaging & Build Tools:** setuptools, PyInstaller
- **Testing & CI:** unittest, GitHub Actions

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.10 or higher.
- `tkinter` installed (bundled by default with standard Python installers on Windows and macOS).

### 1. Clone the Repository
```bash
git clone https://github.com/aledash3/accessible-probability-guide.git
cd accessible-probability-guide
```

### 2. Install the Package
```bash
python -m pip install .
```

### 3. Launch the Application
Run the globally registered console script:
```bash
guia-probabilidad
```
Or execute directly as a Python module:
```bash
python -m guia_probabilidad
```

---

## 📦 Windows Standalone Executable

To compile a self-contained `.exe` binary that runs on Windows without requiring a Python runtime:

```powershell
./scripts/build_windows.ps1
```

The compiled binary will be located in:
```text
dist/GuiaProbabilidad/GuiaProbabilidad.exe
```

---

## 📝 Batch Input File Format

The application parses batch calculations from simple text files:

```text
# Syntax: Operation, n, r
P, 6, 5
C, 6, 5
```
- `P`: Permutation ($P(n, r)$) — Element order matters.
- `C`: Combination ($C(n, r)$) — Element order does not matter.
- Lines starting with `#` or empty rows are automatically ignored.

---

## 🧪 Running Unit Tests

Run the test suite covering combinatorics calculations and file parsing routines:

```bash
python -m unittest discover -s tests -v
```

All tests are verified automatically on every push and pull request via GitHub Actions.

---

## 📚 Academic References

1. **Devore, J. L.** *Probability and Statistics for Engineering and the Sciences*. Cengage Learning.
2. **Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K.** *Probability & Statistics for Engineers & Scientists*. Pearson.
3. **Ross, S. M.** *Introduction to Probability and Statistics for Engineers and Scientists*. Academic Press.

---

## 👨‍💻 Author

**David Alejandro Cruz Palacios**  
Computer Science Engineering Student  
Universidad Politécnica Salesiana — Quito, Ecuador  
GitHub: [@aledash3](https://github.com/aledash3)

---

## 📄 License

This project is licensed under the terms of the [MIT License](LICENSE).
