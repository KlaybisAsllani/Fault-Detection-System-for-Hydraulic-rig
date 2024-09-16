document.getElementById('monitor-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const temperature = document.getElementById('temperature').value;
    const pressure = document.getElementById('pressure').value;
    const flow_rate = document.getElementById('flow_rate').value;
    const pH = document.getElementById('pH').value;

    const data = {
        temperature: parseFloat(temperature),
        pressure: parseFloat(pressure),
        flow_rate: parseFloat(flow_rate),
        pH: parseFloat(pH)
    };

    fetch('/monitor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = `Prediction: ${result.prediction}, Diagnosis: ${result.diagnosis}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});