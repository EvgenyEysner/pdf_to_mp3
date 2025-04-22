from pathlib import Path
import re
import pdfplumber
from art import tprint
from gtts import gTTS
from typing import Optional


class PdfToSpeechConverter:
    def __init__(self):
        self.supported_languages = self._get_supported_languages()

    def _get_supported_languages(self) -> dict:
        try:
            from gtts.lang import tts_langs

            return tts_langs()
        except (ImportError, AttributeError):
            return {"en": "English", "de": "German", "ru": "Russian"}

    def convert_pdf_to_mp3(
        self, pdf_path: Path, language: str, output_path: Optional[Path] = None
    ) -> Path:
        self._validate_input(pdf_path, language)

        text = self._extract_and_clean_text(pdf_path)
        output_file = self._get_output_path(pdf_path, output_path)

        self._text_to_speech(text, language, output_file)
        return output_file

    def _validate_input(self, pdf_path: Path, language: str) -> None:
        if not pdf_path.exists():
            raise FileNotFoundError(f"File {pdf_path} not found")
        if pdf_path.suffix.lower() != ".pdf":
            raise ValueError("Invalid file format. Only PDF files are supported")
        if language not in self.supported_languages:
            raise ValueError(
                f"Unsupported language. Available options: {', '.join(self.supported_languages.keys())}"
            )

    def _extract_and_clean_text(self, pdf_path: Path) -> str:
        with pdfplumber.open(pdf_path) as pdf:
            text_pages = [page.extract_text() or "" for page in pdf.pages]

        full_text = " ".join(text_pages)
        return self._clean_text(full_text)

    def _clean_text(self, text: str) -> str:
        text = re.sub(r"-\n", "", text)  # Silbentrennung entfernen
        text = re.sub(r"\n", " ", text)  # Neue Zeilen durch Leerzeichen ersetzen
        text = re.sub(r"\s+", " ", text)  # Mehrfache Leerzeichen reduzieren
        return text.strip()

    def _get_output_path(self, pdf_path: Path, output_path: Optional[Path]) -> Path:
        if output_path:
            if output_path.is_dir():
                return output_path / f"{pdf_path.stem}.mp3"
            return output_path
        return pdf_path.with_suffix(".mp3")

    def _text_to_speech(self, text: str, language: str, output_file: Path) -> None:
        if not text:
            raise ValueError("No text found in PDF document")

        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_file)


def run_cli():
    tprint("PDF->MP3", font="bulbhead")
    converter = PdfToSpeechConverter()

    try:
        pdf_path = Path(input("\nEnter PDF file path: ").strip())
        language = input("Enter language code (e.g., 'en', 'de'): ").strip().lower()

        output_file = converter.convert_pdf_to_mp3(pdf_path, language)
        print(f"\nSuccess! Created audio file: {output_file}")

    except Exception as e:
        print(f"\nError: {str(e)}")
    finally:
        print("\n--- Process completed ---")


if __name__ == "__main__":
    run_cli()
