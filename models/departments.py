from config import db, ma


class Departments(db.Model):
    __tablename__ = "Departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class DepartmentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Departments
        load_instance = True
        sqla_session = db.session


departments_schema = DepartmentsSchema(many=True)
