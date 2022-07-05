import time
import random

# fastapi 에서 호출하는 함수
def predict(usage_data, curr_pods):
    
    # 임의로 설정한 inference 시간
    time.sleep(3)
    replicas = random.randrange(1, 6)

    return replicas
