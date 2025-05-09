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
Проверка, что сущность создана
```
kubectl get <entity-name>
```
Удаление сущности
```
kubectl delete <entity-name> my-<entity-name>
```
---
Установка туннеля
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
