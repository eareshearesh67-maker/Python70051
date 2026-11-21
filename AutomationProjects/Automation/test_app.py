import pytest
from app import app


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