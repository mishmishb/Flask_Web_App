from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import redirect
from script import cuboid_calculator

app = Flask(__name__)
app.config["DEBUG"] = True

saved_results = ['Empty']
saved_volume = ['Empty']
saved_surface_area = ['Empty']
saved_sum_of_edge_lengths = ['Empty']



@app.route("/", methods=["GET", "POST"])
def main():
    errors = ""

    if request.method == "GET":
        return render_template('index.html').format(errors=errors,
                                                    saved_volume=saved_volume,
                                                    saved_surface_area=saved_surface_area,
                                                    saved_sum_of_edge_lengths=saved_sum_of_edge_lengths,
                                                    saved_results=saved_results)
    
    if request.method == "POST":
        input_a = None
        input_b = None
        input_c = None
        
        try:
            input_a = float(request.form["input_a"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["input_a"])
        try:
            input_b = float(request.form["input_b"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["input_b"])
        try:
            input_c= float(request.form["input_c"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["input_c"])

        result = cuboid_calculator(input_a, input_b, input_c)
        saved_volume.insert(0, result['volume'])
        saved_surface_area.insert(0, result['surface_area'])
        saved_sum_of_edge_lengths.insert(0, result['sum_of_edge_lengths'])
        saved_results.insert(0, result)

        return redirect(url_for('main'))


if __name__ == "__main__":
    app.run()
