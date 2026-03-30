import pytest
from endpoints import api_requests
from tests.data import client_data

@pytest.mark.parametrize('payload', client_data.create_payloads)
def test_create_various_booking(client, payload):
    create_response = api_requests.create_various_data(payload)
    assert create_response.status_code == 200

@pytest.mark.parametrize('payload', client_data.invalid_payloads)
def test_create_invalid_booking(client, payload):
    create_response = api_requests.create_invalid_data(payload)
    assert create_response.status_code == 500

@pytest.mark.parametrize("checkin, checkout", client_data.generate_pairs())
def test_create_various_booking(client, checkin, checkout):
    payload = client_data.build_payload(checkin, checkout)
    response = api_requests.create_various_data(payload)
    assert response.status_code == 200