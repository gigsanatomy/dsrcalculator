from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@route('/calculate_dsr', methods=['POST'])
def calculate_dsr():
    data = request.json
    income = data['income']
    expenses = data['expenses']
    loan_amount = data['loan_amount']
    interest_rate = data['interest_rate']
    loan_term = data['loan_term']

    # Example calculation for monthly payment (PMT formula)
    monthly_interest_rate = interest_rate / 100 / 12
    number_of_payments = loan_term * 12
    monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -number_of_payments)

    # Calculate DSR (example)
    dsr = ((expenses + monthly_payment) / income) * 100
    return jsonify({'dsr': dsr})

if __name__ == '__main__':
    app.run(debug=True)
