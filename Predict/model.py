import time
import random
import math
from tensorflow.keras.models import load_model
import numpy as np

# fastapi 에서 호출하는 함수
def predict(usage_data):
    
    model=load_model('./bi_lstm_model0.h5', compile = False)

    usage_data=np.array(usage_data).reshape(1, 10, 1)
    yhat=model.predict(usage_data)
    replicas=math.ceil(yhat[0][0])
    
    return replicas
