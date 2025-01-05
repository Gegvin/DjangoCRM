import requests
from django.conf import settings

API_BASE_URL = 'http://127.0.0.1:8000/'  # URL вашего DjangoCRM API
API_TOKEN = 'b8a3f1412fddb243e9ea1bc1ed82805d33b3b07e'  # Замените на ваш токен доступа

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