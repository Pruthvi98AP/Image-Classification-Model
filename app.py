from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware  # Add CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Initialize FastAPI
app = FastAPI()

# Enable CORS (Optional, but useful for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (can restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authentication setup (Fix)
security = HTTPBasic()

VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

# Authentication function
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},  # Force authentication popup
        )
    return credentials.username

# Load trained model
model = tf.keras.models.load_model("C:/Users/Hp/fastapi_project/fashion_mnist_mobilenet_model.keras")

# Class labels
class_labels = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# ✅ Home route (Now requires authentication)
@app.get("/")
def home(username: str = Depends(authenticate)):
    return {"message": "FastAPI is working! Authentication successful!"}

# ✅ Predict route (Now requires authentication)
@app.post("/predict")
def predict_image(file: UploadFile = File(...), username: str = Depends(authenticate)):
    # Read and process the image
    image = Image.open(io.BytesIO(file.file.read())).convert("RGB")
    image = image.resize((32, 32))  # Resize to match model input size
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model.predict(image)
    predicted_label = class_labels[np.argmax(prediction)]

    return {"prediction": predicted_label}
