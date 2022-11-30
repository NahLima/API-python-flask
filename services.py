from flask import abort
from models import Employees,EmployeesSchema, employees_schema, employee_schema, Departments, Dependents, dependents_schema, \
    dependent_schema, departments_schema, department_schema


def read_all_employees():
    people = Employees.query.all()
    person_schema = EmployeesSchema(many=True)
    return person_schema.dump(people)


def read_all_departments():
    department = Departments.query.all()
    return department_schema.dump(department)


def read_all_dependents():
    dependent = Dependents.query.all()
    return dependent_schema.dump(dependent)


def get_employees_by_name(full_name):
    employee = Employees.query.filter(Employees.full_name == full_name).one_or_none()

    if employee is not None:
        return employees_schema.dump(employee)
    else:
        abort(404, f"Person with last name {full_name} not found")

# def get_employees_by_department(department):
#    employee = Employees.query.filter(Employees.full_name == department).one_or_none()
#   if employee is not None:
#      return employees_schema.dump(employee)
# else:
#    abort(404, f"Person with last name {department} not found")
