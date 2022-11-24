from flask import Flask, request, render_template

app = Flask(__name__)

from simple_calculator import basic_calculator

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    number_1 = request.form['number_1']
    number_2 = request.form['number_2']
    operation = str(request.form['operation'])

    result = basic_calculator(number_1,number_2,operation)

    return render_template("result.html",prediction_text=str(result))


if __name__ == "__main__":
    app.run(debug=True)