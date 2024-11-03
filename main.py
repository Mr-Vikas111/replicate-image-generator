from fastapi import FastAPI, HTTPException
from schemas import GenerateImageRequest, FineTuneImageRequest,GenerateImageRequestResponse,GenerateFineTuneRequestResponse
import requests


#import env keys
import keys

# Set up logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# define object
app = FastAPI(
    title="Replicate Image Generation APIs ",
    description="Build a FastAPI application that uses the Replicate Image generation endpoint to fine-tune and generate images.",
    version="v1.0.0",
)


""" # -> COMMON FUNCTION FOR VALIDATE AUTH TOKEN AND URLS """
def send_request(payload: dict,REPLICATE_URL:str) -> dict:
    headers = {
        "Authorization": f"Bearer { keys.REPLICATE_TOKEN }",
        "Content-Type": "application/json",
    }
    response = requests.post(REPLICATE_URL, headers=headers, json=payload)
    if response.status_code != 200:
        logger.error(f"Error response: { response.json() }")
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()



""" # -> API FOR GENERATE IMAGE USING REPLICATE MODAL """
@app.post("/image-generator/",status_code=200,tags=["API's"],response_model = GenerateImageRequestResponse)
async def generate_image(request: GenerateImageRequest) -> dict:
    payload = {
        "version": keys.REPLICATE_IMAGE_GENERATE_MODEL_VERSION,
        "input": request.input.dict()
    }
    response =  send_request(payload,keys.REPLICATE_URL)
    logger.info("Image generated successfully.")
    return response



""" # -> API FOR FINE TUNE IMAGE USING REPLICATE MODAL """
@app.post("/fine-tune/",status_code=200,tags=["API's"],response_model=GenerateFineTuneRequestResponse)
async def image_fine_tune(request: FineTuneImageRequest) -> dict:
    payload = {
        "version":keys.REPLICATE_FINE_TUNE_MODEL_VERSION,
        "input": request.input.dict()
    }
    response = send_request(payload,keys.REPLICATE_URL)
    logger.info("Image fine tune successfully.")
    return response