from flask import Flask, make_response, request
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hero_powers.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/heroes', methods=["GET"])
def get_heroes():
    heroes = []

    for hero in Hero.query.all():
        heroes.append(hero.to_dict())

    return make_response(heroes, 200)

@app.route('/heroes/<int:id>', methods=["GET"])
def get_hero_by_id(id):
    hero = Hero.query.get(id)

    return make_response(hero.to_dict(), 200)

@app.route('/powers', methods=["GET"])
def get_powers():
    powers = []

    for power in Power.query.all():
        powers.append(power.to_dict())

    return make_response(powers, 200)

@app.route('/powers/<int:id>', methods=["GET"])
def get_power_by_id(id):
    power = Power.query.get(id)

    return make_response(power.to_dict(), 200)

@app.route('/powers/<int:id>', methods=["PATCH"])
def update_power_description(id):
    power = Power.query.get(id)

    data = request.get_json()
    power.description = data.get("description")
    db.session.commit()

    return make_response(power.to_dict(), 200)

@app.route('/heropowers', methods=["POST"])
def add_hero_power():
    data = request.get_json()

    new_hero_power = HeroPower(strength=data["strength"], hero_id=["hero_id"], power_id=["power_id"])
    db.session.add(new_hero_power)
    db.session.commit()

    return make_response(new_hero_power.to_dict(), 201)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
