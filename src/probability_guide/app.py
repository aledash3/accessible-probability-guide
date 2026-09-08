"""Interfaz moderna, accesible y bilingüe (ES/EN) de la Guía de Probabilidad."""

from __future__ import annotations

import os
from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk
import pygame
from PIL import Image

from .file_processing import export_csv, exportar_csv, parse_file, procesar_archivo
from .calculations import ErrorDeEntrada, InputError, calculate, calcular
from .content import LECCIONES, LESSONS, Leccion, Lesson, get_lessons
from .speech import SistemaVoz, SpeechEngine


ASSETS_DIR = Path(__file__).with_name("assets")
RECURSOS = ASSETS_DIR
COLOR_PRIMARIO = "#5B5BD6"
COLOR_SECUNDARIO = "#8B5CF6"
COLOR_ACENTO = "#14B8A6"

STRINGS = {
    "es": {
        "window_title": "Guía accesible de probabilidad · v2",
        "sidebar_tag": "PROBABILIDAD",
        "sidebar_title": "Guía de estudio\naccesible",
        "sidebar_desc": "Versión 2.0 · Aprende a contar\nposibilidades con criterio.",
        "sidebar_progress": "{idx} de {total} temas",
        "sidebar_content": "CONTENIDO",
        "sidebar_tip_title": "CONSEJO",
        "sidebar_tip_text": "Si cambiar el orden cambia el resultado, usa una permutación.",
        "module_prefix": "MÓDULO {idx:02d}",
        "btn_read": "🔊  Leer lección",
        "btn_stop": "■  Detener",
        "status_ready": "Listo para estudiar",
        "status_reading": "Leyendo contenido…",
        "status_calc_done": "Cálculo completado",
        "calc_tag": "CALCULADORA",
        "calc_title": "Resuelve en segundos",
        "calc_desc": "Elige la operación e ingresa los valores.",
        "op_perm": "P  Permutación",
        "op_comb": "C  Combinación",
        "label_n": "n",
        "help_n": "Elementos disponibles",
        "label_r": "r",
        "help_r": "Elementos elegidos",
        "btn_calc": "Calcular resultado",
        "res_tag": "RESULTADO",
        "res_prompt": "Ingresa n y r",
        "res_invalid": "Revisa los datos",
        "tools_tag": "HERRAMIENTAS",
        "btn_batch": "↥  Procesar archivo TXT",
        "tools_hint": "Formato: P,n,r o C,n,r",
        "access_tag": "ACCESIBILIDAD",
        "access_size": "Tamaño",
        "access_contrast": "Alto contraste",
        "themes": ["Sistema", "Claro", "Oscuro"],
        "btn_audio": "♫ Audio",
        "dlg_err_title": "Datos inválidos",
        "dlg_batch_title": "Selecciona un archivo de cálculos",
        "dlg_save_title": "Guardar resultados",
        "dlg_batch_err": "No se pudo procesar el archivo",
        "dlg_save_err": "No se pudo guardar el CSV",
        "dlg_done_title": "Exportación completada",
        "dlg_done_msg": "Se guardaron {count} cálculos.",
    },
    "en": {
        "window_title": "Accessible Probability Guide · v2",
        "sidebar_tag": "PROBABILITY",
        "sidebar_title": "Accessible\nStudy Guide",
        "sidebar_desc": "Version 2.0 · Learn combinatorics\nand counting with confidence.",
        "sidebar_progress": "{idx} of {total} topics",
        "sidebar_content": "CONTENT",
        "sidebar_tip_title": "TIP",
        "sidebar_tip_text": "If swapping the order changes the outcome, use a permutation.",
        "module_prefix": "MODULE {idx:02d}",
        "btn_read": "🔊  Read lesson",
        "btn_stop": "■  Stop",
        "status_ready": "Ready to study",
        "status_reading": "Reading lesson content…",
        "status_calc_done": "Calculation complete",
        "calc_tag": "CALCULATOR",
        "calc_title": "Solve in seconds",
        "calc_desc": "Choose operation and enter values.",
        "op_perm": "P  Permutation",
        "op_comb": "C  Combination",
        "label_n": "n",
        "help_n": "Available elements",
        "label_r": "r",
        "help_r": "Selected elements",
        "btn_calc": "Calculate result",
        "res_tag": "RESULT",
        "res_prompt": "Enter n and r",
        "res_invalid": "Check your input values",
        "tools_tag": "TOOLS",
        "btn_batch": "↥  Process TXT file",
        "tools_hint": "Format: P,n,r or C,n,r",
        "access_tag": "ACCESSIBILITY",
        "access_size": "Font Size",
        "access_contrast": "High contrast",
        "themes": ["System", "Light", "Dark"],
        "btn_audio": "♫ Audio",
        "dlg_err_title": "Invalid Input",
        "dlg_batch_title": "Select a calculations file",
        "dlg_save_title": "Save results",
        "dlg_batch_err": "Could not process batch file",
        "dlg_save_err": "Could not save CSV file",
        "dlg_done_title": "Export Completed",
        "dlg_done_msg": "Successfully saved {count} calculations.",
    },
}


