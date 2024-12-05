from flask import Flask, render_template, request

app = Flask(__name__)

# Conversões de comprimento
LENGTH_CONVERSIONS = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34
}

# Conversões de peso
WEIGHT_CONVERSIONS = {
    'milligram': 0.001,
    'gram': 1,
    'kilogram': 1000,
    'ounce': 28.3495,
    'pound': 453.592
}

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = value * LENGTH_CONVERSIONS[from_unit] / LENGTH_CONVERSIONS[to_unit]
    return render_template('length.html', result=result, units=LENGTH_CONVERSIONS.keys())

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = value * WEIGHT_CONVERSIONS[from_unit] / WEIGHT_CONVERSIONS[to_unit]
    return render_template('weight.html', result=result, units=WEIGHT_CONVERSIONS.keys())

@app.route('/temp', methods=['GET', 'POST'])
def temp():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                result = value * 9/5 + 32
            elif to_unit == 'Kelvin':
                result = value + 273.15
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                result = (value - 32) * 5/9
            elif to_unit == 'Kelvin':
                result = (value - 32) * 5/9 + 273.15
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                result = value - 273.15
            elif to_unit == 'Fahrenheit':
                result = (value - 273.15) * 9/5 + 32

    return render_template('temp.html', result=result, units=['Celsius', 'Fahrenheit', 'Kelvin'])

if __name__ == '__main__':
    app.run(debug=True)
