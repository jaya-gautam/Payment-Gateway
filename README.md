# Payment-Gateway

## Getting Started

Setup project environment with virtualenv and pip

```bash
Make a directory to start the project (Payement-Gateway)
cd Payment-Gateway/
python -m venv project-env
source project-env/bin/activate
pip install -r requirements.txt
```

Copy the code from git to Payment-Gateway folder

Application Name is APIapp

## Run the Code

```bash
cd APIapp/
change setting.py according to the server IP (otherwise can be run on localhost)
python manage.py runserver 0.0.0.0:8000
```

The resulting structure should look like this:

    PaymentGateway/
    |-- db.sqlite3
    |-- manage.py
    |-- PaymentGateway/
    |   |-- setting.py
    |   |-- urls.py
    |   |-- wsgi.py
    |   |-- __init__.py
    
    [...]
    |-- APIapp/
    |   |-- models.py
    |   |-- views.py
    |   |-- serializers.py
    |   |-- admin.py
    [...]
