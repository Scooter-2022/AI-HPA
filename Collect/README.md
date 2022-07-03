## 메트릭 서버 설치
```bash
kubectl apply -f metrics-server.yaml 
```

## RBAC 설정 (기본 namespace : default)
```bash
kubectl apply -f rbac.yaml
```

## 파드에 접속하기 (bash shell)
```bash
kubectl exec -it [파드이름] -- /bin/bash
```

## 파드 내부 
```bash
# ex) ubuntu 18.04 환경
apt-get update
apt install curl -y

APISERVER=https://kubernetes.default.svc # 내부 API 서버 호스트 이름을 가리킨다
SERVICEACCOUNT=/var/run/secrets/kubernetes.io/serviceaccount # 서비스어카운트 토큰 경로
NAMESPACE=$(cat ${SERVICEACCOUNT}/namespace) # 이 파드의 네임스페이스를 읽는다
TOKEN=$(cat ${SERVICEACCOUNT}/token) # 서비스어카운트 베어러 토큰을 읽는다
CACERT=${SERVICEACCOUNT}/ca.crt # 내부 인증 기관(CA)을 참조한다
curl --cacert ${CACERT} --header "Authorization: Bearer ${TOKEN}" -X GET https://${APISERVER}/metrics/api # TOKEN으로 API를 탐색한다
curl --cacert ${CACERT} --header "Authorization: Bearer ${TOKEN}" -X GET https://${KUBERNETES_SERVICE_HOST}/metrics/api # 만약 APISERVER를 인식하지 못한다면 KUBERNETES_SERVICE_HOST에 요청을 보낸다
```

