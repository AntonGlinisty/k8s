Создание configmap
```
kubectl apply -f ./configmap.yaml
```
Проверка, что configmap создан
```
kubectl get cm
```
Создание podа
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
Подключение к podу
```
kubectl exec -it my-app -- bash
```
Удаление configmap
```
kubectl delete cm my-configmap
```
Удаление podа
```
kubectl delete pod my-app
```