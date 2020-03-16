### Create virtual environment

``virtualenv fvenv -p python3.X``
### Activate virtual environment

``source fvenv/bin/activate``

### Install dependencies
``pip install -r requirements.txt``

### Run the project 
``uvicorn main:app --reload --host 0.0.0.0 --port 8000``