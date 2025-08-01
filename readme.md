# 💳 Python Flask Payment Gateway (Razorpay)

This repository was created as a **step-by-step tutorial** for a friend to learn how to integrate the **Razorpay Payment Gateway** using **Flask (Python)**. It includes everything from setting up the backend, customizing the payment form UI, to integrating Razorpay’s checkout interface.

---

## 🚀 Features

- One-page modern web app
- User-selectable amount and currency
- Razorpay integration with secure `.env` config
- Clean and responsive UI
- Beginner-friendly structure

---

## 🛠️ Tech Stack

- **Backend**: Python + Flask
- **Frontend**: HTML, CSS (Custom modern style)
- **Payments**: Razorpay API
- **Env Management**: `python-dotenv`

---

## 📦 How to Run This App (Step-by-Step)

Follow this guide to clone and run the project on **any machine**.

### 1. Clone the repository

```bash
git clone https://github.com/prasad-gade05/python_flask_payment_gateway
cd python_flask_payment_gateway
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create your `.env` file

Make a `.env` file in the root directory with your Razorpay keys:

```env
RAZORPAY_KEY_ID=your_key_id
RAZORPAY_KEY_SECRET=your_key_secret
```

> 🔒 **Do not share or commit this file. It's ignored using `.gitignore`.**

### 6. Run the Flask app

```bash
python app.py
```

The app will run on [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔪 Test Payments

Use Razorpay’s [Test Mode] credentials to simulate payments.

### Example Test:

1. Put in amount
2. Click **Pay**
3. Enter your **mobile number** in the **"Using as"** field (left side)
4. Click **Pay Later**
5. Choose the last option: **Razorpay xPostpaid**
6. You'll receive an **OTP** on your mobile
7. Enter the **OTP** and click **Submit**
8. On the **demo page**, choose whether to simulate **Payment Success** or **Failure**

---

## 📁 Project Structure

```
.
├── static/
│   └── style.css         # Custom modern CSS
├── templates/
│   └── index.html        # Main page
├── .env                  # Your Razorpay credentials (ignored)
├── .gitignore
├── app.py                # Flask backend logic
├── requirements.txt
└── README.md             # This file
```

---

## 🙇‍♂️ Why I Made This

This is a personal tutorial project to help a friend learn **real-world integration** of payment systems using Python Flask.

Feel free to fork or reuse.

---

## 📬 Contact

If you need help or want to contribute, raise an issue or ping me on GitHub.
