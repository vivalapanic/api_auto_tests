import allure
import requests
from tests.data import auf_data
from tests.data import client_data

def get_token():
    url = f"{auf_data.base_url}/auth"
    response = requests.post(url, json=auf_data.credentials, headers=auf_data.headers)
    with allure.step('Status code'):
        return response

def create_booking():
    url = f"{auf_data.base_url}/booking"
    response = requests.post(url, json=client_data.payload)
    with allure.step('Status code create'):
        return response

def update_booking(session,booking_id):
    url = f"{auf_data.base_url}/booking/{booking_id}"
    response = session.put(url, json=client_data.update_payload)
    with allure.step('Status code update'):
        return response

def get_booking(session,booking_id):
    url = f"{auf_data.base_url}/booking/{booking_id}"
    response = session.get(url)
    with allure.step('Status code get'):
        return response

def delete_booking(session,booking_id):
    url = f"{auf_data.base_url}/booking/{booking_id}"
    response = session.delete(url)
    with allure.step('Status code delete'):
        return response



