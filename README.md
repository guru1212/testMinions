# testMinions
Python Flask API project

**GIT remote repository URL:**

https://github.com/guru1212/testMinions.git

**Objective:** This Python Flask REST API project acts as a master which control a bunch of servers as minions.

This project exposes the below URL to the client to receive the necessary data in JSON format to login to minions and perform some operations.

http://<hostname:5000>/master/api/run/

**Data required to perform the operations:**

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

**How to Dockerize Python Flask project:**

Once the files from GIT hub is pulled to local, launch Docker Quickstart Terminal and change directory to that path.

**Build docker image:** docker build -t flask-python .

**To list the docker image created:** docker images

**To run the app inside the container:** docker run -d -p 5000:5000 --name flask-container flask-python

The above dockerize steps will install Python2.7 and the required modules/libraries and will start the python API application.

**To check the API:**
1) Open RestClient in mozilla Firefox. If this add-on is not installed then can be added to mozilla - https://addons.mozilla.org/en-US/firefox/addon/restclient/

2) In restclient, select method as post and URL - http://<hostname>:5000//master/api/run/
  Note: hostname is the default VM of the docker whcih gets configured at the time of launching Docker Quickstart Terminal. This IP should be displayed once docker is launched successfully.   
  
3) Add authentication: - Authentication->Basic Authentication: Username -> admin Passworrd -> pass123

4) Add headers: - Headers->Custom Headers-> Name : Content-Type Value: application/json

5) Add the above mentioned json payload in the body and click send.
