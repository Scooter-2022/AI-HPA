import requests
import os

SCALE_TARGET = os.environ['SCALE_TARGET']

APISERVER = "https://kubernetes.default.svc"
SVCACC = "/var/run/secrets/kubernetes.io/serviceaccount"
NS = open(SVCACC + "/namespace").readline()
TOKEN = open(SVCACC + "/token").readline()

def scale(replica=1):
    URL = APISERVER + "/apis/apps/v1/namespaces/" + NS + "/deployments/" + SCALE_TARGET
    PAYLOAD = "{\"spec\":{\"replicas\":" + str(replica) + "}}"
    HEADER = {"Authorization": "Bearer " + TOKEN, "Content-Type": "application/strategic-merge-patch+json"}
    requests.patch(URL, PAYLOAD, headers=HEADER, verify=SVCACC+"/ca.crt")
