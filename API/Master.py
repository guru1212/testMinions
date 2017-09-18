'''
Created on Sep 14, 2017

@author: gsethura
'''

from flask import Flask, request,jsonify
from flask_httpauth import HTTPBasicAuth
from functools import wraps
from werkzeug.exceptions import BadRequest
from minionServers import testMinions

app = Flask(__name__)
auth = HTTPBasicAuth()

user_data = {"admin":"pass123"}

@auth.verify_password
def verify_password(uname,password):
    if not (uname and password):
        return False
    return user_data.get(uname) == password
    
@auth.get_password
def get_pw(username):
    if username in user_data:
        print username
        return user_data.get(username)
    return None

def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except BadRequest, e:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper

@app.route("/")
@auth.login_required
def hello():
    return "Hello World"


@app.route('/master/api/run',methods=['POST'])
@auth.login_required
@validate_json
def master(): 
     # get host, username, password
    dat = {'host':request.json['host'], 'username':request.json['username'], 'password':request.json['password']}
    #Pass ssh detatils to minion
    master = testMinions(dat['host'], dat['username'], dat['password'])
    #get list of operations to be performed
    operationsList = request.json['todo']
    listMinionResp = master.testsshMinion(operationsList)
    print "---master----", listMinionResp
    
    return jsonify(listMinionResp)



@app.route('/master/api/json',methods=['POST'])
@validate_json
def testjson():
    # get host, username, password
    dat = {'host':request.json['host'], 'username':request.json['username'], 'password':request.json['password']}
    #Pass ssh detatils to minion
    master = testMinions(dat['host'], dat['username'], dat['password'])
    #get list of operations to be performed
    operationsList = request.json['todo']
    listMinionResp = master.testsshMinion(operationsList)
    print "---master----", listMinionResp
    
    return listMinionResp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
