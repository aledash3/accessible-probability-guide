import os
import tkinter as tk
from tkinter import Image, messagebox, filedialog
import math
import csv
import pyttsx3
import pygame
import threading
from PIL import Image, ImageTk
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, "media")

# ==============================
# CONTENIDO TEÓRICO EMBEBIDO
# ==============================

class Contenido:
    
    GUIA = {

    "Introducción": {
        "texto": """
BIENVENIDO A LA GUÍA DE PERMUTACIONES Y COMBINACIONES

Esta guía explica los conceptos fundamentales de probabilidad
relacionados con conteo:

• Factorial
• Permutaciones (orden importa)
• Combinaciones (orden no importa)

Además, incluye ejercicios resueltos, videos explicativos y una calculadora integrada.
"""
    },

    "Factorial": {
        "texto": """
FACTORIAL

Definición:
n! = n · (n-1) · (n-2) · ... · 1

Ejemplo:
5! = 5·4·3·2·1 = 120

En probabilidad, el factorial se usa como base
para calcular permutaciones y combinaciones.
""",
        "imagen": os.path.join(MEDIA_DIR, "factorial.png")
    },

    "Permutaciones": {
        "texto": """
PERMUTACIONES

Una permutación es un arreglo de elementos
DONDE EL ORDEN IMPORTA.

Fórmula:
P(n,r) = n! / (n-r)!

Ejemplo:
Si nueve estudiantes toman un examen y todos obtienen diferente calificación, 
cualquier alumno podría alcanzar la calificación más alta. 
La segunda calificación más alta podría ser obtenida por uno de los 8 restantes. 
La tercera calificación podría ser obtenida por uno de los 7 restantes.

P(9,3) = 9! / 6! = 504
""",
        "imagen": os.path.join(MEDIA_DIR, "permutacion.png")
    },

    "Combinaciones": {
        "texto": """
COMBINACIONES

Una combinación es una selección de elementos
DONDE EL ORDEN NO IMPORTA.

Fórmula:
C(n,r) = n! / (r!(n-r)!)

Ejemplo:
Si se seleccionan cinco cartas de un grupo de nueve, ¿Cuántas combinaciones de cinco cartas habría?

C(9,5) = 126
""",
        "imagen": os.path.join(MEDIA_DIR, "combinaciones.png")
    },

    "Ejercicios Resueltos": {
        "texto": """
EJERCICIO 1:
¿Cuántas formas hay de ordenar 4 libros?

Paso 1: El orden importa → Permutación
Paso 2: P(4,4) = 4! = 24

EJERCICIO 2:
Elegir 2 cartas de un grupo de 5

Paso 1: El orden no importa → Combinación
Paso 2: C(5,2) = 10

VIDEOS EXPLICATIVOS

VIDEO 1 -> PERMUTACIONES
VIDEO 2 -> COMBINACIONES
""",
        "videos": [
            os.path.join(MEDIA_DIR, "permutaciones.mp4"),
            os.path.join(MEDIA_DIR, "combinaciones.mp4")
        ]
    },

    "Bibliografía": {
        "texto": """
BIBLIOGRAFÍA

1. Devore, J. L. (2016).
   Probabilidad y Estadística para Ingeniería y Ciencias.
   Cengage Learning.

2. Walpole, R. E., Myers, R. H.
   Probabilidad y Estadística para Ingenieros.
   Pearson Educación.

3. Ross, S. M.
   Introducción a la Probabilidad.
   Academic Press.

4. Apuntes de clase – Universidad Politécnica Salesiana
"""
    },

    "Guía de Uso": {
        "texto": """
GUÍA DE USO DE LA APLICACIÓN

1. USO DE LA CALCULADORA
Ingrese n y r, seleccione la operación y presione calcular.

2. CARGA DE ARCHIVOS TXT
Los archivos .txt son los únicos que se pueden cargar para procesar múltiples cálculos a la vez.

Formato:
P,n,r
C,n,r

Ejemplo de contenido:
P,5,3
C,7,2

3. EXPORTACIÓN CSV
Se genera archivo con resultados procesados.
Al momento de guardar el archivo, debe escribir el nombre que desee y añadir al final la extensión .csv (ejemplo: resultados.csv)

NOTAS:
- n y r deben ser enteros
- r ≤ n (r debe ser menor o igual a n)
"""
    }

}

# ==============================
# MOTOR MATEMÁTICO
# ==============================

