Создание deployment
```
kubectl apply -f ./deployment.yaml 
```
Проверка, что replicaset создан
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
 