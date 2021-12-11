# Billing API
This repository is based on the implementation of a simple API for the PayU [confirmation page](http://developers.payulatam.com/latam/en/docs/integrations/webcheckout-integration/confirmation-page.html).

## Installation

- Create [virtual environment](https://docs.python.org/es/3/tutorial/venv.html) with the command

    `python -m venv virtual-env`

- Activate the virtual environment:

    - In Linux or Mac:
    `source virtual-env/bin/activate`

    - Windows:
    `.\venv\Scripts\activate.bat`

    It should appear (venv) in the console. Whenever a new console is executed, the virtual machine has a libraries and dependencies other than those found in the normal Windows environment, this to maintain the integrity of the applications in the operating system.

- Install dependencies

    `python -m pip install -r requirements.txt`

- Perform database migration

    `python migrate.py`

## Execution

- With the virtual machine activated, run the following console command:

    `uvicorn app:app --reload --port 5000`

## Deployment

- For development:

    To build docker

    `docker build . -t yourrepository:development`

    To push docker

    `docker push yourrepository:development`

    To test docker locally

    `docker run -it -p 80:5000 yourrepository:development:development`


- For production:
    
    To build docker

    `docker build . -t yourrepository:development:latest`

    To push docker

    `docker push yourrepository:development:latest`

    To test docker locally

    `docker run -it -p 80:8000 yourrepository:development:latest`