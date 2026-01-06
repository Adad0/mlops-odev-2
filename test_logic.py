import pytest
from feature_eng import hash_customer_id
from app import app

def test_hashing_consistency():
    assert hash_customer_id("USER_123").startswith("G")

def test_api_integration():
    app.config['TESTING'] = True
    with app.test_client() as client:
        response = client.post('/predict', json={'customer_id': 'TEST'})
        assert response.status_code == 200