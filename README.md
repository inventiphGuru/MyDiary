# MyDiary
<a href="https://codeclimate.com/github/inventiphGuru/MyDiary/maintainability">
<img src="https://api.codeclimate.com/v1/badges/1b2d513327c14f928799/maintainability" /></a>

<a href="https://codeclimate.com/github/inventiphGuru/MyDiary/test_coverage">
<img src="https://api.codeclimate.com/v1/badges/1b2d513327c14f928799/test_coverage" /></a>

this is an Api that allows CRUD functionilty to the Mydiary app.
The following are the http verbs and end points of the Api.

#functions implemented (End points):
* Get all diary entries.  --- method [GET]
* Get a specific diary entry. --- method [GET]
* Add an entry  --- Method [POST]
* Modify an entry. --- method [PUT]

# Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer. 
If not, you can get python3 by running

		$ pip install python3
		
* After this, ensure you have installed virtualenv globally as well. If not, run this:

        $ pip install virtualenv

* Git clone this repo to your PC
 
        $ git clone https://github.com/inventiphGuru/MyDiary.git
		
* # Pre-requisite dependencies
    1.get into your the cloned repo 
     
        $ cd MyDiary
     

    2. Create and start your virtual environment in python3:
         
		 * #Create
        $ virtualenv -p python3 venv
		
		* #start
        $ pip install autoenv
        
* #Install your requirements from within the virtualenv
    
    $ pip install -r requirements.txt

* ## Running It
    On your terminal navigate to the v1 folder
    ```
	 $ cd myDiary
	(myDiary)$ cd api
	 (api)$ Cd v1
	 ```
	 run the server using this one simple command:
	 ``` $ (v1)$ python app.py
 	 ```
	You can now access the app on your local browser by using
    ```
    http://localhost:5040/my_entries
    ```
   
 * ##test creating entries using Postman
