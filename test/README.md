# Launch Prometheus & Grafana

### Promethues

```bash
kubectl apply -f prometheus-cluster-role.yaml
kubectl apply -f prometheus-config-map.yaml
kubectl apply -f prometheus-deployment.yaml
kubectl apply -f prometheus-node-exporter.yaml
kubectl apply -f prometheus-svc.yaml
```

### Grafana

```bash
kubectl apply -f grafana.yaml
```

port : 30002
