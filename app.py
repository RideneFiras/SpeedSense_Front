from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import RootModel
import joblib
import pandas as pd

from services.preprocessing import preprocess_single_row

# ✅ Init
app = FastAPI()

# ✅ Load model
model = joblib.load("Models/best_xgb_model.pkl")

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Mount static folders
app.mount("/css", StaticFiles(directory="frontend/css"), name="css")
app.mount("/js", StaticFiles(directory="frontend/js"), name="js")
app.mount("/images", StaticFiles(directory="frontend/images"), name="images")
app.mount("/webfonts", StaticFiles(directory="frontend/webfonts"), name="webfonts")

# ✅ Serve pages
@app.get("/")
async def serve_index():
    return FileResponse("frontend/index.html")

@app.get("/predict-page")
async def serve_predict_page():
    return FileResponse("frontend/predict.html")

@app.get("/about")
async def serve_predict_page():
    return FileResponse("frontend/aboutus.html")    

# ✅ Prediction input model
class RawQoSInput(RootModel[dict]):
    pass

# ✅ Predict
@app.post("/predict")
async def predict(payload: RawQoSInput):
    data = payload.root
    input_df = preprocess_single_row(data)
    prediction = model.predict(input_df)
    return {"prediction_mbps": float(prediction[0]) / 1e6}
