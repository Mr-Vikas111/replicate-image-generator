# FastAPI -> Replicate Image Generation 

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.4-orange)
![Tests](https://github.com//Mr-Vikas111/replicate-image-generator/actions/workflows/fastapici.yml/badge.svg)


## Description

This project is a built with FastAPI. It provides APIs for  Replicate Image generation endpoint to fine-tune and generate images.

## Features

- **API Endpoints**:
  ```bash
  http://127.0.0.1:8000/image-generator/

  use image model ->  lucataco/realistic-vision-v5
  ```
  ```bash
  http://127.0.0.1:8000/fine-tune/
  
  use image fine-tune model ->  halimalrasihi/flux-mystic-animals
  ```
- **Pydantic Schemas**: Ensure data validation and serialization.
- **Secret Management**: Centralized management of API keys and secrets.
- **Test Cases**: the test cases for verifying the functionality of the application. The tests are designed to ensure that each component behaves as expected and to maintain overall code quality.

## Requirements

- Python 3.9 or higher
- FastAPI
- [Pytest, Docker, FastAPI, Pydantic, Uvicorn, ]

## API Documentation
- Swagger UI

## Installation

  1. Clone the repository:
     ```bash
     git clone https://github.com/Mr-Vikas111/replicate-image-generator.git
     cd your-repo-name
  2. Create a virtual environment:
     ```bash
     python -m venv venv
  3. Activate the virtual environment:
     - On macOS/Linux:
     ```bash
     venv\Scripts\activate
     ```
     - On macOS/Linux:
      ```bash
     source venv/bin/activate
     ```
  4. Install the required packages:
     ```bash
     pip install -r requirements.txt
     
## Usage 

  To run the application, use the following command:
  
  ```bash
  uvicorn app.main:app --reload
 ```

## Running Tests

  To run the tests for this project, use the following command:
   
   ```bash
     pytest
 ```
