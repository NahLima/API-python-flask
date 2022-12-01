from models import Employees, EmployeesSchema, Departments, Dependents, dependent_schema, department_schema


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


def count_dependents(responsible_id):
    dependents = Dependents.query.filter(Dependents.responsible_id == responsible_id).count()
    result = [{"total_dependents": dependents}]
    return result


def get_employees_by_department_result(name):
    get_department = Departments.query.filter(Departments.name == name).all()
    dep_id = get_department[0].id
    dep_name = get_department[0].name

    get_employees = Employees.query.filter(Employees.department_id == dep_id).all()

    emp_list = []

    for emp in get_employees:
        get_total_dependent = count_dependents(emp.id)

        if get_total_dependent[0]['total_dependents'] > 0:
            have_dependents = True
        else:
            have_dependents = False

        employees_result = {"id": emp.id, "name": emp.name, "have_dependents": have_dependents}
        emp_list.append(employees_result)

    result_info = [{"Department": dep_name, "Employees": emp_list}]

    return result_info
