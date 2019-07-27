from urllib.parse import urljoin

import requests

from dev.about_mocking.constants import BASE_URL

USERS_URL = urljoin(BASE_URL, 'users')


def get_users():
    response = requests.get(USERS_URL)
    
    if response.ok:
        return response
    else:
        return None