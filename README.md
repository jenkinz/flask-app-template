# Flask Application Template

This is an example Flask project, using my preferred project structure and
development environment setup. The instructions below are tailored for macOS.

This project implements the Flask tutorial from
the [official documentation](https://flask.palletsprojects.com/en/2.1.x/tutorial/)
. The application is called `flaskr` which is a simple blogging app. The
project is structured as a python package named `flaskr`.

## Development Setup

**Prerequisites:** Follow one-time steps
at https://github.com/jenkinz/python-project-template#one-time-steps-per-machine
, then return
here and run the commands below.

1. Run the following to create the Conda environment for this project:

        $ conda env create -f environment.yaml

2. Activate the environment by specifying the project name to `conda activate`:

        $ conda activate <name>
3. Verify the environment was activated correctly:

        $ conda env list         # should output all environments with a * next to the active env
        $ poetry --version       # should output Poetry version X.Y.Z

4. Install all Python dependencies:

        $ poetry install
5. Run the following commands to activate the required git pre-commit hooks:

        $ pre-commit install
6. Run the project test suite to verify everything is working:

        $ cd tests
        $ pytest .
7. Initialize the local sqlite database:

        $ export FLASK_APP=src/flaskr
        $ flask init-db
8. Optional: Create a PyCharm run configuration:
    - Select **Flask Server** as the type
    - Enter `flaskr` as the name
    - Select **Module** and enter `flaskr` in the **Target** field
    - Ensure `FLASK_ENV` is set to `development` and `FLASK_DEBUG` is checked
