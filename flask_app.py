from flask import Flask, render_template, redirect, url_for, request
from forms import NumberForm
app = Flask(__name__)
app.config["SECRET_KEY"] = "^&86WDFGD65165!&**"



@app.route("/", methods=["GET", "POST"])
def homepage():
    form = NumberForm()
    if request.method == "POST":
        card_number = form.number.data
        is_valid = validate(card_number)
        result = "Valid" if is_valid else "Invalid"
        return redirect(url_for("card_result", result=result))
    return render_template("index.html", form=form)

def validate(number):
    try:
        if not number.isdigit():
            return False
        reversed_card_number = number[::-1]

        doubled_digits = [int(digit) * 2 if i % 2 == 1 else int(digit) for i, digit in enumerate(reversed_card_number)]

        subtracted_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]

        total_sum = sum(subtracted_digits)

        return total_sum % 10 == 0
    except ValueError:
        return False

@app.route("/card_result/<result>")
def card_result(result):
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)