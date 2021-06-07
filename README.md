# intern_test

A simple Github Login page. Used flask, HTML, CSS and React.js.

Steps:

### Backend

1. Download the project
2. Navigate to the intern app directory
3. Setup the virtual env by `python -m venv <env-name>`
4. Activate env by `source  <env-name>/bin/activate`
4. Install requirements using   `pip install -r requirements.txt`
4. navigate to the backend_api
6. run the following commands
```
export FLASK_APP=app_api.py
export FLASK_ENV=deployment
flask run
```
*Note* :

If want app to load with changes done without restarting server repeatedly, set debug to on by using `export FLASK_DEBUG=1 `

### Frontend

1. Navigate to the intern app directory
2. install dependencies by `npm install`
3. Start server by `npm run start-api`
4. To start react app run `npm run start`

__env variables__

* Secret key
* etc