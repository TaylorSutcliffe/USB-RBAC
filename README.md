
# Group 11 

## RBAC system for accessing Urban Sciences Building Data  

## Setup and Run
###### with python 3 installed in parent directory 

```
py -3 -m venv venv

Set-ExecutionPolicy Unrestricted -Force

venv\Scripts\activate
```

(this should set up the virtual env for the project and you should see venv on the terminal)


###### first run requires:

```
pip install flask

pip install matplotlib
```

###### after that to run (and from now on as venv is set up)

```
set FLASK_APP = flaskr

set FLASK_ENV = development

py -m flask run
```

