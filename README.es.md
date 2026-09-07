# 📘 Guía Accesible de Probabilidad

<p align="center">
  <a href="https://github.com/aledash3/accessible-probability-guide/actions/workflows/tests.yml">
    <img src="https://github.com/aledash3/accessible-probability-guide/actions/workflows/tests.yml/badge.svg" alt="Estado de Tests">
  </a>
  <img src="https://img.shields.io/badge/python-3.10%20%7C%203.11-blue.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/licencia-MIT-green.svg" alt="Licencia MIT">
  <a href="README.md">
    <img src="https://img.shields.io/badge/lang-English-blue.svg" alt="Switch to English">
  </a>
</p>

Aplicación de escritorio interactiva desarrollada en Python para reforzar la comprensión y el aprendizaje de **factorial, permutaciones y combinaciones**. Integra contenido pedagógico, ejercicios prácticos, cálculos interactivos en tiempo real, procesamiento por lotes mediante archivos y características avanzadas de accesibilidad (síntesis de voz, temas adaptativos, modo de alto contraste y atajos de teclado) en una interfaz gráfica moderna.

> 🌐 **Language / Idioma:** Español | [Switch to English documentation](README.md)

---

## 📌 Descripción general

La aplicación ayuda a comprender problemas de análisis combinatorio y a resolverlos de forma guiada y accesible. El usuario puede estudiar conceptos teóricos con ejemplos interactivos, calcular operaciones individuales con validación estricta de dominios matemáticos, procesar archivos con múltiples ejercicios en lote y exportar los resultados tabulados en CSV para su análisis en hojas de cálculo.

Presenta una interfaz gráfica moderna y accesible, arquitectura modular desacoplada, validación de datos por línea y un empaquetador para generar ejecutables autónomos de Windows sin dependencias externas.

---

## 🎯 Objetivos

### Objetivo general
Facilitar la enseñanza y el aprendizaje autónomo del análisis combinatorio y la probabilidad elemental mediante una aplicación de escritorio interactiva, universalmente accesible y pedagógicamente guiada.

### Objetivos específicos
- **Pedagogía guiada:** Explicar factorial, permutaciones y combinaciones mediante definiciones formales, propiedades y ejemplos visuales.
- **Validación matemática rigurosa:** Validar entradas numéricas enteras respetando las restricciones de dominio ($n \ge 0$, $0 \le r \le n$).
- **Automatización por lotes:** Procesar archivos de texto con múltiples operaciones combinatorias ignorando comentarios y líneas vacías.
- **Exportación estructurada:** Generar reportes tabulados en formato CSV compatibles con Microsoft Excel y LibreOffice Calc.
- **Accesibilidad universal:** Integrar síntesis de voz en segundo plano (TTS), control dinámico de tipografía, temas claro/oscuro/alto contraste y navegación rápida por teclado.
- **Ingeniería mantenible:** Mantener una arquitectura de código desacoplada, modular y verificada por pruebas unitarias automatizadas e integración continua (CI).

---

## ✨ Funcionalidades

### 🧮 Calculadora combinatoria interactiva
- **Permutaciones ordinarias:** $P(n, r) = \frac{n!}{(n - r)!}$
- **Combinaciones ordinarias:** $C(n, r) = \frac{n!}{r! \cdot (n - r)!}$
- **Factorial:** $n! = \prod_{k=1}^n k$ (con $0! = 1$)
- Validación estricta con retroalimentación clara ante entradas inválidas o desbordamientos lógicos.

### 📂 Procesamiento por lotes y exportación CSV
- Lectura y parsing tolerante de operaciones en archivos `.txt` (`sample_calculations.txt`).
- Soporte para comentarios (iniciados con `#`), espacios en blanco y líneas vacías.
- Localización precisa de errores indicando el número exacto de línea ante datos mal estructurados.
- Exportación automática a `.csv` (`sample_export.csv`) con cabeceras estándar para auditoría o evaluación académica.

### ♿ Accesibilidad y diseño universal
- **Texto a voz (TTS):** Lectura del contenido de las lecciones mediante `pyttsx3` en hilos de fondo desacoplados.
- **Escalado tipográfico:** Botones directos para aumentar y reducir dinámicamente el tamaño de la fuente.
- **Paleta y contrastes:** Temas claro, oscuro y modo de alto contraste para personas con baja visión.
- **Atajos de teclado:**
  - `Ctrl + Enter`: Ejecutar cálculo inmediato.
  - `Ctrl + R`: Iniciar / pausar lectura por voz.
  - `Ctrl + S`: Seleccionar y procesar archivo de texto.
- **Resiliencia de hardware:** Operatividad completa garantizada incluso si el sistema carece de tarjeta o salida de audio.

---

## 🖼 Recursos visuales

