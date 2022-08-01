# Welcome to project!

In this document, you can find details about **FILES**, **INSTALL INSTRUCTIONS** and **API documentation**.

- [Install and run locally](README.md#install-and-run-locally) <br>
- [Build and run docker](README.md#build-and-run-docker)
- [API Documentation](README.md#api-documentation)
- - [Action](README.md#action)
- - [Users](README.md#users)
- - [Sports](README.md#sports)
- - [Events](README.md#events)
- - [Selections](README.md#selections)
- - [Displays](README.md#displays) - General requests

# Project

**FILE:** [Internal Node Exercise](exercise1.py)

This code is composed of two different solutions:
```
1st It consists in finding the elements after the construction of a tree.

2th It consists in finding the elements without building a tree.
```

**REST Application**

This project consists of a sportsbook product which is responsible for managing **sports**, **events** and **selections** with layer for **users** security.
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
    cd technical888
    python3 -m venv venv
    source venv/bin/activate
    ```
    
-   Install requirements
    ```
    pip install -r requirements.txt
    ```
-   Run development server
    ```
    python app.py
    ```
    
## Build and run docker

-   Build image
    ```
    docker build -t webapi -f Dockerfile .
    ```
    
-   Run
    ```
    docker run -p 5000:5000 webapi
    ```
    

    
# API Documentation
# Users

### [GET] Return specific user

| Method        | URL               | Filters    | Authorization |
|---------------|-------------------|------------|---------------|
| `GET`         | /user/< id_user > | No filters | NO            |

> **200 OK** | curl --request GET 'http://127.0.0.1:5000/user/1'

```json
{
    "user_id": 1,
    "login": "jonas"
}
 ```

### [POST] Insert new user

| Method | URL        | Filters         | Authorization |
|--------|------------|-----------------|---------------|
| `POST` | /register  | No filters      | No            |

> **201 CREATED** | curl --request POST 'http://127.0.0.1:5000/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "login": "jonas",
    "password": "1234"
}''
```json
{
    "message": "Login jonas888 created :) ."
}
 ```

### [POST] Login user (generate access-token)

| Method | URL    | Filters         | Authorization |
|--------|--------|-----------------|---------------|
| `POST` | /login | No filters      | No            |

> **200 OK** | curl --request POST 'http://127.0.0.1:5000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "login": "jonas",
    "password": "1234"
}''
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1OTIwMjg4MywianRpIjoiOTkyMmY1YTktN2NkNi00M2YyLTk5ZjctYTY5ZGQ1M2RhM2Q1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjU5MjAyODgzLCJleHAiOjE2NTkyMDM3ODN9.u2KOj4gHXGPPg1TElU0QaF85fZjUz5KnkAZJGUQUFuo"
}
 ```

### [POST] Logout user (insert access-token in blacklist)

| Method | URL     | Filters         | Authorization |
|--------|---------|-----------------|---------------|
| `POST` | /logout | No filters      | Required      |

> **200 OK** | curl --request POST 'http://127.0.0.1:5000/logout' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "login": "jonas",
    "password": "1234"
}''
```json
{
    "message": "Logged out successfully ."
}
 ```

# Action

### [POST] Started event

| Method | URL                         | Filters    | Authorization |
|--------|-----------------------------|------------|---------------|
| `POST` | /startevent/{event}/{sport} | No filters | Required      |

> **201 CREATED** | curl --request POST 'http://127.0.0.1:5000/startevent/Internazionale x Liverpol/FOOTBALL' \
--header 'Authorization: Bearer <access_token>'
```json
{
    "message": "Event Internazionale x Liverpol started"
}
 ```

### [POST] Started events less than datetime now

| Method | URL            | Filters    | Authorization |
|--------|----------------|------------|---------------|
| `POST` | /startevents   | No filters | Required      |

> **201 CREATED** | curl --request POST 'http://127.0.0.1:5000/startevents' \
--header 'Authorization: Bearer <access_token>'
```json
{
    "message": "Event Internazionale x Liverpol started"
}
 ```

# Sports

### [GET] Return sports with filters

| Method        | URL                         | Filters         | Authorization |
|---------------|-----------------------------|-----------------|---------------|
| `GET`         | /sports                     | name \ active   | NO            |

> **200 OK** | curl --request GET 'http://127.0.0.1:5000/sports?name=%FOOT%&active=1'

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
 
### [GET] Return specific sport

| Method        | URL            | Filters         | Authorization |
|---------------|----------------|-----------------|---------------|
| `GET`         | /sports/{name} | No filters      | NO            |

> **200 OK** | curl --request GET 'http://127.0.0.1:5000/sports/BASKETBALL'

```json
{
    "name": "BASKETBALL",
    "slug": "BASKETBALL",
    "active": true
}
 ```
> **404 NOT FOUND** | curl --request GET 'http://127.0.0.1:5000/sports/BASKETBSSALL'

```json
{
    "message": "Sport name BASKETBSSALL not found."
}
 ```

### [POST] Insert new sports

| Method | URL             | Filters         | Authorization |
|--------|-----------------|-----------------|---------------|
| `POST` | /sports/{name}  | No filters      | Required      |

> **200 OK** | curl --request POST 'http://127.0.0.1:5000/sports/VOLEYBALL' \
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
> **400 BAD REQUEST** | curl --request POST 'http://127.0.0.1:5000/sports/RUGBY' \
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

### [PUT] Update or add new sport

| Method | URL             | Filters         | Authorization |
|--------|-----------------|-----------------|---------------|
| `PUT`  | /sports/{name}  | No filters      | Required      |

> **200 OK** | curl --request PUT 'http://127.0.0.1:5000/sports/VOLEYBALL' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "VOLEYBALL",
    "slug": "VOLEYBALL888",
    "active": 1
}'

```json
{
    "name": "VOLEYBALL",
    "slug": "VOLEYBALL888",
    "active": 1
}
 ```
> **201 CREATED** | curl --request PUT 'http://127.0.0.1:5000/sports/VOLEYBALL888' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "VOLEYBALL888",
    "slug": "VOLEYBALL888",
    "active": 1
}'

```json
{
    "name": "VOLEYBALL888",
    "slug": "VOLEYBALL888",
    "active": true
}
 ```

### [DELETE] Delete (inactive) sport

| Method   | URL             | Filters         | Authorization |
|----------|-----------------|-----------------|---------------|
| `DELETE` | /sports/{name}  | No filters      | Required      |

> **200 OK** | curl --request DELETE 'http://127.0.0.1:5000/sports/VOLEYBALL888' \
--header 'Authorization: Bearer <access_token>'

```json
{
    "message": "Sport inactivate"
}
 ```

## Events

### [GET] Return events with filters

| Method | URL     | Possible filters                                                           | Authorization  |
|--------|---------|----------------------------------------------------------------------------|----------------|
| `GET`  | /events | name \ active \ scheduled_start_min \ scheduled_start_max \ sport \ status | No             |


> **200 OK** | curl --request GET 'http://127.0.0.1:5000/events?name=%x%&active=0&scheduled_start_min=2022-07-30&scheduled_start_max=2022-09-30&sport=TENNIS'

```json
{
    "events": [
        {
            "name": "Mick x Fiona",
            "slug": "WORLD TENNIS",
            "active": 0,
            "type": "preplay",
            "sport": "TENNIS",
            "status": "Pending",
            "scheduled_start": "2022-08-30 20:00:00.000000",
            "actual_start": null
        },
        {
            "name": "Oliveira x Michael",
            "slug": "WORLD TENNIS",
            "active": 0,
            "type": "preplay",
            "sport": "TENNIS",
            "status": "Started",
            "scheduled_start": "2022-08-30 20:00:00.000000",
            "actual_start": "2022-07-30 16:02:21.503674"
        }
    ]
}
 ```

### [GET] Return specific event


| Method        | URL                    | Filters         | Authorization |
|---------------|------------------------|-----------------|---------------|
| `GET`         | /events/{name}/{sport} | No filters      | No            |

> **200 OK** | curl --request GET 'http://127.0.0.1:5000/events/Nadal x Rafael/TENNIS'

```json
{
    "name": "Nadal x Rafael",
    "slug": "Nadal x Rafael 316",
    "active": true,
    "type": "preplay",
    "sport": "TENNIS",
    "status": "Pending",
    "scheduled_start": "2022-08-30 20:00:00",
    "actual_start": null
}
 ```
> **404 NOT FOUND** | curl --request GET 'http://127.0.0.1:5000/events/Nadal ax Rafael/TENNIS'

```json
{
    "message": "Event name Nadal ax Rafael not found."
}
 ```
### [POST] Insert new event

| Method | URL                    | Filters         | Authorization |
|--------|------------------------|-----------------|---------------|
| `POST` | /events/{name}/{sport} | No filters      | Required      |

> **200 CREATED** | curl --request POST 'http://127.0.0.1:5000/events/Alan x Michael/TENNIS' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Mick x Fiona",
    "slug": "WORLD TENNIS",
    "active": 1,
    "type": "preplay",
    "sport": "TENNIS",
    "status": "Pending",
    "scheduled_start": "2022-08-30 20:00:00"
}'
```json
{
    "name": "Mick x Fiona",
    "slug": "WORLD TENNIS",
    "active": 1,
    "type": "preplay",
    "sport": "TENNIS",
    "status": "Pending",
    "scheduled_start": "2022-08-30 20:00:00"
}
 ```
> **400 BAD REQUEST** | curl --request POST 'http://127.0.0.1:5000/events/Alan x Michael/TENNIS' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Mick x Fiona",
    "slug": "WORLD TENNIS",
    "active": 1,
    "type": "preplay",
    "sport": "TENNIS",
    "status": "Pending",
    "scheduled_start": "2022-08-30 20:00:00"
}'

```json
{
    "message": "Event name Alan x Michael already exists."
}
 ```

### [PUT] Update or add new events

| Method | URL                    | Filters         | Authorization |
|--------|------------------------|-----------------|---------------|
| `PUT`  | /events/{name}/{sport} | No filters      | Authorization |

> **200 OK** | curl --request PUT 'http://127.0.0.1:5000/events/Alan x Michael/TENNIS' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Alan x Michael",
    "slug": "WORLD TENNIS",
    "active": 1,
    "type": "preplay",
    "sport": "TENNIS",
    "status": "Started",
    "scheduled_start": "2022-08-30 20:00:00"
}'

```json
{
    "name": "Alan x Michael",
    "slug": "WORLD TENNIS",
    "active": true,
    "type": "preplay",
    "sport": "TENNIS",
    "status": "Started",
    "scheduled_start": "2022-08-30 20:00:00",
    "actual_start": "2022-07-30 16:01:04"
}
 ```
> **201 CREATED** | curl --request PUT 'http://127.0.0.1:5000/events/Oliveira x Michael/TENNIS' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Oliveira x Michael",
    "slug": "WORLD TENNIS",
    "active": 1,
    "type": "preplay",
    "sport": "TENNIS",
    "status": "Started",
    "scheduled_start": "2022-08-30 20:00:00",
    "actual_start": null
}'

```json
{
    "name": "Oliveira x Michael",
    "slug": "WORLD TENNIS",
    "active": true,
    "type": "preplay",
    "sport": "TENNIS",
    "status": "Started",
    "scheduled_start": "2022-08-30 20:00:00",
    "actual_start": "2022-07-30 16:02:21"
}
 ```

### [DELETE] Delete (inactive) Event

| Method   | URL                    | Filters         | Authorization |
|----------|------------------------|-----------------|---------------|
| `DELETE` | /events/{name}/{sport} | No filters      | Required      |

> **200 OK** | curl --request DELETE 'http://127.0.0.1:5000/events/Oliveira x Michael/TENNIS' \
--header 'Authorization: Bearer <access_token>'

```json
{
    "message": "Event inactivate"
}
 ```

## Selections

### [GET] Return selections with filters

| Method | URL         | Filters                  | Authorization |
|--------|-------------|--------------------------|---------------|
| `GET`  | /selections | event \ outcome \ active | No            |

> **200 OK** | curl --request GET 'http://127.0.0.1:5000/selections?event=%Internazionale%&active=True'

```json
{
    "selections": [
        {
            "name": "1",
            "event": "Internazionale x Liverpol",
            "price": 1.2,
            "active": 1,
            "outcome": "Unsettled"
        },
        {
            "name": "2",
            "event": "Internazionale x Liverpol",
            "price": 4.9,
            "active": 1,
            "outcome": "Unsettled"
        },
        {
            "name": "X",
            "event": "Internazionale x Liverpol",
            "price": 8.0,
            "active": 1,
            "outcome": "Unsettled"
        }
    ]
}
 ```

### [GET] Return specific selection

| Method        | URL                        | Filters         | Authorization |
|---------------|----------------------------|-----------------|---------------|
| `GET`         | /selections/{name}/{event} | No filters      | No            |

> **200 OK** | curl --request GET 'http://127.0.0.1:5000/selections/X/Internazionale x Liverpol'

```json
{
    "name": "X",
    "event": "Internazionale x Liverpol",
    "price": 8.0,
    "active": true,
    "outcome": "Unsettled"
}
 ```
> **404 NOT FOUND** | curl --request GET 'http://127.0.0.1:5000/selections/SX/Internazionale x Liverpol'

```json
{
    "message": "Selection name SX not found."
}
 ```

### [POST] Insert new selection

| Method | URL                        | Filters         | Authorization |
|--------|----------------------------|-----------------|---------------|
| `POST` | /selections/{name}/{event} | No filters      | Required      |

> **200 OK** | curl --request POST 'http://127.0.0.1:5000/selections/X/Michael x Stace' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "X",
    "event": "Michael x Stace",
    "price": 3.7,
    "active": 1,
    "outcome": "Unsettled"
}'
```json
{
    "name": "X",
    "event": "Michael x Stace",
    "price": 3.7,
    "active": true,
    "outcome": "Unsettled"
}
 ```
> **400 BAD REQUEST** | curl --request POST 'http://127.0.0.1:5000/selections/X/Michael x Stace' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "X",
    "event": "Michael x Stace",
    "price": 3.7,
    "active": 1,
    "outcome": "Unsettled"
}'

