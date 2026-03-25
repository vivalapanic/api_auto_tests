import allure
from endpoints import api_requests
from tests.data import client_data

def test_auth(client):
    assert client.token is not None

@allure.feature('Auth')
@allure.story('Token')
def test_auth_response(client):
    response = client.auth()
    assert response.status_code == 200
    with allure.step('Token is in'):
        assert "token" in response.json()

@allure.feature('Create booking')
@allure.story('e2e booking')
def test_crud_booking(client):
    create_response = api_requests.create_booking()
    assert create_response.status_code == 200

    create_data = create_response.json()
    booking_id = create_data["bookingid"]
    with allure.step('Create booking'):
        assert create_data["booking"]["firstname"] == client_data.payload["firstname"]

    update_response = api_requests.update_booking(client.session, booking_id)
    assert update_response.status_code == 200

    update_data = update_response.json()
    with allure.step('Update firstname'):
        assert update_data["firstname"] == client_data.update_payload["firstname"]
    with allure.step('Update lastname'):
        assert update_data["lastname"] == client_data.update_payload["lastname"]

    get_response = api_requests.get_booking(client.session, booking_id)
    assert get_response.status_code == 200

    get_data = get_response.json()
    with allure.step('Get booking'):
        assert get_data == client_data.update_payload

    delete_response = api_requests.delete_booking(client.session, booking_id)
    assert delete_response.status_code == 201

    get_after_delete = api_requests.get_booking(client.session, booking_id)
    with allure.step('Status code'):
        assert get_after_delete.status_code == 404




