# ❤️ Heart Disease Prediction

A Flask web application that predicts the likelihood of heart disease from a patient's clinical data, using a trained Support Vector Classifier (SVC) machine learning model. Deployable both locally and as a serverless function on Vercel, with Docker support for platforms like Railway.

**Live demo:** [heart-disease-prediction-ruddy-seven.vercel.app](https://heart-disease-prediction-ruddy-seven.vercel.app)

---

## 🩺 Overview

This app takes 13 standard clinical features (age, blood pressure, cholesterol, ECG results, etc.) and returns a prediction of whether heart disease is likely present, along with a confidence score.

- **Frontend:** HTML, CSS, JavaScript (server-rendered via Flask/Jinja2)
- **Backend:** Flask (Python)
- **ML Model:** Scikit-learn SVC, trained on the [UCI Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)
- **Deployment:** Vercel (serverless) and Docker (Railway or any container host)

---

## ✨ Features

- Clean, responsive UI with dedicated Home, About, Predict, and Contact pages
- Real-time prediction with probability/confidence score
- Single codebase that runs identically in local dev and serverless (Vercel) environments
- Dockerized for easy deployment to any container-based host

---

## 📁 Project Structure

```
heart-disease-prediction/
│
├── app.py                  # Complete Flask application (routes, model loading, prediction logic)
├── api/
│   └── index.py             # Vercel serverless entrypoint (re-exports app from app.py)
├── models/
│   ├── heart_model.pkl      # Trained SVC classifier
│   ├── scaler.pkl           # StandardScaler used for feature preprocessing
│   └── feature_names.pkl    # Feature name/order reference
├── templates/
│   ├── index.html           # Home page
│   ├── about.html           # About page
│   ├── predict.html         # Prediction form + results
│   └── contact.html         # Contact page
├── static/
│   ├── css/                 # Stylesheets
│   ├── js/                  # Client-side scripts
│   └── images/              # Assets (favicon, etc.)
├── dataset/
│   └── heart.csv            # Source dataset used for training
├── requirements.txt         # Python dependencies
├── Dockerfile                # Container build for Railway/other hosts
├── vercel.json               # Vercel deployment configuration
└── README.md
```

---

## 🧠 Model Details

The model expects **13 input features**, in this exact order:

| Feature    | Description                                      |
|------------|---------------------------------------------------|
| `age`      | Age in years                                       |
| `sex`      | Sex (1 = male, 0 = female)                         |
| `cp`       | Chest pain type (0–3)                              |
| `trestbps` | Resting blood pressure (mm Hg)                     |
| `chol`     | Serum cholesterol (mg/dl)                          |
| `fbs`      | Fasting blood sugar > 120 mg/dl (1 = true, 0 = false) |
| `restecg`  | Resting ECG results (0–2)                          |
| `thalach`  | Maximum heart rate achieved                        |
| `exang`    | Exercise-induced angina (1 = yes, 0 = no)           |
| `oldpeak`  | ST depression induced by exercise relative to rest  |
| `slope`    | Slope of the peak exercise ST segment (0–2)         |
| `ca`       | Number of major vessels colored by fluoroscopy (0–3)|
| `thal`     | Thalassemia (0–3)                                   |

Features are scaled using a pre-fit `StandardScaler` before being passed to the SVC model for prediction.

---

## 🚀 Getting Started (Local Development)

### Prerequisites
- Python 3.11+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/khushdutt149-del/heart-disease-prediction.git
cd heart-disease-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app will be available at **http://localhost:5000** (or the port set via the `PORT` environment variable).

---

## ☁️ Deployment

### Vercel

This project is pre-configured for Vercel using `vercel.json`. The single Flask app defined in `app.py` is re-exported through `api/index.py`, which serves as the serverless entrypoint.

```bash
vercel deploy
```

> **Note:** Non-Python assets (model files, templates, static files) must be included via the `includeFiles` config in `vercel.json` for the serverless function to access them at runtime.

### Docker / Railway

Build and run the container:

```bash
docker build -t heart-disease-prediction .
docker run -p 8000:8000 heart-disease-prediction
```

The Dockerfile uses Gunicorn as the production WSGI server.

---

## 🛠️ Tech Stack

- **Flask** — web framework
- **scikit-learn** — model training & inference
- **NumPy / SciPy** — numerical computing
- **joblib** — model serialization
- **Gunicorn** — production WSGI server (Docker deployment)

---

## 📊 Dataset

Trained on the [UCI Machine Learning Repository's Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease), a widely used benchmark dataset in ML for binary classification of heart disease presence.

---

## ⚠️ Disclaimer

This application is built for **educational and portfolio purposes only**. It is **not a medical diagnostic tool** and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for any health concerns.

---

## 👤 Author

**Khush Dutt**
- GitHub: [@khushdutt149-del](https://github.com/khushdutt149-del)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
