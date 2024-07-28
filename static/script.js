// static/script.js

function predict() {
    const form = document.getElementById('irisForm');
    const formData = new FormData(form);

    fetch('/rec', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        displayPrediction(data.result);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayPrediction(prediction) {
    const predictionResultDiv = document.getElementById('predictionResult');
    predictionResultDiv.innerHTML = `<p>Prediction: ${prediction}</p>`;
    
    // Remove 'show' class to trigger animation
    predictionResultDiv.classList.remove('show');
    
    // Add 'predicted' class to change background color
    predictionResultDiv.classList.add('predicted');
    
    // Add 'show' class again to apply fade-in animation
    setTimeout(() => {
        predictionResultDiv.classList.add('show');
    }, 50); // Delay added for smooth transition

    // Optionally, you can reset the background image after prediction
    predictionResultDiv.style.backgroundImage = 'none';
}
