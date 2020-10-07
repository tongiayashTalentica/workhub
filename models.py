from app import db
from sqlalchemy.dialects.postgresql import JSON


class Venue(db.Model):
    __tablename__ = "venues"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String())
    state = db.Column(db.String())
    name = db.Column(db.String())
    total_seats_available = db.Column(db.Integer)

    def __init__(self, name, city, state, total_seats_available):
        self.name = name
        self.city = city
        self.state = state
        self.total_seats_available = total_seats_available

    def __repr__(self):
        return " Venue : <id {}>".format(self.id)


class User(db.Model):
    __tablename__ = "venues"

    id = db.Column(db.Integer, primary_key=True)
    mobile = db.Column(db.String())
    email = db.Column(db.String())
    name = db.Column(db.String())
    company = db.Column(db.String())
    employee_id = db.Column(db.String())

    def __init__(self, name, company, employee_id='', mobile, email):
        self.name = name
        self.company = company
        self.employee_id = employee_id
        self.mobile = mobile
        self.email = email

    def __repr__(self):
        return " User : <id {}>".format(self.id)


class Workspace(db.Model):
    __tablename__ = "venues"

    workspace_id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer)
    type = db.Column(db.String())
    total_seats = db.Column(db.Integer)
    pattern = db.Column(db.String())

    def __init__(self, venue_id, type, total_seats, pattern):
        self.venue_id = venue_id
        self.type = type
        self.total_seats = total_seats
        self.pattern = pattern

    def __repr__(self):
        return " Workspace : <id {}>".format(self.workspace_id)