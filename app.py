from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema
from marshmallow.fields import Date, Integer, Nested, String
import os


app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Venue, Workspace, User
from schema import VenueSchema, UserSchema

venue_schema = VenueSchema()
venues_schema = VenueSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
workspace_schema = WorkspaceSchema()
workspace_schema = WorkspaceSchema(many=True)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)


@app.route("/venue/")
def venue_list():
    all_venues = Venue.query.all()
    return jsonify(venues_schema.dump(all_venues))


@app.route("/venue/", methods=["POST"])
def add_venue():
    name = request.json.get("name", "")
    city = request.json.get("city", "")
    state = request.json.get("state", "")
    total_seats_available = request.json.get("total_seats_available", 0)

    venue = Venue(
        name=name, city=city, state=state, total_seats_available=total_seats_available
    )

    db.session.add(venue)
    db.session.commit()

    return jsonify(venue_schema.dump(venue))


@app.route("/workspace/")
def workspace_list():
    all_workspaces = Workspace.query.all()
    return jsonify(workspaces_schema.dump(all_workspaces))


@app.route("/workspace/", methods=["POST"])
def add_workspace():
    venue_id = request.json.get("venue_id", "")
    type = request.json.get("type", "")
    pattern = request.json.get("pattern", "")
    total_seats = request.json.get("total_seats", 0)

    workspace = Workspace(
        venue_id=venue_id, type=type, pattern=pattern, total_seats=total_seats
    )

    db.session.add(workspace)
    db.session.commit()

    return jsonify(workspace_schema.dump(workspace))


@app.route("/user/")
def users_list():
    all_users = User.query.all()
    return jsonify(users_schema.dump(all_users))


@app.route("/user/", methods=["POST"])
def add_user():
    mobile = request.json.get("mobile", "")
    email = request.json.get("email", "")
    name = request.json.get("name", "")
    comapny = request.json.get("company", "")
    employee_id = request.json.get("employee_id", "")

    user = User(
        mobile=mobile, email=email, name=name, comapny=comapny, employee_id=employee_id
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))


if __name__ == "__main__":
    app.run()