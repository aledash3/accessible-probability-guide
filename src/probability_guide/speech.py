"""Asynchronous Text-to-Speech (TTS) narration engine."""

from __future__ import annotations

import threading

import pyttsx3


class SpeechEngine:
    """Plays text narration in a daemon worker thread to prevent UI freezing."""

    def __init__(self) -> None:
        self._engine = None
        self._is_speaking = False

    @property
    def is_speaking(self) -> bool:
        return self._is_speaking

    @property
    def hablando(self) -> bool:
        return self._is_speaking

    def speak(self, text: str) -> None:
        if self._is_speaking or not text.strip():
            return

        def _play() -> None:
            self._is_speaking = True
            try:
                self._engine = pyttsx3.init()
                self._engine.setProperty("rate", 165)
                self._engine.setProperty("volume", 0.8)
                self._engine.say(text)
                self._engine.runAndWait()
            finally:
                if self._engine:
                    self._engine.stop()
                self._engine = None
                self._is_speaking = False

        threading.Thread(target=_play, daemon=True).start()

    def hablar(self, text: str) -> None:
        self.speak(text)

    def stop(self) -> None:
        if self._engine:
            self._engine.stop()
        self._is_speaking = False

    def detener(self) -> None:
        self.stop()


SistemaVoz = SpeechEngine
