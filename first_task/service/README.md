Создание service
```
kubectl apply -f ./service.yaml
```
Проверка, что service создан
```
kubectl get svc
```
Создание контейнера для проверки
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
curl http://my-service/logs
```
Удаление сервиса
```
kubectl delete svc my-service
```
