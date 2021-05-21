from flask import Flask, render_template, request
from script import cuboid_calculator

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def main():
    errors = ""
    if request.method == "POST":
        input_a = None
        input_b = None
        input_c = None
        try:
            input_a = float(request.form["input_a"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["input_a"])
        try:
            input_a = float(request.form["input_b"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["input_b"])
        try:
            input_a = float(request.form["input_c"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["input_c"])
    return render_template('index.html').format(errors=errors)


if __name__ == "__main__":
    app.run()