# FastAPI -> Replicate Image Generation 

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.4-orange)


## Description

This project is a built with FastAPI. It provides APIs for  Replicate Image generation endpoint to fine-tune and generate images.

## Project Structure

image-generator/
├── app/                  # Main application directory
│   ├── __init__.py       # Marks the directory as a Python package
│   ├── keys.py           # Contains all secret keys and configuration
│   ├── main.py           # Main application file containing API routes
│   └── schemas.py        # Individual Pydantic model definitions
│       
├── test.py               # Test cases for the application
├── Dockerfile            # Configuration for building the Docker image
├── pytest.ini            # Configuration test case requiments
├── api.http              # Configure for api test in local machine usine VScode extensions (name -> REST Client)
├── requirements.txt      # List of project dependencies
└── README.md             # Project documentation

