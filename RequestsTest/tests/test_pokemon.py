import pytest, requests

HOST = 'https://pokemonbattle.me:9104'

TOKEN = '5cd242c94a63f9c17384ba51c3dfa3fe'

def test_status_code():
    response = requests.get(f'{HOST}/trainers', params = {'trainer_id': 4238})
    assert response.json()['trainer_name'] == 'Марс'
    assert response.status_code == 200