```json
{
    "message": "Selection name X already exists."
}
 ```

### [PUT] Update or add new selection

| Method | URL                        | Filters         | Authorization |
|--------|----------------------------|-----------------|---------------|
| `PUT`  | /selections/{name}/{event} | No filters      | Authorization |

> **200 OK** | curl --request PUT 'http://127.0.0.1:5000/selections/X/Michael x Stace' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "X",
    "event": "Michael x Stace",
    "price": 7.9,
    "active": 1,
    "outcome": "Unsettled"
}'

```json
{
    "name": "X",
    "event": "Michael x Stace",
    "price": 7.9,
    "active": true,
    "outcome": "Unsettled"
}
 ```
> **201 CREATED** | curl --request PUT 'http://127.0.0.1:5000/selections/2/Michael x Stace' \
--header 'Authorization: Bearer <access_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "2",
    "event": "Michael x Stace",
    "price": 7.9,
    "active": 1,
    "outcome": "Unsettled"
}'

```json
{
    "name": "2",
    "event": "Michael x Stace",
    "price": 7.9,
    "active": true,
    "outcome": "Unsettled"
}
 ```

### [DELETE] Delete (inactive) Selection

| Method   | URL                        | Filters         | Authorization |
|----------|----------------------------|-----------------|---------------|
| `DELETE` | /selections/{name}/{event} | No filters      | Required      |

