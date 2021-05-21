from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from script import cuboid_calculator

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="michaelb",
    password="ionostest",
    hostname="85.215.227.215",
    databasename="cuboidcalc",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class SavedResults(db.Model):

    __tablename__ = "saved_results"

    id = db.Column(db.Integer, primary_key=True)
    edge_a = db.Column(db.Float)
    edge_b = db.Column(db.Float)
    edge_c = db.Column(db.Float)
    volume = db.Column(db.Float)
    surface_area = db.Column(db.Float)
    sum_of_edge_lengths = db.Column(db.Float)




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