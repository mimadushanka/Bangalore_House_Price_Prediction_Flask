#  Bangalore House Price Predictor

A web application built with **Flask** that predicts the price of a house in Bangalore based on user inputs such as square footage, number of bedrooms (BHK), bathrooms, and location.

---

##  Features

- Predict house price using a pre-trained machine learning model.
- Interactive web UI built with **Bootstrap 5**.
- Dynamic dropdown for location (fetched from a JSON file).
- Retains user input on form submission.
- Simple and intuitive user experience.

---
##  Machine Learning Model

- **Algorithm**: Linear Regression
- **Features**: Location, Total Sqft, BHK
- **Libraries**: scikit-learn, pandas
- Trained on cleaned housing dataset
- Pickled model used for inference

---

## Tech Stack

- **Frontend**: HTML5, Bootstrap 5, Jinja2
- **Backend**: Python, Flask
- **ML Model**: Scikit-learn (Linear Regression)
- **Data**: Cleaned and preprocessed real-estate data from Bangalore

---
## Project Structure

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
#  Bangalore House Price Prediction - ML Web App

![appdemo](BangaloreHouse.gif "bangalore House price demo")

This project is a **Machine Learning-powered web application** that predicts house prices in Bangalore based on features like location, BHK, and square footage.

##  Features

- Predicts house prices using a trained **Linear Regression model**
- Interactive **Bootstrap-based UI** with location dropdown
- Model training & evaluation code included
- **Deployed on AWS EC2** with production-ready setup

---

##  Tech Stack

| Layer       | Tool/Framework                   |
|-------------|----------------------------------|
| Frontend    | HTML5, Bootstrap 5               |
| Backend     | Flask                            |
| ML Model    | Scikit-learn, Pandas, NumPy      |
| Deployment  | **AWS EC2**, Gunicorn, Nginx     |
| Packaging   | pipenv (Python dependency manager) |

---



##  Deployment Overview

### 1. **Server Setup**

- Provisioned an **Ubuntu EC2 instance**
- Installed Python, pipenv, and system packages
URL:- http://34.216.141.124/

### 2. **Gunicorn + Nginx**

- Used `Gunicorn` as WSGI HTTP server
- Configured `Nginx` as a reverse proxy
- Exposed port `80` in EC2 Security Group

### 3. **Systemd Service**

- Set up a `houseprice.service` to run Gunicorn in the background
- Enabled auto-start on server reboot

---

##  Run Locally

```bash
# Clone repo
git clone https://github.com/your-username/BHP_Flask.git
cd BHP_Flask

# Install dependencies
pipenv install
pipenv shell

# Run app locally
python server/server.py
