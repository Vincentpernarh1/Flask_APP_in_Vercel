from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    data = []

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2

            data.append({"num1": num1, "num2": num2, "operation": operation, "result": result})
        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result, data=data)


if __name__ == "__main__":
    app.run(debug=True)