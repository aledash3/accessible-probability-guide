# Guía accesible de probabilidad

Aplicación de escritorio en Python para estudiar **factorial, permutaciones y combinaciones**. Combina contenido teórico, una calculadora, procesamiento por lotes y herramientas de accesibilidad en una interfaz creada con Tkinter.

> Proyecto académico mejorado como pieza de portafolio: separa la lógica matemática de la interfaz, valida entradas y cuenta con pruebas automatizadas.

## Características

- Calculadora de permutaciones y combinaciones con validación de `n` y `r`.
- Explicaciones, ejercicios resueltos, imágenes y videos locales.
- Importación de operaciones desde un archivo TXT y exportación a CSV compatible con Excel y LibreOffice.
- Lectura de contenido por voz y controles para aumentar o reducir la tipografía.
- Reproductor opcional de música local; si el sistema no tiene audio disponible, el resto de la aplicación continúa funcionando.

## Tecnologías

Python, Tkinter, Pillow, pygame y pyttsx3.

## Instalación y ejecución

Requiere Python 3.10 o superior.

```bash
git clone https://github.com/aledash3/Guia-de-estudio-Probabilidad-y-Estadistica.git
cd Guia-de-estudio-Probabilidad-y-Estadistica
python -m venv .venv
```

Activa el entorno virtual y después instala las dependencias:

```bash
pip install -r requirements.txt
python proba.py
```

`tkinter` forma parte de la instalación estándar de Python en Windows y macOS. En algunas distribuciones Linux puede requerir instalarse desde el gestor de paquetes del sistema.

## Procesamiento por lotes

Usa una operación por línea; admite espacios y líneas de comentario que comienzan por `#`:

```text
# Operación,n,r
P,6,5
C,6,5
```

- `P`: permutación. El orden importa.
- `C`: combinación. El orden no importa.
- Para ambas operaciones se cumple `n ≥ 0` y `0 ≤ r ≤ n`.

Desde la aplicación selecciona **Cargar TXT** y luego elige dónde guardar el archivo CSV resultante.

## Arquitectura

```text
proba.py          interfaz Tkinter y funciones de accesibilidad
probabilidad.py   validación y cálculos combinatorios
procesamiento.py  lectura de TXT y exportación de CSV
media/            recursos visuales y audiovisuales locales
tests/            pruebas de la lógica y el procesamiento
```

## Pruebas

La lógica se prueba sin abrir la interfaz gráfica:

```bash
python -m unittest discover -s tests -v
```

## Recursos y atribución

Los materiales de estudio citan a Devore, Walpole, Myers y Ross; las referencias completas se muestran en la aplicación. El reproductor permite elegir una pista MP3 local; evita redistribuir música sobre la que no tengas derechos.

## Licencia

Este proyecto está disponible bajo la [licencia MIT](LICENSE).
