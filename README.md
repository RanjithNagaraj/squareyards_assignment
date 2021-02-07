# squareyards_assignment

_To find the Coordinates of the input file I created the Web application using Django Frameowork which outputs the excel file with the latitude and longitude values for those inputs_


_Steps to run this application_

1. Create a project folder,inside the project folder create an virtual environment ******```syntax:python -m venv /path/to/new/virtual/environment```******

2. To Activate the virtual enmvironment  ******```cd /path/to/new/virtual/environment/lib/scripts activate ```******
3. Once you get into the environment install the dependencies using  ******```pip install -r requirments.txt ```******
4. Finally run this command  ******```python manage.py runserver ```****** inside the root directory to up the WSGI Server.
5. Once the server is up and running you could able to upload the input file.
6. Enter the below ```URL``` in the browser.
7. Once you get the lamding page , download the ```INPUTFILE``` from the repository and upload the file in the file upload form.
8. Once the inputfile is processed by our application, output file will be automatically downloaded from the browser which contains the latitude and longitude values and the address.

``` URL: ``` ******``` http://127.0.0.1:8000/geocoding/ ```******

``` INPUTFILE:  ``` https://github.com/RanjithNagaraj/squareyards_assignment/blob/master/geocodeinputs.xlsx


###### Landing Page

![Landingpage](https://github.com/RanjithNagaraj/squareyards_assignment/blob/master/landingpage.png)


###### Output PNG

![outputpage](https://github.com/RanjithNagaraj/squareyards_assignment/blob/master/output.png)




``` OUTPUTFILE:  ```  ******``` https://github.com/RanjithNagaraj/squareyards_assignment/blob/master/squareyards/lat_lng.xls ```******
