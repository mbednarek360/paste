# imports
from flask import Flask
from flask import request
from flask_cors import CORS
from random import choice
import hashlib
import sys
import os

# init id length
idLen = 3

# init storage dir
store = sys.argv[2]
pas = sys.argv[3]

# setup app
app = Flask(__name__)
CORS(app)

# create paste
@app.route('/paste/create', methods=['POST'])
def create():
    passwd = request.args.get('pass', type = str)
    return writePaste(list(request.form.to_dict().keys())[0], passwd)

# delete paste
@app.route('/paste/delete', methods=['GET'])
def delete():
    passwd = request.args.get('pass', type = str)
    pid = request.args.get('id', type = str)
    return deletePaste(pid, passwd)

# delete with id and password
def deletePaste(pid, passwd):
    f = open(pas + '/' + pid, 'rb')
    if f.read() == hashlib.sha3_256(passwd.encode()).digest():
        f.close()
        os.remove(pas + '/' + pid)
        os.remove(store + '/' + pid)        
        return 'true'
    else:
        f.close()
        return 'false'

# write and return id
def writePaste(data, passwd):
    tid = genId()

    # recurse if exists
    if os.path.isfile(store + '/' + tid):
        writePaste(data, passwd)

    # all good
    else:
        f = open(store + '/' + tid, 'w')
        f.write(data)
        f.close()
        f = open(pas + '/' + tid, 'wb')
        f.write(hashlib.sha3_256(passwd.encode()).digest())
        f.close()
        return tid

# generate random id
def genId():
    out = ""
    for _ in range(idLen):
        out += choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    return out

# start server
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=80)