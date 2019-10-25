# training.refarch.training.refarch.python-web-poc

#### how to run in local (I'm using macos)
* get code by cloning repo (git clone)

* create virtual environment , install app, and run app
  * pyvenv venv
  * source venv/bin/activate
  * pip install -e .
  * export FLASK_APP=app.controller
  * export FLASK_ENV=development
  * flask run

* access api (use postman)
   ``` GET localhost:5000/todos

      POST localhost:5000/todos/ -d '{ 
	     "title":"something-1", 
	    "done":"false"
      }'
    ```