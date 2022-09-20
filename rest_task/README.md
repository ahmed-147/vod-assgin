# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

# Sites API

Sites api is a Rest API that allows to deal with sites data.

The app allows :

1) List Sites - all sties, Able to filter by Active status, Region or both.
2) Export Sites date as CSV file.
3) Import Sites date by CSV file to create them.
4) Create and list requests.
5) Add questions and require that they include question and answer text.

## Requirements
- Python 3.6
- Django 3.1
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```
You have to start up Django's development server by negative `rest_task/resttask`.
```
python manage.py runserver
```

## Structure
We can test the API using [curl](https://curl.haxx.se/), or we can use [Postman](https://www.postman.com/)

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `sites`, so we will use the following URLS - `/sites/` and `/sites/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/sites` | GET | READ | Get all sites
`api/sites/import/` | POST | CREATE | Create all sites in CSV file
`api/sites/export/` | GET | READ | Get all sites and export CSV file 
`api/requests/` | GET | READ | Get all requests
`api/requests/:id` | GET | READ | Get a single request
`api/requests`| POST | CREATE | Create a new request
`api/requests/:id` | PUT | UPDATE | Update a request
`api/requests/:id` | DELETE | DELETE | Delete a requests



### GET api/sites
- General:
    1. Returns all the sites.
    2. Returns the sites filtered by active or region or both.

- Sample: curl http://127.0.0.1:8000/api/sites
```bash
 HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 91,
        "name": "site 3",
        "region": "region 3",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "yes"
    },
    {
        "id": 92,
        "name": "site 4",
        "region": "region 4",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "yes"
    },
    {
        "id": 95,
        "name": "site 7",
        "region": "region 7",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "no"
    },
    ...
]
```

- Sample: curl http://127.0.0.1:8000/api/sites?active=no
```bash
 HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 91,
        "name": "site 3",
        "region": "region 3",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "yes"
    },
    {
        "id": 92,
        "name": "site 4",
        "region": "region 4",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "yes"
    },
    {
        "id": 95,
        "name": "site 7",
        "region": "region 7",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "no"
    },
    ...
]
```

- Sample: curl http://127.0.0.1:8000/api/sites?active=no
```bash
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 4,
        "name": "site 6",
        "region": "region 6",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "no"
    }
]
```


### GET api/sites/export/
- General:
    1. Returns all the sites.
    2. Export CSV file to media directory.

- Sample: curl http://127.0.0.1:8000/api/sites/export/
```bash
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 99,
        "name": "site 3",
        "region": "region 3",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "yes"
    },
    {
        "id": 103,
        "name": "site 7",
        "region": "region 7",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "no"
    },
    {
        "id": 104,
        "name": "site 8",
        "region": "region 8",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "no"
    },
    ...
]

```

### POST api/sites/import/
- General:
    1. Import sites by CSV file and create.
    2. Return sites that created.

- Sample: curl -i -X POST -H "Content-Type: multipart/form-data" -F "sites=@/vod-assgin/rest_task/resttask/static/test_sheet_valid.csv;type=text/csv" http://127.0.0.1:8000/api/sites/import/
```bash
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[
    {
        "id": null,
        "name": "site 3",
        "region": "region 3",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "yes"
    },
    {
        "id": null,
        "name": "site 4",
        "region": "region 4",
        "latitude": 0.0,
        "longitude": 0.0,
        "active": "yes"
    },
    ...
]

```

### GET /api/requests
- General:
    1. Returns all requests


- Sample: curl http://127.0.0.1:8000/api/requests
```bash
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 2,
        "reuest_no": 67764,
        "details": "req 1",
        "SiteName": 91
    },
    {
        "id": 3,
        "reuest_no": 67764,
        "details": "req 2",
        "SiteName": 97
    }
]
```

### Post /api/requests
- General:
    1. Creates a new request based on a payload

- Sample: curl -X POST http://127.0.0.1:8000/api/requests -H "Content-Type: application/json" -d '{ "reuest_no": 655643, "details": "testx", "SiteName": 96 }'
```bash
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 4,
    "reuest_no": 655643,
    "details": "testx",
    "SiteName": 96
}
```

### GET api/requests/<int:pk>
- General:
    1. Return the request that have this ID.

- Sample: curl -X DELETE http://127.0.0.1:8000/api/requests/2
```bash
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "reuest_no": 67764,
    "details": "req 1",
    "SiteName": 91
}
```

### Delete api/requests/<int:pk>
- General:
    1. Delete the request that have this ID.

- Sample: curl -X DELETE http://127.0.0.1:8000/api/requests/2
```bash
{
  "message": "Question was deleted",
  "success": true
}
```

### UPDATE api/requests/<int:pk>
- General:
    1. UPDATE the request that have this ID.

- Sample: curl -X UPDATE http://127.0.0.1:8000/api/requests/ -H "Content-Type: application/json" -d '{ "reuest_no": 655643, "details": "tesddtx", "SiteName": 96 }'
```bash
{
    "id": 5,
    "reuest_no": 655643,
    "details": "tesddtx",
    "SiteName": 96
}
```