> **200 OK** | curl --request DELETE 'http://127.0.0.1:5000/selections/3/Michael x Stace' \
--header 'Authorization: Bearer <access_token>'

```json
{
    "message": "Selection inactivate"
}
 ```

## Displays

### [GET] Return all information in database (sports, events and selections)

| Method | URL      | Filters | Authorization |
|--------|----------|---------|---------------|
| `GET`  | /display | active  | No            |

> **200 OK** | curl --request GET 'http://127.0.0.1:5000/display'

```json
{
    "result": [
        {
            "name": "FOOTBALL",
            "slug": "FOOTBALL783",
            "active": 1,
            "events": [
                {
                    "name": "Internazionale x Liverpol",
                    "slug": "EUROPE LEAGUE",
                    "active": 1,
                    "type": "preplay",
                    "sport": "FOOTBALL",
                    "status": "Pending",
                    "scheduled_start": "2022-07-30 20:00:00.000000",
                    "actual_start": null,
                    "selections": [
                        {
                            "name": "1",
                            "event": "Internazionale x Liverpol",
                            "price": 1.2,
                            "active": 1,
                            "outcome": "Unsettled"
                        },
                        {
                            "name": "2",
                            "event": "Internazionale x Liverpol",
                            "price": 4.9,
                            "active": 1,
                            "outcome": "Unsettled"
                        },
                        {
                            "name": "X",
                            "event": "Internazionale x Liverpol",
                            "price": 8.0,
                            "active": 1,
                            "outcome": "Unsettled"
                        }
                    ]
                },
                {
                    "name": "Barcelona x Real Madrid",
                    "slug": "EUROPE LEAGUE",
                    "active": 1,
                    "type": "preplay",
                    "sport": "FOOTBALL",
                    "status": "Pending",
                    "scheduled_start": "2022-07-30 20:00:00.000000",
                    "actual_start": null,
                    "selections": [
                        {
                            "name": "X",
                            "event": "Barcelona x Real Madrid",
                            "price": 3.7,
                            "active": 1,
                            "outcome": "Unsettled"
                        }
                    ]
                },
                {
                    "name": "Chelsea x Real Madrid",
                    "slug": "EUROPE LEAGUE",
                    "active": 1,
                    "type": "preplay",
                    "sport": "FOOTBALL",
                    "status": "Pending",
                    "scheduled_start": "2022-07-30 20:00:00.000000",
                    "actual_start": null,
                    "selections": []
                }
            ]
        },
        {
            "name": "BASKETBALL",
            "slug": "BASKETBALL",
            "active": 1,
            "events": []
        },
        {
            "name": "HORSE RACING",
            "slug": "HORSE RACING",
            "active": 1,
            "events": []
        }
    ]
}
 ```

