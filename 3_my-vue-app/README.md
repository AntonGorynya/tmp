# Запуску Local

```commandline
npm run dev
```

# Запуск Docker

```commandline
docker build -t test_app_img . 
docker run  -p 5173:5173 --network="host" 33aa1f862c26
```