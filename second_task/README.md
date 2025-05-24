### Установка Istio в кластер kubernetes на macos

### Установка Istio CLI
```
brew install istioctl
```

### Установка Istio в кластер
```
istioctl install --set profile=default -y
```

### Включение автоматической инъекции sidecar
```
kubectl label namespace default istio-injection=enabled
```

### Проверить состояние компонентов Istio
```
kubectl get pods -n istio-system
```
