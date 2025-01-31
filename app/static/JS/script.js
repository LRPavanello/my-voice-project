let recorder;
let audioChunks = [];

// Função para gerar áudio a partir de texto
async function generateAudio() {
    const text = document.getElementById("textToSpeech").value;
    if (text.trim() === "") {
        alert("Por favor, digite um texto!");
        return;
    }

    const response = await fetch('/generate_audio', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text })
    });

    if (response.ok) {
        const audioBlob = await response.blob();
        const audioUrl = URL.createObjectURL(audioBlob);
        const audioPlayer = document.getElementById("audioPlayer");
        audioPlayer.src = audioUrl;
    } else {
        alert("Erro ao gerar áudio!");
    }
}

// Função para começar a gravação
async function startRecording() {
    const status = document.getElementById("status");
    status.textContent = "Gravando...";

    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = new MediaRecorder(stream);

    recorder.ondataavailable = event => {
        audioChunks.push(event.data);
    };

    recorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const formData = new FormData();
        formData.append('file', audioBlob, 'user_voice.wav');

        // Enviar o áudio para o servidor
        fetch('/upload_audio', {
            method: 'POST',
            body: formData
        }).then(response => response.json())
          .then(data => {
              alert('Áudio enviado com sucesso!');
              status.textContent = "Gravação concluída!";
          }).catch(error => {
              console.error(error);
              status.textContent = "Erro ao enviar o áudio!";
          });
    };

    recorder.start();
}

// Função para parar a gravação
function stopRecording() {
    recorder.stop();
    const status = document.getElementById("status");
    status.textContent = "Gravação parada.";
}

// Função para enviar o arquivo MP3
async function sendAudio() {
    const audioFile = document.getElementById("audioFile").files[0];
    if (!audioFile) {
        alert("Por favor, escolha um arquivo MP3!");
        return;
    }

    const formData = new FormData();
    formData.append('file', audioFile);

    const response = await fetch('/upload_audio', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    if (data.message) {
        alert(data.message);
    } else {
        alert("Erro ao enviar o arquivo!");
    }
}
