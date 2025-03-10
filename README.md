# Image-Classification-Model

 Fashion MNIST Classification API 

  Project Overview
This project classifies Fashion MNIST images using MobileNetV2 and serves predictions via FastAPI.

  Project Structure
- `fashion_mnist.ipynb` - Jupyter Notebook with training code
- `app.py` - FastAPI application for model inference
- `fashion_mnist_mobilenet_model.keras` - Trained model file
- `Dockerfile` - Containerization setup
- `README.md` - Instructions for running the project

  Installation & Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/Pruthvi98AP/fashion-mnist-api.git
   
2. Navigate to the project folder in anaconda prompt:
cd fashion-mnist-api

3. Run the API locally:(FastAPI Server)
   uvicorn app:app --reload

4. open in browser:
   http://127.0.0.1:8000

5. API Testing (Using CURL)
   curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -u admin:password \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@sample_image.jpg'

6. In the end model predict the Image type








