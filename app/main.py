from flask import Flask, request, jsonify, send_file, render_template
from gtts import gTTS
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, '../uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, 
            static_folder=os.path.join(BASE_DIR, '../static'), 
            template_folder=os.path.join(BASE_DIR, '../templates'))

app.config['FLASK_ENV'] = 'development'
# Ativando o modo de depuração
app.config["DEBUG"] = True

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
    app.run(debug=True, port=5001)