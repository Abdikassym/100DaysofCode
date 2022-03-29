import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

all_cafes = Cafe.query.all()

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def get_random():
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe={
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "has_sockets": random_cafe.has_sockets,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price
    })


@app.route('/all')
def get_all():
    cafe_list = []
    for i in all_cafes:
        current_cafe = dict(
            name=i.name,
            map_url=i.map_url,
            img_url=i.img_url,
            location=i.location,
            has_sockets=i.has_sockets,
            has_toilet=i.has_toilet,
            has_wifi=i.has_wifi,
            can_take_calls=i.can_take_calls,
            coffee_price=i.coffee_price
        )
        cafe_list.append(current_cafe)
    return jsonify(cafes=[cafe for cafe in cafe_list])


@app.route('/search')
def search_cafe():
    query_location = request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=dict(name=cafe.name,
                                 map_url=cafe.map_url,
                                 img_url=cafe.img_url,
                                 location=cafe.location,
                                 has_sockets=cafe.has_sockets,
                                 has_toilet=cafe.has_toilet,
                                 has_wifi=cafe.has_wifi,
                                 can_take_calls=cafe.can_take_calls,
                                 coffee_price=cafe.coffee_price))
    else:
        return jsonify(error={"not found": "Sorry, we do not have a cafe at this location."})

# HTTP GET - Read Record

# HTTP POST - Create Record


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            seats=request.form.get("seats"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            coffee_price=request.form.get("coffee_price"),
            )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response="success")


## HTTP PUT/PATCH - Update Record

@app.route('/update-price/<cafe_id>', methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    current_cafe = db.session.query(Cafe).get(cafe_id)
    if current_cafe:
        current_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response=f"Successfully changed price to {current_cafe.coffee_price}")
    else:
        return jsonify(response="Failed to change the price. No cafe id found.")


## HTTP DELETE - Delete Record

@app.route('/report-closed/<cafe_id>', methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe_to_delete = db.session.query(Cafe).get(cafe_id)
    api_key = request.args.get("api_key")
    if cafe_to_delete:

        if api_key == "TopSecretAPIKey":
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": f"{cafe_to_delete.name} was successfully deleted."})
        else:
            return jsonify(response={"failure": f"Incorrect API Key."})

    else:
        return jsonify(response={'failure': "There is no provided cafe id."})


if __name__ == '__main__':
    app.run(debug=True)
