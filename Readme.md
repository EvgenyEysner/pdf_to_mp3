# 📚 PDF to MP3 Converter 🎧

[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Convert your PDF documents into audio files using Google's Text-to-Speech technology.

## ✨ Features

- 📝 Extract text from PDF files
- 🌍 Support for multiple languages (English, German, Russian, and more)
- 🎵 Generate high-quality MP3 audio files
- 🧹 Intelligent text cleaning and formatting
- 💻 Simple command-line interface

## 🚀 Installation
1. Clone the repository and install dependencies:

```bash
git clone <repository-url>
cd pdf-to-mp3
```
2. Make sure you have Python 3.8 or higher installed
3. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate  # Windows
```
4. Install pipenv if you haven't already:

```bash
pip install pipenv
```
5. Install the required packages:

```bash
pipenv install
```
## 🎯 Usage

Run the script using pipenv:

```bash
python main.py
```

Follow the prompts to:

1. Enter the path to your PDF file
2. Specify the language code (e.g., 'en' for English, 'de' for German)

The converted MP3 file will be created in the same directory as the PDF file.

## 🌍 Supported Languages

- 🇺🇸 English (en)
- 🇩🇪 German (de)
- 🇷🇺 Russian (ru)
- And many more! The complete list is available through the gTTS library