from flask import Flask, request, render_template
import MyMath

app = Flask(__name__)

ButtonPressed = 0


@app.route('/', methods=['GET', 'POST'])


def calc():
    """contains calculator functions"""
    if request.method == "POST":
        if '1' in request.form:
            MyMath.nums.append(1)
            return render_template("calculator.html",
                                   ButtonPressed="You entered 1")
        if '2' in request.form:
            MyMath.nums.append(2)
            return render_template("calculator.html",
                                   ButtonPressed="You entered 2")
        if '3' in request.form:
            MyMath.nums.append(3)
            return render_template("calculator.html",
                                   ButtonPressed="You entered 3")
        if '4' in request.form:
            MyMath.nums.append(4)
            return render_template("calculator.html",
                                   ButtonPressed="You entered 4")
        if '5' in request.form:
            MyMath.nums.append(5)
            return render_template("calculator.html",
                                   ButtonPressed="You entered 5")
        if '6' in request.form:
            MyMath.nums.append(6)
            return render_template("calculator.html",
                                   ButtonPressed="You entered 6")
        if '7' in request.form:
            MyMath.nums.append(7)
            return render_template("calculator.html",
                                   ButtonPressed="You entered 7")
        if '8' in request.form:
            MyMath.nums.append(8)
            return render_template("calculator.html",
                                   ButtonPressed="You entered 8")
        if '9' in request.form:
            MyMath.nums.append(9)
            return render_template("calculator.html",
                                   ButtonPressed="You entered 9")
        if '0' in request.form:
            MyMath.nums.append(0)
            return render_template("calculator.html",
                                   ButtonPressed="You entered 0")
        if 'clear' in request.form:
            MyMath.nums.clear()
        if 'calculate' in request.form:
            math = MyMath.MyMath(1)
            test = "Standard deviation of nums: " + \
                str(round(math.standardDeviation(MyMath.nums), 4)) + \
                " the average of nums: " + \
                str(round(math.avg(MyMath.nums), 3)) + \
                " the largest of nums: " + \
                str(math.largest(MyMath.nums))
            return render_template("calculator.html", ButtonPressed=test)
    return render_template("calculator.html", ButtonPressed=ButtonPressed)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')