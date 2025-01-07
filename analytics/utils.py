import requests
from django.conf import settings

API_BASE_URL = settings.API_BASE_URL
API_TOKEN = settings.API_TOKEN

def get_orders():
    url = f"{API_BASE_URL}orders/"
    headers = {
        'Authorization': f'Token {API_TOKEN}',
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None