# otus_project

Посмотреть отчет allure локально  
/home/alisapokormlyak/Desktop/allure/allure-2.22.0/bin/allure serve allure-results/

Запустить селеноид: 
```commandline
./cm selenoid (start, stop, status)
./cm selenoid-ui start
```

Селеноид доступен по адресу:
http://localhost:4444/wd/hub
http://localhost:8080

### Запуск проекта с помощью docker

Собрать образ проекта:
```commandline
docker build -t tests .
```

Запустить тесты удаленно: 
```commandline
docker run -it tests
```

Запустить тесты локально: 
```commandline
docker run -it tests --executor local
```

### Запуск Jenkins
sudo systemctl start jenkins
jenkins доступен по адресу:
http://localhost:8080/