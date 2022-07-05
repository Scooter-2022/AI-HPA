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
    print(values)
    print(values.dict())

    values = values.dict()
    print(type(values))
    print(values)

    return values, predict([], 1)
