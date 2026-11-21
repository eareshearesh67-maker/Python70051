import pytest
from app import app
import threading


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_get_equipment(client):
    response = client.get('/api/equipment')

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) == 2

    assert data[0]['id'] == 101
    assert data[0]['name'] == "Flight control unit"
    assert data[0]['type'] == "FCU"
    assert data[0]['status'] == "Operational"

@pytest.mark.parametrize("equipment_id", [101])

def test_get_equipment_by_id(client,equipment_id):
    response = client.get('/api/equipment/{}'.format(equipment_id))

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, dict)

    assert data['id'] == 101
    assert data['name'] == "Flight control unit"
    assert data['type'] == "FCU"
    assert data['status'] == "Operational"

def task1():
    print("Running Task 1")
    test_get_equipment(client)

def task2():
    print("Running Task 2")
    test_get_equipment_by_id(client, 101)  

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()      