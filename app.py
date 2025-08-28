from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    expr = ""
    if request.method == "POST":
        expr = request.form["expression"]
        expr = expr.replace('×', '*').replace('÷', '/')
        try:
            result = str(eval(expr))
            expr = result
        except:
            expr = "Error"
    return render_template("index.html", expression=expr)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
