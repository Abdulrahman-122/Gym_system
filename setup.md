first you need to modify the database server that you will work on;
1.in my case i will use mariadb as i am using arch linux
go into your db server; mariadb -u root -p
build a new database;  create database name ; in my case gym_system
make a user to control this datebase ; in my case; i made it gym_developer
then
create user gym_developer@localhost identified by 'password'

give him all privileges on that database; like this ;
GRANT ALL PRIVILEGES ON gym_system.* TO 'gym_developer'@'localhost';
flush privileges

check this on the server ; go into the server using this user and see whether you can update,create tables 
if you can okay go to next stage;
2.connect database  with flask 
 like this ;
 app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://gym_developer:password@localhost/gym_system"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
now go i will walk you through the files to understand how it's going
first; 
start loooking at;
--init--.py 
then
go to models.py