class MotorProbabilidad:

    @staticmethod
    def factorial(n):
        return math.factorial(n)

    @staticmethod
    def permutacion(n, r):
        return math.factorial(n) // math.factorial(n - r)

    @staticmethod
    def combinacion(n, r):
        return math.factorial(n) // (
            math.factorial(r) * math.factorial(n - r)
        )


# ==============================
# SISTEMA DE VOZ
# ==============================

class SistemaVoz:

    def __init__(self):
        self.hablando = False
        self.engine = None

    def hablar(self, texto):
        if self.hablando:
            return

        def ejecutar():
            self.hablando = True
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 160)
            self.engine.setProperty('volume', 0.5)
            self.engine.say(texto)
            self.engine.runAndWait()
            self.engine.stop()
            self.engine = None
            self.hablando = False

        threading.Thread(target=ejecutar, daemon=True).start()

    def pausar(self):
        if self.hablando and self.engine:
            self.engine.stop()
            self.hablando = False

    def cambiar_volumen(self, valor):
        if self.engine:
            self.engine.setProperty('volume', float(valor))

# ==============================
# SISTEMA DE MÚSICA
# ==============================
class SistemaMusica:

    def __init__(self):
        pygame.mixer.init()
        self.reproduciendo = False
        self.pausado = False

    def cargar(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("Archivos MP3", "*.mp3")]
        )
        if archivo:
            pygame.mixer.music.load(archivo)
            self.pista_actual = archivo.split("/")[-1]
            return self.pista_actual


    def reproducir(self):
        pygame.mixer.music.play(-1)
        self.reproduciendo = True
        self.pausado = False

    def pausar(self):
        pygame.mixer.music.pause()
        self.pausado = True

    def reanudar(self):
        pygame.mixer.music.unpause()
        self.pausado = False

    def detener(self):
        pygame.mixer.music.stop()
        self.reproduciendo = False
        self.pausado = False

# ==============================
# INTERFAZ PRINCIPAL
# ==============================

