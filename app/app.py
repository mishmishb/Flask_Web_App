''' Flask web app '''

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from script import cuboid_calculator

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = \
    "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="michaelb",
        password="ionostest",
        hostname="85.215.227.215",
        databasename="cuboidcalc",
    )
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_ENGINE_OPTIONS['pool_recycle']"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class SavedResults(db.Model):
    ''' Creates database model '''

    __tablename__ = "saved_results"

    id = db.Column(db.Integer, primary_key=True)
    edge_a = db.Column(db.Float)
    edge_b = db.Column(db.Float)
    edge_c = db.Column(db.Float)
    volume = db.Column(db.Float)
    surface_area = db.Column(db.Float)
    sum_of_edge_lengths = db.Column(db.Float)


saved_errors = ['Empty']

def input_validator(input_a, input_b, input_c, errors):
    ''' Check the inputs exist and are positive numbers '''
    for idx, input_x in enumerate([input_a, input_b, input_c]):
        if input_x:
            try:
                input_x = float(input_x)
            except ValueError:
                errors.append(f'{input_x} is not a number.\n')
            else:
                if input_x < 1:
                    errors.append(f'{input_x} is not a positive number.')
        else:
            errors.append(f'Field {idx+1} is empty.\n')
    errors = (" ").join(errors)
    return errors


@app.route("/", methods=["GET", "POST"])
def main():
    ''' Main function for serving app and data '''
    errors = []

    if request.method == "GET":
        saved_results = SavedResults.query.order_by(SavedResults.id.desc()).limit(30)
        return render_template('index.html', saved_errors=saved_errors,
                                             saved_results=saved_results)

    input_a = request.form['input_a']
    input_b = request.form['input_b']
    input_c = request.form['input_c']

    errors = input_validator(input_a, input_b, input_c, errors)

    if errors:
        saved_errors.insert(0, errors)
    else:
        if len(saved_errors) > 0:
            saved_errors[0] = 'Empty'
        result = cuboid_calculator(input_a, input_b, input_c)

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
    app.run(host='0.0.0.0')