### [GET] Return all events with your specific sport

| Method | URL           | Filters                              | Authorization |
|--------|---------------|--------------------------------------|---------------|
| `GET`  | /events/sport | datemin \ datemax \ minimum \ status | No            |

> **200 OK** | curl --request GET 'http://127.0.0.1:5000/events/sport?datemin=2022-07-20&datemax=2022-07-31&minimum=1&status=Pending'

```json
{
    "sport": [
        {
            "FOOTBALL": [
                {
                    "name": "Internazionale x Liverpol",
                    "slug": "EUROPE LEAGUE",
                    "active": 1,
                    "type": "preplay",
                    "sport": "FOOTBALL",
                    "status": "Pending",
                    "scheduled_start": "2022-07-30 20:00:00.000000",
                    "actual_start": null
                },
                {
                    "name": "Barcelona x Real Madrid",
                    "slug": "EUROPE LEAGUE",
                    "active": 1,
                    "type": "preplay",
                    "sport": "FOOTBALL",
                    "status": "Pending",
                    "scheduled_start": "2022-07-30 20:00:00.000000",
                    "actual_start": null
                },
                {
                    "name": "Chelsea x Real Madrid",
                    "slug": "EUROPE LEAGUE",
                    "active": 1,
                    "type": "preplay",
                    "sport": "FOOTBALL",
                    "status": "Pending",
                    "scheduled_start": "2022-07-30 20:00:00.000000",
                    "actual_start": null
                }
            ]
        }
    ]
}
 ```

