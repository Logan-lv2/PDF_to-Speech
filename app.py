from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfReader
from gtts import gTTS
import os

app = Flask(__name__)

# Page principale
@app.route("/")
def home():
    return render_template("index.html")

# Conversion PDF en audio
@app.route("/convert-pdf", methods=["POST"])
def convert_pdf():
    if "pdf" not in request.files:
        return "Aucun fichier uploadé !", 400
    
    pdf = request.files["pdf"]
    if pdf.filename == "":
        return "Fichier invalide !", 400

    # Extraction du texte
    text = ""
    reader = PdfReader(pdf)
    for page in reader.pages:
        text += page.extract_text() or ""  # Gère les pages vides

    # Conversion en audio
    tts = gTTS(text=text, lang="fr")
    tts.save("output.mp3")

    return send_file("output.mp3", mimetype="audio/mp3")

if __name__ == "__main__":
    app.run(debug=True)