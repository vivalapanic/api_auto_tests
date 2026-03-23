import requests
from tests.data import auf_data
from tests.data import client_data

def get_token():
    url = f"{auf_data.base_url}/auth"
    response = requests.post(url, json=auf_data.credentials, headers=auf_data.headers)
    return response

def create_booking():
    url = f"{auf_data.base_url}/booking"
    response = requests.post(url, json=client_data.payload)
    return response

def update_booking(session,booking_id):
    url = f"{auf_data.base_url}/booking/{booking_id}"
    response = session.put(url, json=client_data.update_payload)
    return response

def get_booking(session,booking_id):
    url = f"{auf_data.base_url}/booking/{booking_id}"
    response = session.get(url)
    return response

def delete_booking(session,booking_id):
    url = f"{auf_data.base_url}/booking/{booking_id}"
    response = session.delete(url)
    return response



