from flask import Flask, request, render_template

app = Flask(__name__)

ButtonPressed = 0  
@app.route('/calculator', methods=['GET', 'POST'])
def calc():
    if request.method == "POST":
        if '1' in request.form:
            return render_template("calculator.html", ButtonPressed = 1)
        if '2' in request.form:
            return render_template("calculator.html", ButtonPressed = 2)
        if '3' in request.form:
            return render_template("calculator.html", ButtonPressed = 3)
        if '4' in request.form:
            return render_template("calculator.html", ButtonPressed = 4)
        if '5' in request.form:
            return render_template("calculator.html", ButtonPressed = 5)
        if '6' in request.form:
            return render_template("calculator.html", ButtonPressed = 6)
        if '7' in request.form:
            return render_template("calculator.html", ButtonPressed = 7)
        if '8' in request.form:
            return render_template("calculator.html", ButtonPressed = 8)
        if '9' in request.form:
            return render_template("calculator.html", ButtonPressed = 9)
        if '0' in request.form:
            return render_template("calculator.html", ButtonPressed = 0)

    return render_template("calculator.html", ButtonPressed = ButtonPressed)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')