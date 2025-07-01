# 🏠 Bangalore House Price Predictor

A web application built with **Flask** that predicts the price of a house in Bangalore based on user inputs such as square footage, number of bedrooms (BHK), bathrooms, and location.

---

## 🚀 Features

- Predict house price using a pre-trained machine learning model.
- Interactive web UI built with **Bootstrap 5**.
- Dynamic dropdown for location (fetched from a JSON file).
- Retains user input on form submission.
- Simple and intuitive user experience.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, Bootstrap 5, Jinja2
- **Backend**: Python, Flask
- **ML Model**: Scikit-learn (Linear Regression)
- **Data**: Cleaned and preprocessed real-estate data from Bangalore

---

## 📂 Project Structure

BHP_Flask/
│
├── artifacts/
│ ├── banglore_home_prices_model.pickle
│ └── columns.json
│
├── server/
│ └── server.py
│
├── templates/
│ └── client/
│ └── app.html
│
├── util.py
└── README.md