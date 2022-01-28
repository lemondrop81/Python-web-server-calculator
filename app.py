from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')