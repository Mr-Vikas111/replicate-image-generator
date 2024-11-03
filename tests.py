import pytest
from fastapi.testclient import TestClient

from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_generate_image(client):
    payload = {
        "input": {
            "prompt": "RAW photo, a portrait photo of a latina woman in casual clothes, natural skin, 8k uhd, high quality, film grain, Fujifilm XT3"
        }
    }
    response = client.post("/image-generator/",json=payload)
    
    print("reposne_json",response)
    assert response.status_code == 402
    assert response.status_code == 401
    # assert response.status_code == 200
    assert response.json()

def test_image_fine_tune(client):
    payload = {   
        "input": {
            "prompt": "majestic lion with dragon wings and a mane that glows like a sunset, standing proudly on a cliff overlooking a magical forest.\\n\\n, in the style of m1st1c"
        }
    }
    response = client.post("/fine-tune/",json=payload)
   
    # assert response.status_code == 402
    # assert response.status_code == 200
    assert response.status_code == 401
    assert response.json()