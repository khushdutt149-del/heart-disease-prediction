from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(
    os.path.join(BASE_DIR, "models", "heart_model.pkl")
)

scaler = joblib.load(
    os.path.join(BASE_DIR, "models", "scaler.pkl")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        age = float(request.form["age"])
        sex = float(request.form["sex"])
        cp = float(request.form["cp"])
        trestbps = float(request.form["trestbps"])
        chol = float(request.form["chol"])
        fbs = float(request.form["fbs"])
        restecg = float(request.form["restecg"])
        thalach = float(request.form["thalach"])
        exang = float(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = float(request.form["slope"])
        ca = float(request.form["ca"])
        thal = float(request.form["thal"])

        data = np.array([[

            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal

        ]])

        data = scaler.transform(data)

        prediction = model.predict(data)[0]

        probability = round(model.predict_proba(data).max() * 100, 2)

        if prediction == 1:
            result = "❤️ Heart Disease Detected"
        else:
            result = "💚 No Heart Disease Detected"

        return render_template(
            "predict.html",
            prediction=result,
            probability=probability
        )

    return render_template("predict.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)