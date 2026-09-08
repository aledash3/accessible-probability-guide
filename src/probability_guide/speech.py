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

    def speak(self, text: str, lang: str = "es") -> None:
        if self._is_speaking or not text.strip():
            return

        def _play() -> None:
            self._is_speaking = True
            try:
                self._engine = pyttsx3.init()
                self._engine.setProperty("rate", 165)
                self._engine.setProperty("volume", 0.8)
                
                # Auto-detect language voice if available
                target_lang = "en" if str(lang).lower().startswith("en") else "es"
                for voice in self._engine.getProperty("voices"):
                    name_lower = voice.name.lower()
                    langs = [str(l).lower() for l in getattr(voice, "languages", [])]
                    if target_lang == "en" and ("english" in name_lower or "zira" in name_lower or any("en" in l for l in langs)):
                        self._engine.setProperty("voice", voice.id)
                        break
                    elif target_lang == "es" and ("spanish" in name_lower or "helena" in name_lower or any("es" in l for l in langs)):
                        self._engine.setProperty("voice", voice.id)
                        break

                self._engine.say(text)
                self._engine.runAndWait()
            finally:
                if self._engine:
                    self._engine.stop()
                self._engine = None
                self._is_speaking = False

        threading.Thread(target=_play, daemon=True).start()

    def hablar(self, text: str, lang: str = "es") -> None:
        self.speak(text, lang=lang)

    def stop(self) -> None:
        if self._engine:
            self._engine.stop()
        self._is_speaking = False

    def detener(self) -> None:
        self.stop()


SistemaVoz = SpeechEngine
