#testMinions
Python Flask API project

**GIT remote repository URL:**

https://github.com/guru1212/testMinions.git

Objective: This Python Flask REST API project acts as a master which control a bunch of servers as minions.
This project exposes the below URL to the client to receive the necessary data in JSON format to login to minions and perform some operations.
http://<hostname:5000>/master/api/run/

Data required to perform the operations:
1) host name, username and password of the server to login.
2) operations to be performed on that server.
Sample JSON request as below.


{
	"host":"vm-gsethura-002",
	"username" : "root",
	"password":"Cisco123",
	"todo" : [
		{"operation1":"mkdir"},
		{"operation2":"ls"}
	]
}

How to Dockerize Python Flask project:
Once the files from GIT hub is pulled to local, launch Docker Quickstart Terminal and change directory to that path.


