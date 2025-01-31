from flask import Flask, request, jsonify, send_file, render_template
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Endpoint para gerar áudio a partir de texto
@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'Texto não fornecido'}), 400
    
    # Gerar áudio com gTTS
    tts = gTTS(text, lang='pt')
    file_path = 'audio.mp3'
    tts.save(file_path)

    return send_file(file_path, mimetype='audio/mp3')

# Endpoint para receber e armazenar áudio do usuário
@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'Arquivo não encontrado'}), 400

    file = request.files['file']
    file.save(os.path.join('uploads', file.filename))

    return jsonify({'message': 'Áudio armazenado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)