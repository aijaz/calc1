from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/calculator", methods=['POST'])
@app.post("/calculator")
def calculator():
    op1 = int(request.values.get('operand1'))
    op2 = int(request.values.get('operand2'))
    op = request.values.get('operator')
    guess = int(request.values.get('guess'))

    answer = None

    if op == '+':
        answer = op1 + op2
    elif op == '-':
        answer = op1 - op2
    elif op == '*':
        answer = op1 * op2
    else:
        return "I'm not smart enough to understand this operator"

    if answer == guess:
        return f"That's correct! The answer is indeed {answer}"
    else:
        return f"Sorry. The correct answer is {answer}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
