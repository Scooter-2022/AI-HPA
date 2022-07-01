import requests
import json
import os

APISERVER = "https://kubernetes.default.svc"
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
                total_cpu_usage += int(cur_usage)
    return total_cpu_usage
