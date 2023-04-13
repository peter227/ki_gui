# KI/GUI - Python-flask ORM
Workshop for showing database orm in python flask
## Installation
To clone this repository, run the following command:
```bash
git clone https://github.com/peter227/ki_gui.git
```
Install virutal enviroment
```bash
py -m pip install --user virtualenv
```
Create a virtual environment
```bash
py -m venv env
```
Activate a virtual environment
```bash
.\env\Scripts\activate
```
Install requirements from requirements.txt file
```bash
py -m pip install -r requirements.txt
```
Docker compose detached
```bash
docker compose up -d
```
We can see if everything went fine by going to http://localhost:9090 and seeing phpmyadmin, if not, don't worry, we'll find out what the problem is :)

Now we need to run migration to create tables in our db, so let's run this command
```bash
flask db upgrade
```
Now if we look in phpmyadmin we should see already created tables.

One more thing we need to import data to our database. We can do this be following steps:

1.
![Alt text](https://github.com/peter227/ki_gui/blob/main/phpmyadmin_1.png)

2.
![Alt text](https://github.com/peter227/ki_gui/blob/main/phpmyadmin_2.png)

3.
![Alt text](https://github.com/peter227/ki_gui/blob/main/phpmyadmin_3.png)

Alternative way without phpmyadmin:
```bash
# copying a file to docker container
docker cp ./ki_gui_db_final.sql c4f435751266:./
# opening the mysql command line client in docker container
docker exec -it c4f435751266  mysql -u root -p
```

In mysql command-line
```bash
USE ki_gui_db
SOURCE ki_gui_db_final.sql
\q
```


Now if we run that command, we should already see the web application
```bash
flask  --app app run
```
