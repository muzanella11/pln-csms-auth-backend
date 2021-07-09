# PLN Contractor Safety Management System Auth Backend

> PLN Contractor Safety Management System authentication system

## Build Setup

``` bash
# install dependencies
$ pip install -r requirements.txt

# run flask
$ flask run 

# or run scripts
$ . bin/run.sh

# db migration
$ python -m app.migrations.db_migration

# or run scripts
$ . bin/migrate.sh

# update pip package
$ pip freeze > requirements.txt
```

## Run with Docker

```bash
### Run with docker ###
# Building your docker container
$ docker build -t your_app_name_images .

# Run the container
$ docker run -it -p 5002:5002 your_app_name_images
######################
```
