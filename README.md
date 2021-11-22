# AdjustHomeTask-backend

The backend of the AdjustHome application.

Done in Python, based on FastAPI.

## Requirements

* [Python](https://www.python.org/).
* [Uvicorn](https://www.uvicorn.org/).

### Install or update python itself

```console
sudo apt update
sudo apt -y upgrade
sudo apt install python3.10
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3.10-dev
sudo apt install -y python3.10-venv
```

- Create an empty python virtual environment in the project root directory:
```console
$ python3 -m venv .venv
```
Note: specify the right version of python if your default python3 points to one less than 3.9 (i.e. `python3.9 -m venv .venv`)

- Activate such virtual environment:
```console
$ . .venv/bin/activate
```

#### Install dependencies

```console
$ pip install -r requirements.txt
```

### IDE setup

Make sure the IDE uses the python environment you just created (Visual Studio Code automatically recognises the default `.venv/` created in the project directory)

### Application code

Modify or add SQLAlchemy models in `./backend/app/models/`,

Pydantic schemas in `./backend/app/schemas/`,

API endpoints in `./backend/app/endpoints/`,

CRUD (Create, Read, Update, Delete) utils in `./backend/app/cruds/`.

### Start app
```console
$ uvicorn main:app --reload
```

### Assumptions

The response model is not suggested, so an elegent way to inspect the performance matrices is to get the exported in to a CSV.

Possiblity to skip and limit the result is also present. 

### URLs

1. Show the number of impressions and clicks that occured before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.

```console
http://127.0.0.1:8000/?date_to=2017-06-01&group_by=channel%2Ccountry&sum_by=impressions%2Cclicks&order_by=clicks&order_dir=desc&skip=0&limit=100
```

2. Show the number of installs that occured in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

```console
http://127.0.0.1:8000/?date_from=2017-05-01&date_to=2017-05-31&os=iOS&group_by=date&sum_by=installs&order_by=date&order_dir=asc&skip=0&limit=100
```

3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

```console
http://127.0.0.1:8000/?date_from=2017-06-01&date_to=2017-06-01&country=US&group_by=os&sum_by=revenue&order_by=revenue&order_dir=desc&skip=0&limit=100
```

4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order

```console
http://127.0.0.1:8000/?country=CA&group_by=channel&order_by=cpi&order_dir=desc&skip=0&limit=100
```
