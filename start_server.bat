pipenv sync --dev
set FLASK_ENV=development
set FLASK_APP=backend
pipenv run flask run --host=api.perfect-projects.com --cert=api.perfect-projects.com.cert --key=api.perfect-projects.com.key