class Aplicacion(ctk.CTk):
    """Ventana principal con soporte bilingüe (ES/EN), navegación, cálculos y accesibilidad."""

    def __init__(self, idioma_inicial: str = "es") -> None:
        super().__init__()
        self.idioma = ctk.StringVar(value="en" if str(idioma_inicial).lower().startswith("en") else "es")
        self.lecciones = get_lessons(self.idioma.get())
        self.indice_actual = 0
        self.leccion_actual = self.lecciones[0]

        self.title(self._t("window_title"))
        self.geometry("1440x860")
        self.minsize(1120, 700)
        self.configure(fg_color=("#F7F8FC", "#121426"))

        self.voz = SistemaVoz()
        self.botones_navegacion: list[ctk.CTkButton] = []
        self.tamano_fuente = ctk.IntVar(value=16)
        self.tema = ctk.StringVar(value=self._t("themes")[0])
        self.alto_contraste = ctk.BooleanVar(value=False)
        self.tipo_operacion = ctk.StringVar(value=self._t("op_perm"))
        self.pista_actual: str | None = None
        self.audio_disponible = self._iniciar_audio()

        self._configurar_grilla()
        self._crear_barra_lateral()
        self._crear_area_principal()
        self._crear_panel_calculo()
        self._crear_barra_inferior()
        self._registrar_atajos()
        self.mostrar_leccion(self.lecciones[0], 0)

    def _t(self, key: str, **kwargs) -> str:
        lang = self.idioma.get()
        text = STRINGS.get(lang, STRINGS["es"]).get(key, "")
        if isinstance(text, str) and kwargs:
            return text.format(**kwargs)
        return text

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

        # Selector bilingüe interactivo
        self.selector_idioma = ctk.CTkSegmentedButton(
            self.sidebar,
            values=["Español", "English"],
            command=self.cambiar_idioma,
            selected_color=COLOR_PRIMARIO,
            selected_hover_color="#4848B8",
            height=28,
            corner_radius=7,
        )
        self.selector_idioma.set("English" if self.idioma.get() == "en" else "Español")
        self.selector_idioma.pack(fill="x", padx=26, pady=(24, 0))

        self.lbl_sidebar_tag = ctk.CTkLabel(
            self.sidebar,
            text=self._t("sidebar_tag"),
            font=("Segoe UI", 13, "bold"),
            text_color="#B9BAFF",
        )
        self.lbl_sidebar_tag.pack(anchor="w", padx=26, pady=(16, 0))

        self.lbl_sidebar_title = ctk.CTkLabel(
            self.sidebar,
            text=self._t("sidebar_title"),
            font=("Segoe UI", 25, "bold"),
            justify="left",
        )
        self.lbl_sidebar_title.pack(anchor="w", padx=26, pady=(5, 8))

        self.lbl_sidebar_desc = ctk.CTkLabel(
            self.sidebar,
            text=self._t("sidebar_desc"),
            font=("Segoe UI", 13),
            justify="left",
            text_color="#C8C8E0",
        )
        self.lbl_sidebar_desc.pack(anchor="w", padx=26, pady=(0, 20))

        self.progreso = ctk.CTkProgressBar(
            self.sidebar, height=7, progress_color=COLOR_ACENTO, fg_color="#3B3D68"
        )
        self.progreso.pack(fill="x", padx=26)
        self.progreso.set(1 / len(self.lecciones))

        self.etiqueta_progreso = ctk.CTkLabel(
            self.sidebar,
            text=self._t("sidebar_progress", idx=1, total=len(self.lecciones)),
            font=("Segoe UI", 12),
            text_color="#C8C8E0",
        )
        self.etiqueta_progreso.pack(anchor="w", padx=26, pady=(7, 20))

        self.lbl_sidebar_content = ctk.CTkLabel(
            self.sidebar,
            text=self._t("sidebar_content"),
            font=("Segoe UI", 11, "bold"),
            text_color="#A3A5CD",
        )
        self.lbl_sidebar_content.pack(anchor="w", padx=26, pady=(0, 8))

        for indice, leccion in enumerate(self.lecciones):
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

        self.lbl_sidebar_tip_title = ctk.CTkLabel(
            self.sidebar,
            text=self._t("sidebar_tip_title"),
            font=("Segoe UI", 11, "bold"),
            text_color="#A3A5CD",
        )
        self.lbl_sidebar_tip_title.pack(anchor="w", padx=26, pady=(20, 2))

        self.lbl_sidebar_tip_text = ctk.CTkLabel(
            self.sidebar,
            text=self._t("sidebar_tip_text"),
            wraplength=210,
            justify="left",
            font=("Segoe UI", 12),
            text_color="#D9DAEF",
        )
        self.lbl_sidebar_tip_text.pack(anchor="w", padx=26)

    def _crear_area_principal(self) -> None:
        contenedor = ctk.CTkFrame(self, fg_color="transparent")
        contenedor.grid(row=0, column=1, sticky="nsew", padx=(30, 20), pady=(28, 12))
        contenedor.grid_columnconfigure(0, weight=1)
        contenedor.grid_rowconfigure(2, weight=1)

        cabecera = ctk.CTkFrame(contenedor, fg_color="transparent")
        cabecera.grid(row=0, column=0, sticky="ew")
        cabecera.grid_columnconfigure(0, weight=1)

        self.etiqueta_ruta = ctk.CTkLabel(
            cabecera,
            text=self._t("module_prefix", idx=1),
            font=("Segoe UI", 12, "bold"),
            text_color=COLOR_SECUNDARIO,
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
            acciones,
            text=self._t("btn_read"),
            width=142,
            height=35,
            corner_radius=9,
            fg_color=COLOR_PRIMARIO,
            hover_color="#4848B8",
            command=self.leer_leccion,
        )
        self.boton_leer.pack(side="left")

        self.boton_detener = ctk.CTkButton(
            acciones,
            text=self._t("btn_stop"),
            width=106,
            height=35,
            corner_radius=9,
            fg_color=("#E8E8F3", "#30314A"),
            text_color=("#343550", "#ECECF5"),
            hover_color=("#D7D7E8", "#41425F"),
            command=self.voz.detener,
        )
        self.boton_detener.pack(side="left", padx=8)

        self.etiqueta_estado = ctk.CTkLabel(
            acciones,
            text=self._t("status_ready"),
            font=("Segoe UI", 12),
            text_color=("#64748B", "#A3A8BA"),
        )
        self.etiqueta_estado.pack(side="right")

        self.tarjeta_contenido = ctk.CTkFrame(
            contenedor,
            corner_radius=18,
            fg_color=("#FFFFFF", "#1E2038"),
            border_width=1,
            border_color=("#E8EAF2", "#30334F"),
        )
        self.tarjeta_contenido.grid(row=2, column=0, sticky="nsew")
        self.tarjeta_contenido.grid_columnconfigure(0, weight=1)
        self.tarjeta_contenido.grid_rowconfigure(1, weight=1)

        self.etiqueta_imagen = ctk.CTkLabel(self.tarjeta_contenido, text="")
        self.contenido_texto = ctk.CTkTextbox(
            self.tarjeta_contenido,
            wrap="word",
            corner_radius=0,
            border_spacing=20,
            fg_color="transparent",
            font=("Segoe UI", self.tamano_fuente.get()),
            activate_scrollbars=True,
        )
        self.contenido_texto.grid(row=1, column=0, sticky="nsew", padx=4, pady=5)
        self.contenido_texto.configure(state="disabled")

    def _crear_panel_calculo(self) -> None:
        self.calculadora = ctk.CTkFrame(
            self,
            width=340,
            corner_radius=18,
            fg_color=("#FFFFFF", "#1E2038"),
            border_width=1,
            border_color=("#E8EAF2", "#30334F"),
        )
        self.calculadora.grid(row=0, column=2, sticky="nsew", padx=(0, 30), pady=(28, 12))
        self.calculadora.grid_propagate(False)
        self.calculadora.grid_columnconfigure(0, weight=1)

        self.lbl_calc_tag = ctk.CTkLabel(
            self.calculadora,
            text=self._t("calc_tag"),
            font=("Segoe UI", 12, "bold"),
            text_color=COLOR_SECUNDARIO,
        )
        self.lbl_calc_tag.pack(anchor="w", padx=24, pady=(24, 2))

        self.lbl_calc_title = ctk.CTkLabel(
            self.calculadora,
            text=self._t("calc_title"),
            font=("Segoe UI", 21, "bold"),
        )
        self.lbl_calc_title.pack(anchor="w", padx=24)

        self.lbl_calc_desc = ctk.CTkLabel(
            self.calculadora,
            text=self._t("calc_desc"),
            font=("Segoe UI", 13),
            text_color=("#64748B", "#B8BBCB"),
        )
        self.lbl_calc_desc.pack(anchor="w", padx=24, pady=(2, 18))

        self.selector = ctk.CTkSegmentedButton(
            self.calculadora,
            values=[self._t("op_perm"), self._t("op_comb")],
            variable=self.tipo_operacion,
            command=self._cambiar_operacion,
            selected_color=COLOR_PRIMARIO,
            selected_hover_color="#4848B8",
        )
        self.selector.set(self._t("op_perm"))
        self.selector.pack(fill="x", padx=24, pady=(0, 20))

        self.lbl_campo_n = ctk.CTkLabel(self.calculadora, text=self._t("label_n"), font=("Segoe UI", 13, "bold"))
        self.lbl_campo_n.pack(anchor="w", padx=24)
        self.entrada_n = ctk.CTkEntry(
            self.calculadora, height=40, corner_radius=9, placeholder_text=self._t("help_n"), font=("Segoe UI", 14)
        )
        self.entrada_n.pack(fill="x", padx=24, pady=(4, 12))

        self.lbl_campo_r = ctk.CTkLabel(self.calculadora, text=self._t("label_r"), font=("Segoe UI", 13, "bold"))
        self.lbl_campo_r.pack(anchor="w", padx=24)
        self.entrada_r = ctk.CTkEntry(
            self.calculadora, height=40, corner_radius=9, placeholder_text=self._t("help_r"), font=("Segoe UI", 14)
        )
        self.entrada_r.pack(fill="x", padx=24, pady=(4, 12))

        self.entrada_n.bind("<Return>", lambda _evento: self.calcular())
        self.entrada_r.bind("<Return>", lambda _evento: self.calcular())

        self.btn_calcular = ctk.CTkButton(
            self.calculadora,
            text=self._t("btn_calc"),
            height=42,
            corner_radius=10,
            font=("Segoe UI", 14, "bold"),
            fg_color=COLOR_PRIMARIO,
            hover_color="#4848B8",
            command=self.calcular,
        )
        self.btn_calcular.pack(fill="x", padx=24, pady=(16, 12))

        self.tarjeta_resultado = ctk.CTkFrame(self.calculadora, corner_radius=12, fg_color=("#F0F3FF", "#292C4B"))
        self.tarjeta_resultado.pack(fill="x", padx=24, pady=(0, 18))

        self.lbl_res_tag = ctk.CTkLabel(
            self.tarjeta_resultado,
            text=self._t("res_tag"),
            font=("Segoe UI", 10, "bold"),
            text_color=COLOR_SECUNDARIO,
        )
        self.lbl_res_tag.pack(anchor="w", padx=16, pady=(12, 0))

        self.etiqueta_resultado = ctk.CTkLabel(
            self.tarjeta_resultado,
            text=self._t("res_prompt"),
            font=("Segoe UI", 21, "bold"),
        )
        self.etiqueta_resultado.pack(anchor="w", padx=16, pady=(1, 12))

        self.lbl_tools_tag = ctk.CTkLabel(
            self.calculadora,
            text=self._t("tools_tag"),
            font=("Segoe UI", 11, "bold"),
            text_color=("#64748B", "#A9ADBD"),
        )
        self.lbl_tools_tag.pack(anchor="w", padx=24, pady=(2, 6))

        self.btn_batch = ctk.CTkButton(
            self.calculadora,
            text=self._t("btn_batch"),
            anchor="w",
            height=35,
            corner_radius=8,
            fg_color="transparent",
            border_width=1,
            border_color=("#DCE0EC", "#41445E"),
            text_color=("#41455A", "#E1E3EC"),
            hover_color=("#EFF1F7", "#30334B"),
            command=self.procesar_lote,
        )
        self.btn_batch.pack(fill="x", padx=24, pady=3)

        self.lbl_tools_hint = ctk.CTkLabel(
            self.calculadora,
            text=self._t("tools_hint"),
            font=("Segoe UI", 11),
            text_color=("#64748B", "#A9ADBD"),
        )
        self.lbl_tools_hint.pack(anchor="w", padx=26, pady=(2, 0))

    def _crear_barra_inferior(self) -> None:
        self.barra_inferior = ctk.CTkFrame(self, height=70, corner_radius=0, fg_color=("#FFFFFF", "#1A1C31"))
        self.barra_inferior.grid(row=1, column=1, columnspan=2, sticky="ew")
        self.barra_inferior.grid_propagate(False)

        self.lbl_access_tag = ctk.CTkLabel(
            self.barra_inferior,
            text=self._t("access_tag"),
            font=("Segoe UI", 11, "bold"),
            text_color=COLOR_SECUNDARIO,
        )
        self.lbl_access_tag.pack(side="left", padx=(30, 10))

        self.lbl_access_size = ctk.CTkLabel(self.barra_inferior, text=self._t("access_size"), font=("Segoe UI", 12))
        self.lbl_access_size.pack(side="left")

        self.control_fuente = ctk.CTkSlider(
            self.barra_inferior, from_=13, to=22, number_of_steps=9, width=125, command=self.cambiar_tamano_fuente
        )
        self.control_fuente.set(self.tamano_fuente.get())
        self.control_fuente.pack(side="left", padx=9)

        self.etiqueta_tamano = ctk.CTkLabel(self.barra_inferior, text="16 px", font=("Segoe UI", 12), width=38)
        self.etiqueta_tamano.pack(side="left")

        self.sw_contraste = ctk.CTkSwitch(
            self.barra_inferior,
            text=self._t("access_contrast"),
            variable=self.alto_contraste,
            command=self.aplicar_contraste,
            font=("Segoe UI", 12),
            progress_color=COLOR_ACENTO,
        )
        self.sw_contraste.pack(side="left", padx=20)

        self.menu_tema = ctk.CTkOptionMenu(
            self.barra_inferior,
            values=self._t("themes"),
            variable=self.tema,
            command=self.cambiar_tema,
            width=102,
            corner_radius=8,
            fg_color=COLOR_PRIMARIO,
            button_color="#4848B8",
        )
        self.menu_tema.pack(side="left")

        self.btn_audio = ctk.CTkButton(
            self.barra_inferior,
            text=self._t("btn_audio"),
            width=82,
            height=30,
            corner_radius=8,
            fg_color="transparent",
            border_width=1,
            border_color=("#DCE0EC", "#41445E"),
            text_color=("#41455A", "#E1E3EC"),
            command=self.elegir_audio,
        )
        self.btn_audio.pack(side="right", padx=(8, 30))

        self.btn_play = ctk.CTkButton(
            self.barra_inferior,
            text="▶",
            width=35,
            height=30,
            corner_radius=8,
            fg_color="transparent",
            border_width=1,
            border_color=("#DCE0EC", "#41445E"),
            text_color=("#41455A", "#E1E3EC"),
            command=self.reproducir_audio,
        )
        self.btn_play.pack(side="right")

    def cambiar_idioma(self, nuevo_idioma: str) -> None:
        lang = "en" if "English" in nuevo_idioma or nuevo_idioma.lower().startswith("en") else "es"
        self.idioma.set(lang)
        self.lecciones = get_lessons(lang)
        self.title(self._t("window_title"))

        # Update sidebar
        self.lbl_sidebar_tag.configure(text=self._t("sidebar_tag"))
        self.lbl_sidebar_title.configure(text=self._t("sidebar_title"))
        self.lbl_sidebar_desc.configure(text=self._t("sidebar_desc"))
        self.lbl_sidebar_content.configure(text=self._t("sidebar_content"))
        self.lbl_sidebar_tip_title.configure(text=self._t("sidebar_tip_title"))
        self.lbl_sidebar_tip_text.configure(text=self._t("sidebar_tip_text"))

        # Update navigation buttons
        for idx, btn in enumerate(self.botones_navegacion):
            if idx < len(self.lecciones):
                leccion = self.lecciones[idx]
                btn.configure(text=f" {leccion.icono}   {leccion.titulo}")

        # Update actions & main area
        self.boton_leer.configure(text=self._t("btn_read"))
        self.boton_detener.configure(text=self._t("btn_stop"))
        self.etiqueta_estado.configure(text=self._t("status_ready"))

        # Update calculator
        self.lbl_calc_tag.configure(text=self._t("calc_tag"))
        self.lbl_calc_title.configure(text=self._t("calc_title"))
        self.lbl_calc_desc.configure(text=self._t("calc_desc"))
        op_current = self.tipo_operacion.get()
        is_comb = "C" in op_current or "Comb" in op_current
        self.selector.configure(values=[self._t("op_perm"), self._t("op_comb")])
        new_op = self._t("op_comb") if is_comb else self._t("op_perm")
        self.tipo_operacion.set(new_op)
        self.selector.set(new_op)

        self.lbl_campo_n.configure(text=self._t("label_n"))
        self.entrada_n.configure(placeholder_text=self._t("help_n"))
        self.lbl_campo_r.configure(text=self._t("label_r"))
        self.entrada_r.configure(placeholder_text=self._t("help_r"))
        self.btn_calcular.configure(text=self._t("btn_calc"))
        self.lbl_res_tag.configure(text=self._t("res_tag"))
        self.etiqueta_resultado.configure(text=self._t("res_prompt"))
        self.lbl_tools_tag.configure(text=self._t("tools_tag"))
        self.btn_batch.configure(text=self._t("btn_batch"))
        self.lbl_tools_hint.configure(text=self._t("tools_hint"))

        # Update bottom bar
        self.lbl_access_tag.configure(text=self._t("access_tag"))
        self.lbl_access_size.configure(text=self._t("access_size"))
        self.sw_contraste.configure(text=self._t("access_contrast"))
        self.btn_audio.configure(text=self._t("btn_audio"))
        themes = self._t("themes")
        self.menu_tema.configure(values=themes)
        if self.tema.get() not in themes:
            self.tema.set(themes[0])

        # Refresh active lesson
        self.mostrar_leccion(self.lecciones[self.indice_actual], self.indice_actual)

    def mostrar_leccion(self, leccion: Lesson, indice: int) -> None:
        self.voz.detener()
        self.indice_actual = indice
        self.leccion_actual = leccion
        self.etiqueta_ruta.configure(text=self._t("module_prefix", idx=indice + 1))
        self.etiqueta_titulo.configure(text=leccion.titulo)
        self.etiqueta_resumen.configure(text=leccion.resumen)
        self.etiqueta_estado.configure(text=self._t("status_ready"))
        self.progreso.set((indice + 1) / len(self.lecciones))
        self.etiqueta_progreso.configure(text=self._t("sidebar_progress", idx=indice + 1, total=len(self.lecciones)))

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
        self.etiqueta_resultado.configure(text=self._t("res_prompt"))

    def calcular(self) -> None:
        try:
            n = int(self.entrada_n.get())
            r = int(self.entrada_r.get())
            operacion = "C" if "C" in self.tipo_operacion.get() else "P"
            resultado = calcular(operacion, n, r)
        except (ValueError, ErrorDeEntrada) as error:
            self.etiqueta_resultado.configure(text=self._t("res_invalid"))
            messagebox.showerror(self._t("dlg_err_title"), str(error), parent=self)
            return
        self.etiqueta_resultado.configure(text=f"{operacion}({n}, {r}) = {resultado:,}")
        self.etiqueta_estado.configure(text=self._t("status_calc_done"))

    def procesar_lote(self) -> None:
        ruta = filedialog.askopenfilename(
            parent=self, title=self._t("dlg_batch_title"), filetypes=[("Plain Text", "*.txt")]
        )
        if not ruta:
            return
        try:
            resultados = procesar_archivo(ruta)
        except (OSError, UnicodeDecodeError, ErrorDeEntrada) as error:
            messagebox.showerror(self._t("dlg_batch_err"), str(error), parent=self)
            return
        destino = filedialog.asksaveasfilename(
            parent=self, title=self._t("dlg_save_title"), defaultextension=".csv", filetypes=[("CSV Spreadsheet", "*.csv")]
        )
        if not destino:
            return
        try:
            exportar_csv(destino, resultados)
        except OSError as error:
            messagebox.showerror(self._t("dlg_save_err"), str(error), parent=self)
            return
        messagebox.showinfo(self._t("dlg_done_title"), self._t("dlg_done_msg", count=len(resultados)), parent=self)

    def leer_leccion(self) -> None:
        lang = self.idioma.get()
        self.voz.hablar(f"{self.leccion_actual.titulo}. {self.leccion_actual.contenido}", lang=lang)
        self.etiqueta_estado.configure(text=self._t("status_reading"))

    def cambiar_tamano_fuente(self, valor: float) -> None:
        tamanio = round(valor)
        self.tamano_fuente.set(tamanio)
        self.etiqueta_tamano.configure(text=f"{tamanio} px")
        self.contenido_texto.configure(font=("Segoe UI", tamanio))

    def cambiar_tema(self, valor: str) -> None:
        modos = {
            "Sistema": "System", "System": "System",
            "Claro": "Light", "Light": "Light",
            "Oscuro": "Dark", "Dark": "Dark"
        }
        ctk.set_appearance_mode(modos.get(valor, "System"))

    def aplicar_contraste(self) -> None:
        if self.alto_contraste.get():
            self.configure(fg_color=("#FFFFFF", "#000000"))
            self.contenido_texto.configure(text_color=("#000000", "#FFFFFF"))
            self.etiqueta_estado.configure(text="High contrast" if self.idioma.get() == "en" else "Alto contraste activado")
        else:
            self.configure(fg_color=("#F7F8FC", "#121426"))
            self.contenido_texto.configure(text_color=("#111827", "#F9FAFB"))
            self.etiqueta_estado.configure(text="Standard contrast" if self.idioma.get() == "en" else "Contraste estándar activado")

    def elegir_audio(self) -> None:
        if not self.audio_disponible:
            msg = "Could not initialize audio system." if self.idioma.get() == "en" else "No se pudo iniciar el sistema de audio en este equipo."
            title = "Audio Unavailable" if self.idioma.get() == "en" else "Audio no disponible"
            messagebox.showwarning(title, msg, parent=self)
            return
        ruta = filedialog.askopenfilename(
            parent=self, title="Select audio track", filetypes=[("Audio MP3", "*.mp3")]
        )
        if not ruta:
            return
        try:
            pygame.mixer.music.load(ruta)
            self.pista_actual = ruta
            self.etiqueta_estado.configure(text=f"Audio: {os.path.basename(ruta)}")
        except pygame.error as error:
            messagebox.showerror("Audio Error", str(error), parent=self)

    def reproducir_audio(self) -> None:
        if not self.pista_actual:
            self.elegir_audio()
            return
        pygame.mixer.music.play(-1)
        self.etiqueta_estado.configure(text="Playing audio" if self.idioma.get() == "en" else "Reproduciendo audio")

    def _registrar_atajos(self) -> None:
        self.bind("<Control-Return>", lambda _evento: self.calcular())
        self.bind("<Control-r>", lambda _evento: self.leer_leccion())
        self.bind("<Control-s>", lambda _evento: self.procesar_lote())


def main() -> None:
    """Inicia la aplicación desde el comando ``guia-probabilidad``."""
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    Aplicacion().mainloop()


if __name__ == "__main__":
    main()
