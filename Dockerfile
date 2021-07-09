FROM python:3.8

# create destination directory
RUN mkdir -p /usr/src/pln-csms-auth-app
WORKDIR /usr/src/pln-csms-auth-app

# copy the app, note .dockerignore
COPY . /usr/src/pln-csms-auth-app/

RUN pip install -r requirements.txt

# If you found cant connect to MySQL on server 'xxx' and you put mysql in docker
# That's the subnet ID, what address does this show for you 
# $ docker inspect [container] | grep -i ipaddress
# If you're trying to change the address mysql is listening on using Docker's ports it will only map that for connections going to the Docker host. So directly connecting to the container's address would still be using 3306 unless you edit the my.cnf

# local development env variable
ENV ENVIRONMENT=local \
    PYTHON_MIGRATE=FALSE \
    FLASK_APP=main.py \
    FLASK_ENV=development \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5002 \
    DB_HOST=172.17.0.2 \
    DB_USERNAME=root \
    DB_PASSWORD=root \
    DB_NAME=pln_csms_auth \
    APP_CSMS_HOST=http://127.0.0.1:5000 \
    APP_AUTH_HOST=http://127.0.0.1:5002

# expose 5002 on container
EXPOSE 5002

# start the app
CMD [ "python", "-m" , "flask", "run" ]
