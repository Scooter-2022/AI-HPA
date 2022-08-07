import time
import os
from utils import *

SCALE_TARGET = os.environ['SCALE_TARGET']
TIME_INTERVAL = os.environ.get('TIME_INTERVAL', 10)

usage_data = [0 for _ in range(30)]
while True:
    print(time.ctime(), end=" : ")
    
    total_cpu_usage = get_metric(SCALE_TARGET)
    print(total_cpu_usage, end=", scaled to ")
    
    # curr_pods 는 현재 더미값
    insert_usage(usage_data, total_cpu_usage)
    replicas = predict_replica(usage_data, 1)
    print(replicas)

    scale(SCALE_TARGET, replicas)
    
    time.sleep(int(TIME_INTERVAL))
