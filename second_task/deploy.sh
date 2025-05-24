kubectl apply -f ../first_task/manifests/configmap.yaml
kubectl apply -f ../first_task/manifests/deployment.yaml
kubectl apply -f ../first_task/manifests/service.yaml
kubectl apply -f ../first_task/manifests/daemonset.yaml
kubectl apply -f ../first_task/manifests/cronjob.yaml
kubectl apply -f ./manifests/gateway.yaml
kubectl apply -f ./manifests/virtualservice.yaml
kubectl apply -f ./manifests/destinationrule.yaml
