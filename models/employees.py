from config import db, ma
from marshmallow_sqlalchemy import fields

from models.dependents import Dependents, DependentsSchema


class Employees(db.Model):
    __tablename__ = "Employees"
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey("Departments.id"))
    name = db.Column(db.String(100))

    dependents = db.relationship(
        Dependents,
        backref="dependents",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="asc(Dependents.id)"
    )


class EmployeesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employees
        load_instance = True
        sqla_session = db.session
        include_fk = True
        include_relationships = True

    dependents = fields.Nested(DependentsSchema, many=True)


employee_schema = EmployeesSchema(many=True)
