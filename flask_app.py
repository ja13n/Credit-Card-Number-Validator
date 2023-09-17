from flask import Flask, render_template, redirect, url_for, request
from forms import NumberForm
app = Flask(__name__)
app.config["SECRET_KEY"] = "^&86WDFGD65165!&**"


@app.route("/", methods=["GET", "POST"])
def homepage():
    form = NumberForm()
    if request.method == "POST":
        card_number = form.number.data
        print(type(card_number))
        is_valid = validate(card_number)
        result = "Valid" if is_valid else "Invalid"
        return redirect(url_for("card_result", result=result))
    return render_template("Validator.html", form=form)

def validate(number):
    try:
        number = ''.join(filter(str.isdigit, number))
        # Check if the number is empty or has non-digit characters
        if not number.isdigit():
            return False
        total_sum = 0
        num_digits = len(number)
        odd_even = num_digits & 1

        for i in range(num_digits):
            digit = int(number[i])

            if not ((i & 1) ^ odd_even):
                digit *= 2
            if digit > 9:
                digit -= 9

            total_sum += digit

        return total_sum % 10 == 0
    except ValueError:
        return False

@app.route("/card_result/<result>")
def card_result(result):
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)