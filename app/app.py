from flask import Flask, redirect, render_template, request, url_for
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




saved_volume = ['Empty']
saved_surface_area = ['Empty']
saved_sum_of_edge_lengths = ['Empty']
saved_errors = ['Empty']

@app.route("/", methods=["GET", "POST"])
def main():
    errors = []

    if request.method == "GET":
        saved_results = SavedResults.query.order_by(SavedResults.id.desc()).limit(30)
        return render_template('index.html', saved_errors=saved_errors,
                                            saved_volume=saved_volume,
                                            saved_surface_area=saved_surface_area,
                                            saved_sum_of_edge_lengths=saved_sum_of_edge_lengths,
                                            saved_results=saved_results)
    
    input_a = request.form['input_a']
    input_b = request.form['input_b']
    input_c = request.form['input_c']
    for idx, input_x in enumerate([input_a, input_b, input_c]):
        if input_x:
            try:
                input_x = float(input_x)
            except:
                errors.append(f'{input_x} is not a number.\n')
            else:
                if input_x < 1:
                    errors.append(f'{input_x} is not a positive number.')
        else:
            errors.append(f'Field {idx+1} is empty.\n')
    errors = (" ").join(errors)

    if errors:
        saved_errors.insert(0, errors)
    else:
        if len(saved_errors) > 0:
            saved_errors.pop()
        result = cuboid_calculator(input_a, input_b, input_c)
        saved_volume.insert(0, result['volume'])
        saved_surface_area.insert(0, result['surface_area'])
        saved_sum_of_edge_lengths.insert(0, result['sum_of_edge_lengths'])

        db_entries = SavedResults(edge_a=input_a,
                                edge_b=input_b,
                                edge_c=input_c,
                                volume=result['volume'],
                                surface_area=result['surface_area'],
                                sum_of_edge_lengths=result['sum_of_edge_lengths'])
        db.session.add(db_entries)
        db.session.commit()
    

    return redirect(url_for('main'))


if __name__ == "__main__":
    app.run()