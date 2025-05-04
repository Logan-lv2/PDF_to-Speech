async function convertPdfToAudio() {
    const file = document.getElementById("pdf-upload").files[0];
    if (!file) return alert("📢 Sélectionnez un PDF !");

    const audioPlayer = document.getElementById("audio-player");
    audioPlayer.hidden = true;

    const formData = new FormData();
    formData.append("pdf", file);

    try {
        const response = await fetch("/convert-pdf", {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            const audioBlob = await response.blob();
            audioPlayer.src = URL.createObjectURL(audioBlob);
            audioPlayer.hidden = false;
        } else {
            alert("Erreur de conversion ❌");
        }
    } catch (error) {
        console.error("Erreur :", error);
    }
}