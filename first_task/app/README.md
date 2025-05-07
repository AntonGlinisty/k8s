Создание образа
```
docker build -t antonglinisty/my-app ./
```
Загрузка образа в DockerHub
```
docker push antonglinisty/my-app
```
Запуск приложения в background
```
docker run --name my-app -d -p 5000:5000 antonglinisty/my-app
```
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
Остановка и удаление контейнера
```
docker stop my-app && docker rm my-app
```
