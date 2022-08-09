import time
import os
from utils import *

SCALE_TARGET = os.environ['SCALE_TARGET']
TIME_INTERVAL = os.environ.get('TIME_INTERVAL', 10)

usage_data = [1 for _ in range(10)]

while True:
    print(time.ctime(), end=" : ")
    
    total_cpu_usage = get_metric(SCALE_TARGET)
    print(total_cpu_usage, end=", scaled to ")
    
    pod_num = cpu_to_pod(total_cpu_usage)
    print(pod_num)

    insert_usage(usage_data, pod_num)
    replicas = predict_replica(usage_data)
    print(str(usage_data))
    print("Model predicts replicas : "+str(replicas))

    scale(SCALE_TARGET, replicas)
    
    time.sleep(int(TIME_INTERVAL))
