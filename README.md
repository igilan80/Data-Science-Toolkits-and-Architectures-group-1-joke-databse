# Data-Science-Toolkits-and-Architectures-group-1-joke-databse


## Installation of requirements 
Make sure you have [Docker](https://docs.docker.com/get-docker/), [Docker Compose](https://docs.docker.com/compose/install/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed. 
The project was built with the following versions:
- git 2.43.0
- docker 27.3.1
- docker-compose 1.29.2

## Creation of a .env
In the project folder, create a file called `.env` with the following content:
```shell
POSTGRES_USER=your_user_name
POSTGRES_PASSWORD=your_pwd
POSTGRES_DB=joke_db
PGADMIN_EMAIL=your_email
PGADMIN_PASSWORD=your_pwd
DB_NAME=ms3_jokes
```
## Run Containers
You can run the entire application by executing the following command in the CLI when you are in the root directory.
```shell
docker-compose up
```
Then, the example Python script is executed, which creates 2 jokes from `pyjokes`, adds them to the database, modifies the last added joke, and deletes the other joke. This shows all the functionalities of this small project.