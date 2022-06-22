import requests
import time
import json

APISERVER = "https://kubernetes.default.svc"
SVCACC = "/var/run/secrets/kubernetes.io/serviceaccount"
NS = open(SVCACC + "/namespace").readline()
TOKEN = open(SVCACC + "/token").readline()
headers = {"Authorization": "Bearer " + TOKEN}

while True:
    print('---------------------------------------------------------------------------------------------------------------')
    print(time.ctime()) 
    pods = json.loads(requests.get(APISERVER + f"/apis/metrics.k8s.io/v1beta1/namespaces/{NS}/pods", verify=SVCACC+"/ca.crt", headers=headers).text)
    if 'items' in pods.keys():
        for pod in pods['items']:
            print(f"{pod['timestamp']}\tname: {pod['metadata']['name']}\tcontainers: {len(pod['containers'])}\tusage: {pod['containers'][0]['usage']}")
    print('---------------------------------------------------------------------------------------------------------------')
    time.sleep(10)
