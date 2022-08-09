import requests
import json
import os
import math

APISERVER = "https://" + os.environ['KUBERNETES_SERVICE_HOST'] + ":" + os.environ['KUBERNETES_SERVICE_PORT_HTTPS']
SVCACC = "/var/run/secrets/kubernetes.io/serviceaccount"
NS = open(SVCACC + "/namespace").readline()
TOKEN = open(SVCACC + "/token").readline()

def scale(scale_target, replica):
    URL = APISERVER + "/apis/apps/v1/namespaces/" + NS + "/deployments/" + scale_target
    PAYLOAD = "{\"spec\":{\"replicas\":" + str(replica) + "}}"
    HEADER = {"Authorization": "Bearer " + TOKEN, "Content-Type": "application/strategic-merge-patch+json"}
    requests.patch(URL, PAYLOAD, headers=HEADER, verify=SVCACC+"/ca.crt")
    return

def get_metric(scale_target):
    URL = APISERVER + "/apis/metrics.k8s.io/v1beta1/namespaces/" + NS + "/pods" 
    HEADER = {"Authorization": "Bearer " + TOKEN}
    pods = json.loads(requests.get(URL, headers=HEADER, verify=SVCACC+"/ca.crt").text)

    total_cpu_usage = 0
    if 'items' in pods.keys():
        for pod in pods['items']:
            if scale_target in pod['metadata']['name']:
                cur_usage = pod['containers'][0]['usage']['cpu']
                if cur_usage[-1] == 'n':
                    cur_usage = cur_usage[:-1]
                elif cur_usage[-1] == 'u':
                    cur_usage = cur_usage[:-1] + "000"
                elif cur_usage[-1] == 'm':
                    cur_usage = cur_usage[:-1] + "000000"
                total_cpu_usage += int(cur_usage)
    return total_cpu_usage

def cpu_to_pod(total_cpu_usage):
    user_cpu_limit=os.environ.get('CONTAINER_CPU_LIMIT_MILLICORES', 250000000)
    cpu_limit_rate=int(user_cpu_limit)*0.8                                   
    pod_num = math.ceil(total_cpu_usage/cpu_limit_rate)                                                              
    return pod_num                             

def insert_usage(usage_data, usage):
    for i in range(len(usage_data) - 1):
        usage_data[i] = usage_data[i+1]
    usage_data[9] = usage
    return

def predict_replica(usage_data):
    URL = "http://localhost:4000/predict"
    data = {'usage_data':usage_data}
    response = requests.post(URL, json=data)
    replicas = int(response.text)
    return replicas
