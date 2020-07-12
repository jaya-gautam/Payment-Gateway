# Payment-Gateway

Setup project environment with virtualenv and pip

Make a directory to start the project (Payement-Gateway)
cd Payment-Gateway/
virtualenv project-env
source project-env/bin/activate
pip install -r requirements.txt

Copy the code to from git to Payment-Gateway folder

# Application Name is APIapp

cd APIapp/
change setting.py according to the server IP (otherwise can be run on localhost)
python manage.py runserver 0.0.0.0:8000