### [GET] Return all sports with a minimum number of active events

| Method | URL          | Filters    | Authorization |
|--------|--------------|------------|---------------|
| `GET`  | /sportsmin   | min_events | No            |

> **200 OK** | curl --request GET 'http://127.0.0.1:5000/sportsmin?min_events=3'

```json
{
    "sport": [
        {
            "name": "FOOTBALL",
            "slug": "FOOTBALL783",
            "active": 1
        },
        {
            "name": "TENNIS",
            "slug": "TENNIS",
            "active": 0
        }
    ]
}
 ```


### [GET] Return all events with a minimum number of active selections

| Method | URL          | Filters        | Authorization |
|--------|--------------|----------------|---------------|
| `GET`  | /eventsmin   | min_selections | No            |

> **200 OK** | curl --request GET 'http://127.0.0.1:5000/eventsmin?min_selections=2'

```json
{
    "events": [
        {
            "name": "Barcelona x Real Madrid",
            "slug": "EUROPE LEAGUE",
            "active": 1,
            "type": "preplay",
            "sport": "FOOTBALL",
            "status": "Pending",
            "scheduled_start": "2022-07-30 20:00:00.000000",
            "actual_start": null
        },
        {
            "name": "Internazionale x Liverpol",
            "slug": "EUROPE LEAGUE",
            "active": 1,
            "type": "preplay",
            "sport": "FOOTBALL",
            "status": "Pending",
            "scheduled_start": "2022-07-30 20:00:00.000000",
            "actual_start": null
        }
    ]
}
 ```