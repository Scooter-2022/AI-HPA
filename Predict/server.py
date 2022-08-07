from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from model import predict

app = FastAPI()

class Item(BaseModel):
    usage_data: List[int] = []

@app.post("/predict")
async def inference(values: Item):
    values = values.dict()

    usage_data = values['usage_data']
    
    return predict(usage_data)
