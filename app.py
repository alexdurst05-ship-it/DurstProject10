from flask import Flask, render_template, request

# Tax Brackets
# $0 - $1000 = 10%
# $1000 - $10000 = 20%
# Above $10000 = 30%

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    income_text = request.form.get("income", "")

    try:
        income = float(income_text)
    except ValueError:
        return "Error: Please enter a valid number", 400

    if income < 0:
        return "Error: Income cannot be negative", 400

    if income <= 1000:
        tax = income * 0.10
    elif income <= 10000:
        tax = (1000 * 0.10) + ((income - 1000) * 0.20)
    else:
        tax = (1000 * 0.10) + (9000 * 0.20) + ((income - 10000) * 0.30)

    income_display = f"${income:.2f}"
    tax_display = f"${tax:.2f}"

    return render_template("result.html", income=income_display, tax=tax_display)

if __name__ == "__main__":
    app.run(debug=True)
