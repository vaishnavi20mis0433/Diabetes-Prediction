from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model from a pickle file
with open('Diabetes.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the form data
    age = int(request.form['age'])
    high_bp = int(request.form['high-bp'])
    high_chol = int(request.form['high-chol'])
    chol_check = int(request.form['chol-check'])
    bmi = float(request.form['bmi'])
    smoker = int(request.form['smoker'])
    stroke = int(request.form['stroke'])
    heart_disease = int(request.form['heart-disease'])
    phys_activity = int(request.form['phys-activity'])
    fruits = int(request.form['fruits'])
    veggies = int(request.form['veggies'])
    alcohol = int(request.form['alcohol'])
    gen_health = int(request.form['gen-health'])
    phys_health = int(request.form['phys-health'])
    sex = request.form['sex']

    # Perform the prediction
    t = [[age, high_bp, high_chol, chol_check, bmi, smoker, stroke, heart_disease, phys_activity, fruits, veggies, alcohol, gen_health, phys_health, sex]]
    prediction = model.predict(t)

    # Process the prediction result
    if prediction[0] == 1:
        result_text = "You have diabetes. Please take care of your health."
    else:
        result_text = "You don't have diabetes. Stay healthy!"

    return render_template('index.html', prediction=result_text)

if __name__ == '__main__' :
    app.run(debug= False)
