## ignition: http://localhost:8088/
- admin, password

## mysql(3306:3306):
- root, password
## phpmyadmin(http://localhost:8080):
- root, password


# COMMANDS
## FastAPI
- uvicorn app:app --reload

## DOCKER - MYSQL
- docker exec -it ivanignition-db-1 bash
- mysql -u root -p
    - password: password
- create database fridgedb;
- show databases;
