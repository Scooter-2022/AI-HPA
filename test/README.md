# Launch Prometheus & Grafana

### Promethues (:30003)

```bash
kubectl apply -f prometheus-cluster-role.yaml
kubectl apply -f prometheus-config-map.yaml
kubectl apply -f prometheus-deployment.yaml
kubectl apply -f prometheus-node-exporter.yaml
kubectl apply -f prometheus-svc.yaml
```

### kube-state-metrics

```bash
kubectl apply -f kube-state-cluster-role.yaml
kubectl apply -f kube-state-deployment.yaml
kubectl apply -f kube-state-svcaccount.yaml
kubectl apply -f kube-state-svc.yaml
```

### Grafana (:30002)

```bash
kubectl apply -f grafana.yaml
```
