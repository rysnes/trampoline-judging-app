document.addEventListener("DOMContentLoaded", async function() {
    const response = await fetch("http://127.0.0.1:5000/challenge");
    const data = await response.json();

    if (data.error) {
        document.body.innerHTML = "<p>Error loading challenge.</p>";
        return;
    }

    document.getElementById("challenge-video").src = data.video_url;

    const scoreInputs = document.getElementById("score-inputs");
    data.labels.forEach(label => {
        const inputDiv = document.createElement("div");
        inputDiv.innerHTML = `<label>${label}</label> <input type="number" class="score">`;
        scoreInputs.appendChild(inputDiv);
    });
});

function submitScores() {
    const inputs = document.querySelectorAll(".score");
    let userScores = Array.from(inputs).map(input => parseFloat(input.value) || 0);
    console.log("User Scores:", userScores);
}
