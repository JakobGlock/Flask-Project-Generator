# Flask Project Generator

A quick and dirty CLI-tool to generate a template Flask project, this has been created for my own personal use, so it is tailored towards my own preferences.

Once installed and run, it will create the following folder structure and files:

```
my_flask_project/
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   └── templates
│       └── index.html
├── README.md
├── requirements.txt
├── run.py
└── venv
```

This will setup a python virtual environment and install the required packages for the project.

# Setup & Running on Linux

Clone repo onto your machine.

`git clone https://github.com/JakobGlock/Flask-Project-Generator.git`

Navigate to the project directory from within a terminal window.

`cd /path/to/cloned/repo`

Install into your python path using pip or pip3 with the following command:

`pip3 install -e .`

You should then be able to call the program using:

`fpgen project-name`

This will run the script and setup the Flask project.

Once complete, go to the project folder and activate the venv using:

`source venv/bin/activate`

Then run the follwing command to start the server:

`python3 run.py`

Dont forget to setup a database and put in the correct credentials in to __init__.py


# Tested

I have only tested this on Linux.

# Dependencies

Here is a list of the packages used within this project, this is a dump of the `requirements.txt` file:

```
Click==7.0
Flask==1.0.3
flask-marshmallow==0.10.1
Flask-SQLAlchemy==2.4.0
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
marshmallow==2.19.2
marshmallow-sqlalchemy==0.16.3
pkg-resources==0.0.0
PyMySQL==0.9.3
six==1.12.0
SQLAlchemy==1.3.4
Werkzeug==0.15.4
```