class Aplicacion:
    
    def __init__(self, root):

        self.root = root
        # Abrir maximizada
        self.root.state('zoomed')
        # Bloquear redimensionamiento manual
        self.root.resizable(False, False)
        self.root.grid_rowconfigure(3, weight=0)
        self.root.title("Guía Accesible de Probabilidad")
        self.root.geometry("1000x650")
        self.root.configure(bg="#F4F6F7")
        self.motor = MotorProbabilidad()
        self.voz = SistemaVoz()
        self.musica = SistemaMusica()
        self.FUENTE_GENERAL = 20
        self.FUENTE_TITULO = 25
        self.MAX_FUENTE = 32

        self.crear_interfaz()
        
        self.root.grid_rowconfigure(0, weight=0)  # Música (fijo)
        self.root.grid_rowconfigure(1, weight=1)  # Contenido (expandible)
        self.root.grid_rowconfigure(2, weight=0)  # Calculadora (fijo)

        self.root.grid_columnconfigure(0, weight=0)  # Menú lateral
        self.root.grid_columnconfigure(1, weight=1)  # Texto principal
        
        
    def abrir_video(self, ruta):
        if os.path.exists(ruta):
            if os.name == "nt":
                os.startfile(ruta)  # Windows
            else:
                subprocess.call(["xdg-open", ruta])  # Linux
        else:
            messagebox.showerror("Error", "Video no encontrado")
    # ------------------------------
    def cargar_y_actualizar_pista(self):
        pista = self.musica.cargar()
        if pista:
            self.label_pista.config(text=pista)
    # ------------------------------
    def actualizar_limite_fuente(self):
        altura = self.root.winfo_screenheight()
        return max(12, altura // 35)
    
    # ------------------------------
    def cambiar_volumen(self, valor):
        pygame.mixer.music.set_volume(float(valor))

    def crear_interfaz(self):
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=0)  # menú fijo
        self.root.grid_columnconfigure(1, weight=1)  # texto se expande
        
        # ==============================
        # CONFIGURACIÓN GENERAL DEL ROOT
        # ==============================
        tk.Label(self.root,
         text="Calculadora de permutación o combinación",
         font=("Arial", self.FUENTE_TITULO),
         bg="#F4F6F7"
         ).grid(row=2, column=0,pady=2)

        # ==============================
        # BARRA SUPERIOR (MÚSICA) - FIJA
        # ==============================
        barra_musica = tk.Frame(self.root, bg="#1E3A5F", pady=8)
        barra_musica.grid(row=0, column=0, columnspan=2, sticky="ew")

        tk.Button(barra_musica, text="Buscar canción",
              command=self.cargar_y_actualizar_pista,
              font=("Arial", self.FUENTE_GENERAL)
              ).pack(side="left", padx=5)

        tk.Button(barra_musica, text="Reproducir",
              command=self.musica.reproducir,
              font=("Arial", self.FUENTE_GENERAL)
              ).pack(side="left", padx=5)

        tk.Button(barra_musica, text="Pausar",
              command=self.musica.pausar,
              font=("Arial", self.FUENTE_GENERAL)
              ).pack(side="left", padx=5)

        self.volumen = tk.Scale(barra_musica,
                            from_=0, to=1,
                            resolution=0.1,
                            orient="horizontal",
                            label="Volumen música",
                            font=("Arial", self.FUENTE_GENERAL),
                            length=250,
                            command=self.cambiar_volumen)
        self.volumen.set(0.5)
        self.volumen.pack(side="left", padx=10)

        self.label_pista = tk.Label(barra_musica,
                                text="Sin pista seleccionada",
                                bg="#1E3A5F",
                                fg="white",
                                font=("Arial", self.FUENTE_GENERAL))
        self.label_pista.pack(side="right", padx=15)

        # ==============================
        # MENÚ LATERAL
        # ==============================
        self.menu = tk.Listbox(self.root,
                       font=("Arial", self.FUENTE_TITULO),
                       bg="#D6EAF8")
        self.menu.grid(row=1, column=0, sticky="nswe")
        for tema in Contenido.GUIA:
            self.menu.insert(tk.END, tema)
        self.menu.bind("<<ListboxSelect>>", self.mostrar_contenido)

        # ==============================
        # ÁREA DE TEXTO (ÚNICO QUE CRECE)
        # ==============================
        self.texto = tk.Text(self.root,
                         wrap="word",
                         bg="white")
        self.texto.grid(row=1, column=1, sticky="nsew")

        self.texto.tag_configure("normal",
                         font=("Arial", self.FUENTE_GENERAL))

        self.texto.tag_configure("titulo",
                         font=("Arial", self.FUENTE_TITULO, "bold"))
        self.texto.config(state="disabled")

        # ==============================
        # PANEL INFERIOR - FIJO
        # ==============================
        panel = tk.Frame(self.root, bg="#F4F6F7")
        panel.grid(row=3, column=0, columnspan=2, sticky="ew")

        tk.Label(panel,
         text="Control de accesibilidad",
         font=("Arial", self.FUENTE_TITULO)
         ).grid(row=3, column=0, pady=5)
        
        tk.Label(panel, text="n:",
             font=("Arial", self.FUENTE_GENERAL)
             ).grid(row=0, column=0)

        self.entry_n = tk.Entry(panel,
                            font=("Arial", self.FUENTE_GENERAL),
                            width=8)
        self.entry_n.grid(row=0, column=1)

        tk.Label(panel, text="r:",
             font=("Arial", self.FUENTE_GENERAL)
             ).grid(row=0, column=2)

        self.entry_r = tk.Entry(panel,
                            font=("Arial", self.FUENTE_GENERAL),
                            width=8)
        self.entry_r.grid(row=0, column=3)

        self.tipo = tk.StringVar(value="P")

        tk.Radiobutton(panel,
                   text="Permutación",
                   variable=self.tipo,
                   value="P",
                   font=("Arial", self.FUENTE_TITULO)
                   ).grid(row=1, column=0)

        tk.Radiobutton(panel,
                   text="Combinación",
                   variable=self.tipo,
                   value="C",
                   font=("Arial", self.FUENTE_TITULO)
                   ).grid(row=1, column=1)

        tk.Button(panel,
              text="Calcular",
              font=("Arial", self.FUENTE_GENERAL),
              bg="#ABEBC6",
              command=self.calcular
              ).grid(row=1, column=2)

        tk.Button(panel,
              text="Cargar TXT",
              font=("Arial", self.FUENTE_GENERAL),
              bg="#F9E79F",
              command=self.cargar_archivo
              ).grid(row=1, column=3)
        
        tk.Button(panel,
          text="🔊 Leer",
          font=("Arial", self.FUENTE_GENERAL),
          command=self.leer_texto
          ).grid(row=4, column=0)

        tk.Button(panel,
          text="|| Pausar voz",
          font=("Arial", self.FUENTE_GENERAL),
          command=self.voz.pausar
          ).grid(row=4, column=1)

        tk.Button(panel,
              text="Aumentar Letra",
              font=("Arial", self.FUENTE_GENERAL),
              command=self.aumentar_letra
              ).grid(row=4, column=3, padx=15)

        tk.Button(panel,
              text="Reducir Letra",
              font=("Arial", self.FUENTE_GENERAL),
              command=self.reducir_letra
              ).grid(row=4, column=4, padx=15)
        
    # ------------------------------
    def mostrar_contenido(self, event):
        if not self.menu.curselection():
            return

        seleccion = self.menu.get(self.menu.curselection())
        data = Contenido.GUIA[seleccion]

        self.texto.config(state="normal")
        self.texto.delete("1.0", tk.END)

        # TEXTO
        self.texto.insert(tk.END, data["texto"], "normal")

        # IMAGEN (si existe)
        if "imagen" in data:
            ruta_img = data["imagen"]
            if os.path.exists(ruta_img):
                img = Image.open(ruta_img)
                img = img.resize((420, 260))
                self.img_tk = ImageTk.PhotoImage(img)
                self.texto.insert(tk.END, "\n\n")
                self.texto.image_create(tk.END, image=self.img_tk)

        # VIDEOS (si existen)
        if "videos" in data:
            self.texto.insert(tk.END, "\n\n")
            for i, ruta in enumerate(data["videos"], 1):
                if os.path.exists(ruta):
                    btn = tk.Button(self.texto,
                                text=f"▶ Ver video {i}",
                                font=("Arial", self.FUENTE_GENERAL),
                                command=lambda r=ruta: self.abrir_video(r))
                self.texto.window_create(tk.END, window=btn)
                self.texto.insert(tk.END, "\n")

        self.texto.config(state="disabled")
    # ------------------------------

    def leer_texto(self):
        contenido = self.texto.get("1.0", tk.END)
        self.voz.hablar(contenido)

    # ------------------------------

    def aumentar_letra(self):
        if self.FUENTE_GENERAL >= self.MAX_FUENTE:
            messagebox.showinfo("Límite alcanzado",
                            "El tamaño máximo permitido es 32.")
            return

        self.FUENTE_GENERAL += 2
        self.FUENTE_TITULO += 2
        self.actualizar_fuentes()

    # ------------------------------      
    def reducir_letra(self):
        if self.FUENTE_GENERAL <= 15:
            messagebox.showinfo("Límite alcanzado",
                            "El tamaño mínimo permitido es 15.")
            return

        self.FUENTE_GENERAL -= 2
        self.FUENTE_TITULO -= 2
        self.actualizar_fuentes()

    # ------------------------------
    def actualizar_fuentes(self):

        def actualizar(widget):
            try:
                widget.config(font=("Arial", self.FUENTE_GENERAL))
            except:
                pass

            for hijo in widget.winfo_children():
                actualizar(hijo)

        actualizar(self.root)

        self.menu.config(font=("Arial", self.FUENTE_TITULO))
        self.texto.tag_configure("normal",
                             font=("Arial", self.FUENTE_GENERAL))
        self.texto.tag_configure("titulo",
                             font=("Arial", self.FUENTE_TITULO, "bold"))

    # ------------------------------
    def calcular(self):
        try:
            n = int(self.entry_n.get())
            r = int(self.entry_r.get())

            if self.tipo.get() == "P":
                resultado = self.motor.permutacion(n, r)
                texto = f"P({n},{r}) = {resultado}"
            else:
                resultado = self.motor.combinacion(n, r)
                texto = f"C({n},{r}) = {resultado}"

            messagebox.showinfo("Resultado", texto)

        except:
            messagebox.showerror("Error", "Datos inválidos")

    # ------------------------------

    def cargar_archivo(self):

        archivo = filedialog.askopenfilename(
            filetypes=[("Archivo TXT", "*.txt")]
        )

        if not archivo:
            return

        resultados = []

        with open(archivo, "r") as f:
            for linea in f:
                tipo, n, r = linea.strip().split(",")
                n, r = int(n), int(r)

                if tipo == "P":
                    res = self.motor.permutacion(n, r)
                else:
                    res = self.motor.combinacion(n, r)

                resultados.append([tipo, n, r, res])

        self.guardar_csv(resultados)

    # ------------------------------

    def guardar_csv(self, resultados):

        archivo = filedialog.asksaveasfilename(
            defaultextension=".csv"
        )

        if not archivo:
            return

        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Operacion", "n", "r", "Resultado"])
            writer.writerows(resultados)

        messagebox.showinfo("Éxito", "Archivo CSV guardado correctamente")


# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
