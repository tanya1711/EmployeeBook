<center><h1> Employee Book </h1></center>
 
It a Web app made to perform basic CRUD operations on the employees of any company
<hr>

- Installing the Requirements:

~~~

pip install -r requirements.txt

~~~ 

- Upgrading the database:

~~~

flask db init

flask db migrate

flask db upgrade

~~~

- Set environment variable in windows to either production, development, or testing.**

~~~
 FLASK_CONFIG=development
  
 FLASL_APP=run.py
  
 flash run

~~~

- Set environment variable in Linux to either production, development, or testing.**

~~~ 

export FLASK_CONFIG=development
  
export FLASK_APP=run.py 
  
flask run 
~~~
