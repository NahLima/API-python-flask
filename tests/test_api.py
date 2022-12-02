from app import app as aplication


def test_home():
    tester = aplication.app.test_client()
    response = tester.get("/", content_type="html/text")
    assert response.status_code == 200


def test_get_departments():
    tester = aplication.app.test_client()
    response = tester.get('api/departments', content_type="application/json")
    assert response.status_code == 200


def test_get_employees():
    tester = aplication.app.test_client()
    response = tester.get('api/employees', content_type="application/json")
    assert response.status_code == 200


def test_get_dependents():
    tester = aplication.app.test_client()
    response = tester.get('api/dependents', content_type="application/json")
    assert response.status_code == 200
