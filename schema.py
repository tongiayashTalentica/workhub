from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema
from marshmallow.fields import Date, Integer, Nested, String


class VenueSchema(Schema):
    id = Integer(allow_none=False)
    city = String(allow_none=False)
    state = String(allow_none=False)
    name = String(allow_none=False)
    total_seats_available = Integer(allow_none=False)


class UserSchema(Schema):
    id = Integer(allow_none=False)
    name = String(allow_none=False)
    company = String(allow_none=False)
    email = String(allow_none=False)
    mobile = String(allow_none=False)
    employee_id = String(allow_none=True)


class WorkspaceSchema(Schema):
    workspace_id = Integer(allow_none=False)
    venue_id = Integer(allow_none=False)
    type = String(allow_none=False)
    total_seats = Integer(allow_none=False)
    pattern = String(allow_none=True)