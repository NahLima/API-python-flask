from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


EMPLOYEES = {
    "Naiara": {
        "full_name": "Naiara Santos de Lima",
        "department": "Engenharia",
        "timestamp": get_timestamp(),
    },
    "Rafael": {
        "full_name": "Rafael de Freitas Sampaio",
        "department": "Comunicação",
        "timestamp": get_timestamp(),
    }
}


def read_all():
    return list(EMPLOYEES.values())