| Factorial | Permutaciones | Combinaciones |
| :---: | :---: | :---: |
| ![Factorial](src/probability_guide/assets/factorial.png) | ![Permutaciones](src/probability_guide/assets/permutacion.png) | ![Combinaciones](src/probability_guide/assets/combinaciones.png) |

---

## 🏗 Arquitectura del proyecto

El proyecto sigue una estructura modular estándar para empaquetado en Python con nomenclatura en inglés:

```text
accessible-probability-guide/
├── .github/
│   └── workflows/
│       └── tests.yml            # Pipeline de CI (GitHub Actions)
├── scripts/
│   └── build_windows.ps1        # Script PowerShell para empaquetar con PyInstaller
├── src/
│   └── probability_guide/
│       ├── __init__.py          # Metadatos del paquete
│       ├── __main__.py          # Punto de entrada de ejecución como módulo
│       ├── app.py               # Interfaz gráfica (Tkinter) y accesibilidad
│       ├── calculations.py      # Motor matemático y validación de dominios
│       ├── content.py           # Lecciones pedagógicas, teoría y bibliografía
│       ├── file_processing.py   # Parser de TXT y exportación a CSV
│       ├── speech.py            # Motor asíncrono de síntesis de voz (pyttsx3)
│       └── assets/              # Ilustraciones y recursos multimedia
├── tests/
│   └── test_calculations.py     # Suite de pruebas unitarias automatizadas
├── sample_calculations.txt      # Archivo de ejemplo para procesamiento por lotes
├── sample_export.csv            # Ejemplo de archivo CSV resultante
├── pyproject.toml               # Especificación estándar PEP 517/518 y entrypoints
├── LICENSE                      # Licencia MIT
├── README.md                    # Documentación técnica en inglés
└── README.es.md                 # Documentación pedagógica en español
```

---

## 🛠 Tecnologías utilizadas

- **Lenguaje:** Python 3.10+
- **Interfaz gráfica:** Tkinter & CustomTkinter
- **Procesamiento de imágenes y multimedia:** Pillow, pygame
- **Accesibilidad y audio:** pyttsx3 (SAPI5 / NSSpeechSynthesizer / espeak)
- **Empaquetado y distribución:** setuptools, PyInstaller
- **Automatización y pruebas:** unittest, GitHub Actions

---

## 🚀 Instalación y ejecución

### Requisitos previos
- Python 3.10 o superior instalado.
- Soporte para `tkinter` (incluido por defecto en instaladores de Python para Windows y macOS).

### 1. Clonar el repositorio
```bash
git clone https://github.com/aledash3/accessible-probability-guide.git
cd accessible-probability-guide
```

### 2. Instalar el paquete en modo editable o directo
```bash
python -m pip install .
```

### 3. Ejecutar la aplicación
Desde cualquier terminal en tu sistema:
```bash
probability-guide
```
*(O mediante el alias: `guia-probabilidad`)*

O directamente como módulo de Python:
```bash
python -m probability_guide
```

---

## 📦 Generación de ejecutable para Windows

Para compilar un binario independiente (`.exe`) que funcione sin requerir Python instalado:

```powershell
./scripts/build_windows.ps1
```

El ejecutable compilado estará disponible en:
```text
dist/ProbabilityGuide/ProbabilityGuide.exe
```

---

## 📝 Formato para procesamiento por lotes

El archivo `.txt` de entrada permite calcular múltiples combinatorias por línea (`sample_calculations.txt`):

```text
# Formato: Operación, n, r
P, 6, 5
C, 6, 5
```
- `P`: Permutación ($P(n, r)$) — El orden de los elementos importa.
- `C`: Combinación ($C(n, r)$) — El orden de los elementos no importa.
- Las líneas que comiencen con `#` o vacías se omiten automáticamente.

---

## 🧪 Pruebas automatizadas

Para ejecutar la suite de pruebas unitarias de la lógica combinatoria y el parser de archivos:

```bash
python -m unittest discover -s tests -v
```

El pipeline en **GitHub Actions** ejecuta estas pruebas automáticamente en cada `push` o `pull request`.

---

## 📚 Referencias bibliográficas

1. **Devore, J. L.** *Probabilidad y Estadística para Ingeniería y Ciencias*. Cengage Learning.
2. **Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K.** *Probabilidad y Estadística para Ingenieros*. Pearson Educación.
3. **Ross, S. M.** *Introducción a la Probabilidad y Estadística para Ingenieros*. Reverté.

---

## 👨‍💻 Autor

**David Alejandro Cruz Palacios**  
Estudiante de Ingeniería en Ciencias de la Computación  
Universidad Politécnica Salesiana — Quito, Ecuador  
GitHub: [@aledash3](https://github.com/aledash3)

---

## 📄 Licencia

Este proyecto está licenciado bajo los términos de la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
