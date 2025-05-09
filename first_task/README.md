### App

Курл эндпоинтов
```
curl -X GET http://localhost:5000/
```
```
curl -X GET http://localhost:5000/status
```
```
curl -X POST http://localhost:5000/log \
-H 'Content-Type: application/json' \
-d '{
    "message": "some log"
}'
```
```
curl -X GET http://localhost:5000/logs
```

### Docker

Создание образа
```
docker build -t antonglinisty/my-app ./
```
Загрузка образа в DockerHub
```
docker push antonglinisty/my-app
```
Удаление образа
```
docker rmi antonglinisty/my-app
```

### Configmap

Создание configmap
```
kubectl apply -f ./configmap.yaml
```
Проверка, что configmap создан
```
kubectl get cm
```
Удаление configmap
```
kubectl delete cm my-configmap
```

### Pod

Создание pod
```
kubectl apply -f ./pod.yaml
```
Проверка, что pod создан
```
kubectl get pod
```
Установка туннеля
```
kubectl port-forward my-app 5000:5000
```
Подключение к pod
```
kubectl exec -it my-app -- bash
```
Удаление pod
```
kubectl delete pod my-app
```

### Replicaset

Создание replicaset
```
kubectl apply -f ./replicaset.yaml 
```
Проверка, что replicaset создан
```
kubectl get rs
```
Удаление replicaset
```
kubectl delete rs my-replicaset
```

### Deployment

Создание deployment
```
kubectl apply -f ./deployment.yaml 
```
Проверка, что deployment создан
```
kubectl get deployment
```
Обновление deployment
```
kubectl rollout restart deployment my-deployment
```
Удаление deployment
```
kuberctl delete deployment my-deployment
```
 
 ### Service

Создание service
```
kubectl apply -f ./service.yaml
```
Проверка, что service создан
```
kubectl get svc
```
Создание контейнера для курла эндпоинтов
```
kubectl run test --image=amouat/network-utils -it bash
```
Запись логов
```
curl -X POST http://my-service:5000/log \
-H 'Content-Type: application/json' \
-d '{
    "message": "some log"
}'
```
Чтение логов
```
curl http://my-service:5000/logs
```
Удаление service
```
kubectl delete svc my-service
```

### Daemonset

Создание daemonset
```
kubectl apply -f ./daemonset.yaml
```
Проверка, что daemonset создан
```
kubectl get ds
```
Чтение логов daemonset
```
kubectl logs <daemonset-pod-name>
```
Удаление daemonset
```
kubectl delete ds my-daemonset
```


### Cronjob

Запуск cronjob
```
kubectl apply -f ./cronjob.yaml
```
Проверка, что cronjob создан
```
kubectl get cj
```
Удаление cronjob
```
kubectl delete cj my-cronjob
```