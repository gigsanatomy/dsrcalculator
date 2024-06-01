document.getElementById('dsr-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const income = parseFloat(document.getElementById('income').value);
    const expenses = parseFloat(document.getElementById('expenses').value);
    const loan_amount = parseFloat(document.getElementById('loan_amount').value);
    const interest_rate = parseFloat(document.getElementById('interest_rate').value);
    const loan_term = parseFloat(document.getElementById('loan_term').value);

    fetch('/calculate_dsr', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ income: income, expenses: expenses, loan_amount: loan_amount, interest_rate: interest_rate, loan_term: loan_term })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'DSR: ' + data.dsr + '%';
    });
});
