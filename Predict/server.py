from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from model import predict

app = FastAPI()

class Item(BaseModel):
    usage_data: List[int] = []
    curr_pods: int

@app.post("/predict")
async def inference(values: Item):
    values = values.dict()

    usage_data = values['usage_data']
    curr_pods = values['curr_pods']
    
    return predict(usage_data, curr_pods)
