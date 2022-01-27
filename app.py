from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/form', methods=['GET', 'POST'])
def foo():
    bar = request.form['test']
    print(bar)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')