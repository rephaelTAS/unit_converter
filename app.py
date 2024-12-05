from flask import Flask, render_template, request

app = Flask(__name__)

# Conversão de unidades (fatores base para unidades padrão)
LENGTH_CONVERSIONS = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34,
}

WEIGHT_CONVERSIONS = {
    'milligram': 0.000001,
    'gram': 0.001,
    'kilogram': 1,
    'ounce': 0.0283495,
    'pound': 0.453592,
}

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            result = value * LENGTH_CONVERSIONS[from_unit] / LENGTH_CONVERSIONS[to_unit]
        except (ValueError, KeyError):
            result = "Invalid Input"
    return render_template('length.html', result=result, units=LENGTH_CONVERSIONS.keys(), active_page='length')


@app.route('/weight', methods=['GET', 'POST'])
def weight():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            result = value * WEIGHT_CONVERSIONS[from_unit] / WEIGHT_CONVERSIONS[to_unit]
        except (ValueError, KeyError):
            result = "Invalid Input"
    return render_template('weight.html', result=result, units=WEIGHT_CONVERSIONS.keys(), active_page='weight')


@app.route('/temp', methods=['GET', 'POST'])
def temperature():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            if from_unit == to_unit:
                result = value
            elif from_unit == 'Celsius' and to_unit == 'Fahrenheit':
                result = (value * 9/5) + 32
            elif from_unit == 'Celsius' and to_unit == 'Kelvin':
                result = value + 273.15
            elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
                result = (value - 32) * 5/9
            elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == 'Kelvin' and to_unit == 'Celsius':
                result = value - 273.15
            elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
                result = (value - 273.15) * 9/5 + 32
        except (ValueError, KeyError):
            result = "Invalid Input"
    return render_template('temp.html', result=result, units=['Celsius', 'Fahrenheit', 'Kelvin'], active_page='temp')


# Executa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
