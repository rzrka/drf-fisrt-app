import requests

response = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username':
                                                                            'dev', 'password': 'poophy1337'})
print(response.status_code)
print(response.json())
