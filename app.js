document.getElementById('transaction-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const transactionDetails = document.getElementById('transaction-details').value;
    const features = document.getElementById('features').value.split(',').map(Number);

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            transaction_details: transactionDetails,
            features: features,
        }),
    });
 

    const data = await response.json();
    document.getElementById('result').innerText = `Result: ${data.result}`;
});

let likes = 0;

function incrementLikes() {
    likes++;
    document.getElementById("likes-count").textContent = likes;
}
