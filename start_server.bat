pipenv sync --dev
set FLASK_ENV=development
set FLASK_APP=backend
pipenv run flask run --host=api.perfect-projects.link --cert=api.perfect-projects.link.cert --key=api.perfect-projects.link.key