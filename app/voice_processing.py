from gtts import gTTS
import os

# Criar pastas se não existirem
os.makedirs("uploads", exist_ok=True)
os.makedirs("generated_audio", exist_ok=True)

def generate_audio_file(text):
    """Gera um arquivo de áudio a partir de texto e salva na pasta generated_audio"""
    file_path = f"generated_audio/audio.mp3"
    tts = gTTS(text, lang='pt')
    tts.save(file_path)
    return file_path

def save_uploaded_audio(file):
    """Salva um arquivo de áudio enviado pelo usuário na pasta uploads"""
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    return file_path
