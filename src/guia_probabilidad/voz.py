"""Servicios de lectura de contenido para la interfaz."""

from __future__ import annotations

import threading

import pyttsx3


class SistemaVoz:
    """Reproduce texto en un hilo para no bloquear la interfaz."""

    def __init__(self) -> None:
        self._engine = None
        self._hablando = False

    @property
    def hablando(self) -> bool:
        return self._hablando

    def hablar(self, texto: str) -> None:
        if self._hablando or not texto.strip():
            return

        def reproducir() -> None:
            self._hablando = True
            try:
                self._engine = pyttsx3.init()
                self._engine.setProperty("rate", 165)
                self._engine.setProperty("volume", 0.8)
                self._engine.say(texto)
                self._engine.runAndWait()
            finally:
                if self._engine:
                    self._engine.stop()
                self._engine = None
                self._hablando = False

        threading.Thread(target=reproducir, daemon=True).start()

    def detener(self) -> None:
        if self._engine:
            self._engine.stop()
        self._hablando = False
