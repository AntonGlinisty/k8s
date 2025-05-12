### Условие задачи находится в файле task.md

## Полезные команды


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

### K8s entities
Создание сущности
```
kubectl apply -f ./manifests/<entity-name>.yaml
```
Посмотреть на сущность
```
kubectl get <entity-name>
```
Посмотреть на служебные сущности
```
kubectl get <entity-name> -A
```
Посмотреть на все сущности
```
kubectl get all
```
Удаление сущности
```
kubectl delete <entity-name> my-<entity-name>
```

### K8s common
Автодополнение
```
source <(kubectl completion zsh)
```
Установка туннеля до пода
```
kubectl port-forward <pod-name> 5000:5000
```
Подключение к поду
```
kubectl exec -it <pod-name> -- bash
```
Чтение логов пода
```
kubectl logs <pod-name>
```
Обновление deployment
```
kubectl rollout restart deployment my-deployment
```
Создание пода внутри кластера для общения с service
```
kubectl run test --image=amouat/network-utils -it bash
```

### Minikube
Подключение аддона дашборда
```
minikube addons enable dashboard
```
Открытие туннеля по пода дашборда
```
minikube dashboard
```
Открытие туннеля к сервису
```
minikube service <service-name>
```
Ssh на ноду кластера
```
minikube ssh
```
