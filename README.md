# Welcome to project!

In this document, you can find details about **FILES**, **INSTALL INSTRUCTIONS** and **API documentation**.

[Install and run locally](README.md#install-and-run-locally)

# Project

**FILE: exercise1.py**

This code is composed of two different solutions:
```
1st It consists in finding the elements after the construction of a tree.

2th It consists in finding the elements without building a tree.
```

**REST Application**

This project consists of a sportsbook product which is responsible for managing **sports**, **events** and **selections**.
```
technical888/
    ├── models
            ├── __init__.py
            ├── event.py
            ├── selection.py
            ├── sport.py
            ├── user.py
    ├── resources
            ├── __init__.py
            ├── displays.py
            ├── event.py
            ├── events.py
            ├── selection.py
            ├── selections.py
            ├── sport.py
            ├── sports.py
            ├── user.py
    ├── tests
            ├── test_api.py
    ├── app.py                      # Flask() object
    ├── blacklist.py                # Register logout access token   
    ├── database.db
    ├── requirements.txt
    ├── sql_alchemy.py
```

## Install and run locally

-   Create python3 virtual environment and activate it
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
    
-   Install requirements
    ```
    pip install -r technical888/requirements.txt
    ```
-   Run development server
    ```
    python run.py
    ```
    
# API Documentation

## Sports

- Return all sports

| Method        | URL                         | Filters         |
|---------------|-----------------------------|-----------------|
| `GET`         | /sports                     | name \| active  |

> **200 OK** | curl --location --request GET 'http://127.0.0.1:5000/sports?name=%FOOT%&active=1'

```json
{"sports": 
    [
        {
            "name": "FOOTBALL",
            "slug": "FOOTBALL30",
            "active": 1
        }
     ]
 } 
 ```
 
 - Return just one sport

| Method        | URL                         | Filters         |
|---------------|-----------------------------|-----------------|
| `GET`         | /sports/<name>              | No filters      |

> **200 OK** | curl --location --request GET 'http://127.0.0.1:5000/sports/BASKETBALL'

```json
{
    "name": "BASKETBALL",
    "slug": "BASKETBALL",
    "active": true
}
 ```
> **404 NOT FOUND** | curl --location --request GET 'http://127.0.0.1:5000/sports/BASKETBSSALL'

```json
{
    "message": "Sport name BASKETBSSALL not found."
}
 ```

 - Insert new sport

| Method | URL                         | Filters         |
|--------|-----------------------------|-----------------|
| `POST` | /sports/<name>              | No filters      |

> **200 OK** | curl --location --request POST 'http://127.0.0.1:5000/sports/VOLEYBALL' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "VOLEYBALL",
    "slug": "VOLEYBALL",
    "active": true
}'
```json
{
    "name": "VOLEYBALL",
    "slug": "VOLEYBALL",
    "active": true
}
 ```
> **400 BAD REQUEST** | curl --location --request POST 'http://127.0.0.1:5000/sports/RUGBY' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "RUGBY",
    "slug": "RUGBY",
    "active": true
}'

```json
{
    "message": "Sport name RUGBY already exists."
}
 ```

