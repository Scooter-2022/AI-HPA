## 메트릭 서버 설치
```bash
kubectl apply -f metrics-server.yaml 
```

## RBAC 설정 (기본 namespace : default)
```bash
kubectl apply -f rbac-metrics.yaml
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

SERVICEACCOUNT=/var/run/secrets/kubernetes.io/serviceaccount # 서비스어카운트 토큰 경로
NAMESPACE=$(cat ${SERVICEACCOUNT}/namespace) # 이 파드의 네임스페이스를 읽는다
TOKEN=$(cat ${SERVICEACCOUNT}/token) # 서비스어카운트 베어러 토큰을 읽는다
CACERT=${SERVICEACCOUNT}/ca.crt # 내부 인증 기관(CA)을 참조한다
curl --cacert ${CACERT} --header "Authorization: Bearer ${TOKEN}" -X GET https://${KUBERNETES_SERVICE_HOST}/apis/metrics.k8s.io/v1beta1/namespaces/${NAMESPACE}/pods # KUBERNETES_SERVICE_HOST에 요청을 보낸다
```

