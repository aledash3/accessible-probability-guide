"""Interfaz moderna y accesible de la Guía de Probabilidad."""

from __future__ import annotations

import os
from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk
import pygame
from PIL import Image

from .file_processing import export_csv, exportar_csv, parse_file, procesar_archivo
from .calculations import ErrorDeEntrada, InputError, calculate, calcular
from .content import LECCIONES, LESSONS, Leccion, Lesson
from .speech import SistemaVoz, SpeechEngine


ASSETS_DIR = Path(__file__).with_name("assets")
RECURSOS = ASSETS_DIR
COLOR_PRIMARIO = "#5B5BD6"
COLOR_SECUNDARIO = "#8B5CF6"
COLOR_ACENTO = "#14B8A6"


class Aplicacion(ctk.CTk):
    """Ventana principal con navegación, contenido, cálculos y accesibilidad."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Guía accesible de probabilidad · v2")
        self.geometry("1440x860")
        self.minsize(1120, 700)
        self.configure(fg_color=("#F7F8FC", "#121426"))

        self.voz = SistemaVoz()
        self.leccion_actual = LECCIONES[0]
        self.botones_navegacion: list[ctk.CTkButton] = []
        self.tamano_fuente = ctk.IntVar(value=16)
        self.tema = ctk.StringVar(value="Sistema")
        self.alto_contraste = ctk.BooleanVar(value=False)
        self.tipo_operacion = ctk.StringVar(value="P  Permutación")
        self.pista_actual: str | None = None
        self.audio_disponible = self._iniciar_audio()

        self._configurar_grilla()
        self._crear_barra_lateral()
        self._crear_area_principal()
        self._crear_panel_calculo()
        self._crear_barra_inferior()
        self._registrar_atajos()
        self.mostrar_leccion(LECCIONES[0], 0)

    def _iniciar_audio(self) -> bool:
        try:
            pygame.mixer.init()
            return True
        except pygame.error:
            return False

    def _configurar_grilla(self) -> None:
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _crear_barra_lateral(self) -> None:
        self.sidebar = ctk.CTkFrame(
            self, width=270, corner_radius=0, fg_color=("#21224A", "#191A38")
        )
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar.grid_propagate(False)

        ctk.CTkLabel(
            self.sidebar,
            text="PROBABILIDAD",
            font=("Segoe UI", 13, "bold"),
            text_color="#B9BAFF",
        ).pack(anchor="w", padx=26, pady=(32, 0))
        ctk.CTkLabel(
            self.sidebar,
            text="Guía de estudio\naccesible",
            font=("Segoe UI", 25, "bold"),
            justify="left",
        ).pack(anchor="w", padx=26, pady=(5, 8))
        ctk.CTkLabel(
            self.sidebar,
            text="Versión 2.0 · Aprende a contar\nposibilidades con criterio.",
            font=("Segoe UI", 13),
            justify="left",
            text_color="#C8C8E0",
        ).pack(anchor="w", padx=26, pady=(0, 24))

        self.progreso = ctk.CTkProgressBar(
            self.sidebar, height=7, progress_color=COLOR_ACENTO, fg_color="#3B3D68"
        )
        self.progreso.pack(fill="x", padx=26)
        self.progreso.set(1 / len(LECCIONES))
        self.etiqueta_progreso = ctk.CTkLabel(
            self.sidebar, text=f"1 de {len(LECCIONES)} temas", font=("Segoe UI", 12), text_color="#C8C8E0"
        )
        self.etiqueta_progreso.pack(anchor="w", padx=26, pady=(7, 22))

        ctk.CTkLabel(
            self.sidebar, text="CONTENIDO", font=("Segoe UI", 11, "bold"), text_color="#A3A5CD").pack(
            anchor="w", padx=26, pady=(0, 8)
        )
        for indice, leccion in enumerate(LECCIONES):
            boton = ctk.CTkButton(
                self.sidebar,
                text=f" {leccion.icono}   {leccion.titulo}",
                anchor="w",
                height=38,
                corner_radius=9,
                font=("Segoe UI", 13),
                fg_color="transparent",
                hover_color="#343665",
                command=lambda tema=leccion, i=indice: self.mostrar_leccion(tema, i),
            )
            boton.pack(fill="x", padx=16, pady=2)
            self.botones_navegacion.append(boton)

        ctk.CTkLabel(
            self.sidebar, text="TIP", font=("Segoe UI", 11, "bold"), text_color="#A3A5CD").pack(
            anchor="w", padx=26, pady=(22, 2)
        )
        ctk.CTkLabel(
            self.sidebar,
            text="Si cambiar el orden cambia el resultado, usa una permutación.",
            wraplength=210,
            justify="left",
            font=("Segoe UI", 12),
            text_color="#D9DAEF",
        ).pack(anchor="w", padx=26)

    def _crear_area_principal(self) -> None:
        contenedor = ctk.CTkFrame(self, fg_color="transparent")
        contenedor.grid(row=0, column=1, sticky="nsew", padx=(30, 20), pady=(28, 12))
        contenedor.grid_columnconfigure(0, weight=1)
        contenedor.grid_rowconfigure(2, weight=1)

        cabecera = ctk.CTkFrame(contenedor, fg_color="transparent")
        cabecera.grid(row=0, column=0, sticky="ew")
        cabecera.grid_columnconfigure(0, weight=1)
        self.etiqueta_ruta = ctk.CTkLabel(
            cabecera, text="MÓDULO 01", font=("Segoe UI", 12, "bold"), text_color=COLOR_SECUNDARIO
        )
        self.etiqueta_ruta.grid(row=0, column=0, sticky="w")
        self.etiqueta_titulo = ctk.CTkLabel(cabecera, text="", font=("Segoe UI", 30, "bold"), anchor="w")
        self.etiqueta_titulo.grid(row=1, column=0, sticky="w", pady=(2, 0))
        self.etiqueta_resumen = ctk.CTkLabel(
            cabecera, text="", font=("Segoe UI", 15), text_color=("#5F6475", "#B8BBCB"), anchor="w"
        )
        self.etiqueta_resumen.grid(row=2, column=0, sticky="w", pady=(2, 14))

        acciones = ctk.CTkFrame(contenedor, fg_color="transparent")
        acciones.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        self.boton_leer = ctk.CTkButton(
            acciones, text="🔊  Leer lección", width=142, height=35, corner_radius=9,
            fg_color=COLOR_PRIMARIO, hover_color="#4848B8", command=self.leer_leccion
        )
        self.boton_leer.pack(side="left")
        ctk.CTkButton(
            acciones, text="■  Detener", width=106, height=35, corner_radius=9,
            fg_color=("#E8E8F3", "#30314A"), text_color=("#343550", "#ECECF5"),
            hover_color=("#D7D7E8", "#41425F"), command=self.voz.detener
        ).pack(side="left", padx=8)
        self.etiqueta_estado = ctk.CTkLabel(
            acciones, text="Listo para estudiar", font=("Segoe UI", 12), text_color=("#64748B", "#A3A8BA")
        )
        self.etiqueta_estado.pack(side="right")

        self.tarjeta_contenido = ctk.CTkFrame(
            contenedor, corner_radius=18, fg_color=("#FFFFFF", "#1E2038"), border_width=1,
            border_color=("#E8EAF2", "#30334F")
        )
        self.tarjeta_contenido.grid(row=2, column=0, sticky="nsew")
        self.tarjeta_contenido.grid_columnconfigure(0, weight=1)
        self.tarjeta_contenido.grid_rowconfigure(1, weight=1)
        self.etiqueta_imagen = ctk.CTkLabel(self.tarjeta_contenido, text="")
        self.contenido_texto = ctk.CTkTextbox(
            self.tarjeta_contenido, wrap="word", corner_radius=0, border_spacing=20,
            fg_color="transparent", font=("Segoe UI", self.tamano_fuente.get()), activate_scrollbars=True
        )
        self.contenido_texto.grid(row=1, column=0, sticky="nsew", padx=4, pady=5)
        self.contenido_texto.configure(state="disabled")

    def _crear_panel_calculo(self) -> None:
        self.calculadora = ctk.CTkFrame(
            self, width=340, corner_radius=18, fg_color=("#FFFFFF", "#1E2038"), border_width=1,
            border_color=("#E8EAF2", "#30334F")
        )
        self.calculadora.grid(row=0, column=2, sticky="nsew", padx=(0, 30), pady=(28, 12))
        self.calculadora.grid_propagate(False)
        self.calculadora.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.calculadora, text="CALCULADORA", font=("Segoe UI", 12, "bold"), text_color=COLOR_SECUNDARIO).pack(
            anchor="w", padx=24, pady=(24, 2)
        )
        ctk.CTkLabel(self.calculadora, text="Resuelve en segundos", font=("Segoe UI", 21, "bold")).pack(
            anchor="w", padx=24
        )
        ctk.CTkLabel(
            self.calculadora, text="Elige la operación e ingresa los valores.", font=("Segoe UI", 13),
            text_color=("#64748B", "#B8BBCB")
        ).pack(anchor="w", padx=24, pady=(2, 18))

        self.selector = ctk.CTkSegmentedButton(
            self.calculadora, values=["P  Permutación", "C  Combinación"], variable=self.tipo_operacion,
            command=self._cambiar_operacion, selected_color=COLOR_PRIMARIO, selected_hover_color="#4848B8"
        )
        self.selector.set(self.tipo_operacion.get())
        self.selector.pack(fill="x", padx=24, pady=(0, 20))

        self.entrada_n = self._campo("n", "Elementos disponibles")
        self.entrada_r = self._campo("r", "Elementos elegidos")
        self.entrada_n.bind("<Return>", lambda _evento: self.calcular())
        self.entrada_r.bind("<Return>", lambda _evento: self.calcular())

        ctk.CTkButton(
            self.calculadora, text="Calcular resultado", height=42, corner_radius=10, font=("Segoe UI", 14, "bold"),
            fg_color=COLOR_PRIMARIO, hover_color="#4848B8", command=self.calcular
        ).pack(fill="x", padx=24, pady=(22, 12))

        self.tarjeta_resultado = ctk.CTkFrame(self.calculadora, corner_radius=12, fg_color=("#F0F3FF", "#292C4B"))
        self.tarjeta_resultado.pack(fill="x", padx=24, pady=(0, 20))
        ctk.CTkLabel(self.tarjeta_resultado, text="RESULTADO", font=("Segoe UI", 10, "bold"), text_color=COLOR_SECUNDARIO).pack(
            anchor="w", padx=16, pady=(12, 0)
        )
        self.etiqueta_resultado = ctk.CTkLabel(self.tarjeta_resultado, text="Ingresa n y r", font=("Segoe UI", 21, "bold"))
        self.etiqueta_resultado.pack(anchor="w", padx=16, pady=(1, 12))

        ctk.CTkLabel(self.calculadora, text="HERRAMIENTAS", font=("Segoe UI", 11, "bold"), text_color=("#64748B", "#A9ADBD")).pack(
            anchor="w", padx=24, pady=(3, 8)
        )
        ctk.CTkButton(
            self.calculadora, text="↥  Procesar archivo TXT", anchor="w", height=35, corner_radius=8,
            fg_color="transparent", border_width=1, border_color=("#DCE0EC", "#41445E"),
            text_color=("#41455A", "#E1E3EC"), hover_color=("#EFF1F7", "#30334B"), command=self.procesar_lote
        ).pack(fill="x", padx=24, pady=3)
        ctk.CTkLabel(
            self.calculadora, text="Formato: P,n,r o C,n,r", font=("Segoe UI", 11), text_color=("#64748B", "#A9ADBD")
        ).pack(anchor="w", padx=26, pady=(2, 0))

    def _campo(self, etiqueta: str, ayuda: str) -> ctk.CTkEntry:
        ctk.CTkLabel(self.calculadora, text=etiqueta, font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=24)
        entrada = ctk.CTkEntry(
            self.calculadora, height=40, corner_radius=9, placeholder_text=ayuda, font=("Segoe UI", 14)
        )
        entrada.pack(fill="x", padx=24, pady=(4, 12))
        return entrada

    def _crear_barra_inferior(self) -> None:
        barra = ctk.CTkFrame(self, height=70, corner_radius=0, fg_color=("#FFFFFF", "#1A1C31"))
        barra.grid(row=1, column=1, columnspan=2, sticky="ew")
        barra.grid_propagate(False)
        ctk.CTkLabel(barra, text="ACCESIBILIDAD", font=("Segoe UI", 11, "bold"), text_color=COLOR_SECUNDARIO).pack(
            side="left", padx=(30, 10)
        )
        ctk.CTkLabel(barra, text="Tamaño", font=("Segoe UI", 12)).pack(side="left")
        self.control_fuente = ctk.CTkSlider(
            barra, from_=13, to=22, number_of_steps=9, width=125, command=self.cambiar_tamano_fuente
        )
        self.control_fuente.set(self.tamano_fuente.get())
        self.control_fuente.pack(side="left", padx=9)
        self.etiqueta_tamano = ctk.CTkLabel(barra, text="16 px", font=("Segoe UI", 12), width=38)
        self.etiqueta_tamano.pack(side="left")
        ctk.CTkSwitch(
            barra, text="Alto contraste", variable=self.alto_contraste, command=self.aplicar_contraste,
            font=("Segoe UI", 12), progress_color=COLOR_ACENTO
        ).pack(side="left", padx=20)
        ctk.CTkOptionMenu(
            barra, values=["Sistema", "Claro", "Oscuro"], variable=self.tema, command=self.cambiar_tema,
            width=102, corner_radius=8, fg_color=COLOR_PRIMARIO, button_color="#4848B8"
        ).pack(side="left")
        ctk.CTkButton(
            barra, text="♫ Audio", width=82, height=30, corner_radius=8, fg_color="transparent",
            border_width=1, border_color=("#DCE0EC", "#41445E"), text_color=("#41455A", "#E1E3EC"),
            command=self.elegir_audio
        ).pack(side="right", padx=(8, 30))
        ctk.CTkButton(
            barra, text="▶", width=35, height=30, corner_radius=8, fg_color="transparent",
            border_width=1, border_color=("#DCE0EC", "#41445E"), text_color=("#41455A", "#E1E3EC"),
            command=self.reproducir_audio
        ).pack(side="right")

    def mostrar_leccion(self, leccion: Leccion, indice: int) -> None:
        self.voz.detener()
        self.leccion_actual = leccion
        self.etiqueta_ruta.configure(text=f"MÓDULO {indice + 1:02d}")
        self.etiqueta_titulo.configure(text=leccion.titulo)
        self.etiqueta_resumen.configure(text=leccion.resumen)
        self.etiqueta_estado.configure(text="Listo para estudiar")
        self.progreso.set((indice + 1) / len(LECCIONES))
        self.etiqueta_progreso.configure(text=f"{indice + 1} de {len(LECCIONES)} temas")
        for posicion, boton in enumerate(self.botones_navegacion):
            boton.configure(fg_color=COLOR_PRIMARIO if posicion == indice else "transparent")

        self.contenido_texto.configure(state="normal")
        self.contenido_texto.delete("1.0", "end")
        self.contenido_texto.insert("1.0", leccion.contenido.strip())
        self.contenido_texto.configure(state="disabled")
        self._mostrar_imagen(leccion.imagen)

    def _mostrar_imagen(self, nombre: str | None) -> None:
        self.etiqueta_imagen.grid_forget()
        if not nombre:
            return
        ruta = RECURSOS / nombre
        if not ruta.exists():
            return
        imagen = Image.open(ruta)
        self.imagen_actual = ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(330, 205))
        self.etiqueta_imagen.configure(image=self.imagen_actual, text="")
        self.etiqueta_imagen.grid(row=0, column=0, pady=(20, 0))

    def _cambiar_operacion(self, valor: str) -> None:
        self.etiqueta_resultado.configure(text="Ingresa n y r")

    def calcular(self) -> None:
        try:
            n = int(self.entrada_n.get())
            r = int(self.entrada_r.get())
            operacion = self.tipo_operacion.get()[0]
            resultado = calcular(operacion, n, r)
        except (ValueError, ErrorDeEntrada) as error:
            self.etiqueta_resultado.configure(text="Revisa los datos")
            messagebox.showerror("Datos inválidos", str(error), parent=self)
            return
        self.etiqueta_resultado.configure(text=f"{operacion}({n}, {r}) = {resultado:,}")
        self.etiqueta_estado.configure(text="Cálculo completado")

    def procesar_lote(self) -> None:
        ruta = filedialog.askopenfilename(parent=self, title="Selecciona un archivo de cálculos", filetypes=[("Archivo TXT", "*.txt")])
        if not ruta:
            return
        try:
            resultados = procesar_archivo(ruta)
        except (OSError, UnicodeDecodeError, ErrorDeEntrada) as error:
            messagebox.showerror("No se pudo procesar el archivo", str(error), parent=self)
            return
        destino = filedialog.asksaveasfilename(
            parent=self, title="Guardar resultados", defaultextension=".csv", filetypes=[("Archivo CSV", "*.csv")]
        )
        if not destino:
            return
        try:
            exportar_csv(destino, resultados)
        except OSError as error:
            messagebox.showerror("No se pudo guardar el CSV", str(error), parent=self)
            return
        messagebox.showinfo("Exportación completada", f"Se guardaron {len(resultados)} cálculos.", parent=self)

    def leer_leccion(self) -> None:
        self.voz.hablar(f"{self.leccion_actual.titulo}. {self.leccion_actual.contenido}")
        self.etiqueta_estado.configure(text="Leyendo contenido…")

    def cambiar_tamano_fuente(self, valor: float) -> None:
        tamanio = round(valor)
        self.tamano_fuente.set(tamanio)
        self.etiqueta_tamano.configure(text=f"{tamanio} px")
        self.contenido_texto.configure(font=("Segoe UI", tamanio))

    def cambiar_tema(self, valor: str) -> None:
        modos = {"Sistema": "System", "Claro": "Light", "Oscuro": "Dark"}
        ctk.set_appearance_mode(modos[valor])

    def aplicar_contraste(self) -> None:
        if self.alto_contraste.get():
            self.configure(fg_color=("#FFFFFF", "#000000"))
            self.contenido_texto.configure(text_color=("#000000", "#FFFFFF"))
            self.etiqueta_estado.configure(text="Alto contraste activado")
        else:
            self.configure(fg_color=("#F7F8FC", "#121426"))
            self.contenido_texto.configure(text_color=("#111827", "#F9FAFB"))
            self.etiqueta_estado.configure(text="Contraste estándar activado")

    def elegir_audio(self) -> None:
        if not self.audio_disponible:
            messagebox.showwarning("Audio no disponible", "No se pudo iniciar el sistema de audio en este equipo.", parent=self)
            return
        ruta = filedialog.askopenfilename(parent=self, title="Selecciona una pista", filetypes=[("Audio MP3", "*.mp3")])
        if not ruta:
            return
        try:
            pygame.mixer.music.load(ruta)
            self.pista_actual = ruta
            self.etiqueta_estado.configure(text=f"Audio listo: {os.path.basename(ruta)}")
        except pygame.error as error:
            messagebox.showerror("Audio no disponible", str(error), parent=self)

    def reproducir_audio(self) -> None:
        if not self.pista_actual:
            self.elegir_audio()
            return
        pygame.mixer.music.play(-1)
        self.etiqueta_estado.configure(text="Reproduciendo audio")

    def _registrar_atajos(self) -> None:
        self.bind("<Control-Return>", lambda _evento: self.calcular())
        self.bind("<Control-r>", lambda _evento: self.leer_leccion())
        self.bind("<Control-s>", lambda _evento: self.procesar_lote())


def main() -> None:
    """Inicia la aplicación desde el comando ``guia-probabilidad``."""
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    Aplicacion().mainloop()


if __name__ == "__main__":
    main()
