from config import db, ma


class Dependents(db.Model):
    __tablename__ = "Dependents"
    id = db.Column(db.Integer, primary_key=True)
    responsible_id = db.Column(db.Integer, db.ForeignKey("Employees.id"))
    name = db.Column(db.String(100))


class DependentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dependents
        load_instance = True
        sqla_session = db.session
        include_fk = True
        include_relationships = True


dependent_schema = DependentsSchema(many=True)

