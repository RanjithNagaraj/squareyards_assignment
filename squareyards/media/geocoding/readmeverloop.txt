# assignmentverloop

_To find a coordinates of a specific address I created api endpoints in django which will outputs the latitude and longitute in the json/xml formats using mapquest Geocoding api_

_Steps to run this application_

1.Create a project folder,inside the project folder create an virtual environment ******```syntax:python -m venv /path/to/new/virtual/environment```******
2.To Activate the virtual enmvironment  ******```cd /path/to/new/virtual/environment/lib/scripts activate ```******
3.Once you get into the environment install the dependencies using  ******```pip install -r requirments.txt ```******
4.Finally run this command  ******```python manage.py runserver ```****** inside the root directory to up the WSGI Server
5.Once the server is up and running you could able to use the below following endpoints


API Endpoints | Method
------------  | ------------
http://127.0.0.1:8000/getAddressDetails/ | POST
http://127.0.0.1:8000/getAddressDetails/reverse| POST

###### POST: getAddressDetails/
![getAddressDetails](https://github.com/RanjithNagaraj/assignmentverloop/blob/master/screenshots/geocoding.png )


###### POST: getAddressDetails/reverse
![getAddressDetails](https://github.com/RanjithNagaraj/assignmentverloop/blob/master/screenshots/reversecoding.png )