from flask import Flask, render_template, request

app = Flask(__name__)

# HOME PAGE
@app.route("/")
def home():
    return render_template("home.html")


# PRIME CHECKER
@app.route("/prime", methods=["GET", "POST"])
def prime():

    result = ""

    if request.method == "POST":

        number = int(request.form["number"])

        prime = True

        if number <= 1:
            prime = False

        else:
            for i in range(2, number):
                if number % i == 0:
                    prime = False
                    break

        if prime:
            result = f"{number} is a Prime Number"
        else:
            result = f"{number} is Not a Prime Number"

    return render_template("prime.html", result=result)


# DIGIT SUM
@app.route("/digitsum", methods=["GET", "POST"])
def digitsum():

    result = ""

    if request.method == "POST":

        number = request.form["number"]

        total = sum(int(digit) for digit in number)

        result = f"Sum of Digits = {total}"

    return render_template("digitsum.html", result=result)


# VOWEL COUNTER
@app.route("/vowels", methods=["GET", "POST"])
def vowels():

    result = ""

    if request.method == "POST":

        text = request.form["text"]

        vowels = "aeiouAEIOU"

        count = sum(1 for char in text if char in vowels)

        result = f"Total Vowels = {count}"

    return render_template("vowels.html", result=result)


# SQUARES AND CUBES
@app.route("/squares")
def squares():

    data = []

    for i in range(1, 11):

        data.append({
            "number": i,
            "square": i * i,
            "cube": i * i * i
        })

    return render_template("squares.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)