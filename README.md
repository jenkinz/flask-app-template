# Flask App Template

## Prerequisites

- [Python 3.8 or greater](https://www.python.org/downloads/)

## Setup

1. Install `pipenv` (if not already installed):

		python3 -m pip install --user pipenv

2. Create and activate virtual environment for project:

		pipenv shell

3. Install required packages into virtual environment (including development)
   and activate the required `pre-commit` hooks:

		pipenv install --dev
		pre-commit install

4. Run the application (as a local development server):

		FLASK_ENV=dev python app.py


**Note:** When creating a new project from this template, feel free to adjust 
the package dependency versions used by installing the desired versions into 
the virtual environment and running `pipenv lock`. Then, commit the modified 
`Pipfile.lock` file. 

## Other Tools and Recommendations

- For testing a REST API, install [Postman](https://www.getpostman.com/downloads/)
- Follow REST HTTP method best practices while implementing an API: 
  https://restfulapi.net/http-methods/  

## TODOs

- Add tests (run with `pytest`)
- Add `tox` configuration (to run lint and tests with multiple python versions)
- Make into a package (currently a module)
- Add database (SQLAlchemy)
- Review http://alanpryorjr.com/2019-05-20-flask-api-example/ for best pratcies 
  including test-driven development (TDD)
