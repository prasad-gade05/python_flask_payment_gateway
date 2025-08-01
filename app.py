from flask import Flask, render_template, request, jsonify
import razorpay
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

app = Flask(__name__)

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/create-order', methods=['POST'])
def create_order():
    data = request.get_json()
    amount = int(data['amount']) * 100  # Convert ₹ to paise
    currency = data.get('currency', 'INR')

    order = client.order.create({
        "amount": amount,
        "currency": currency,
        "payment_capture": 1
    })

    return jsonify({
        "order_id": order['id'],
        "amount": amount,
        "currency": currency,
        "key": RAZORPAY_KEY_ID
    })

@app.route('/payment-verification', methods=['POST'])
def verify_payment():
    print("Payment verified:", request.form)
    return "Payment Successful!"

if __name__ == '__main__':
    app.run(debug=True)
