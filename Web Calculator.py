from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calculate():
    x = float(request.form['x'])
    y = float(request.form['y'])
    operator = request.form['operator']

    z = 0
    if operator == '+':
        z = x + y
    elif operator == '-':
        z = x - y
    elif operator == '*':
        z = x * y
    elif operator == '/':
        z = x / y

    return render_template('index.html', z=z)

if __name__ == '__main__':
    app.run(debug=True)