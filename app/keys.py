from dotenv import load_dotenv
import os

load_dotenv()

REPLICATE_TOKEN=os.environ.get('REPLICATE_ACCESS_KEY') 
REPLICATE_URL = os.environ.get('REPLICATE_API_URL')

REPLICATE_IMAGE_GENERATE_MODEL_VERSION=os.environ.get('REPLICATE_IMAGE_GENERATE_MODEL_VERSION') # -> model name : lucataco/realistic-vision-v5
REPLICATE_FINE_TUNE_MODEL_VERSION=os.environ.get('REPLICATE_FINE_TUNE_MODEL_VERSION') # -> model name : halimalrasihi/flux-mystic-animals
