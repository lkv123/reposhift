from flask import Flask
from flask import request
from tkinter import messagebox

#WA[
from whatsapp import Client
expected_token = 'cornerstone119596'
#]WA

app = Flask(__name__)



@app.route('/')
def hello_world():
    messagebox.showerror("Error", "error message")
        return 'Hello World!'

@app.route('/msg', methods = ['POST'])
def msg():
    to = request.form['to']
    return str(to)

@app.route('/sendmsg')
def sendmsg():
    to = request.args.get('to')
    msg = request.args.get('msg')
    token = request.args.get('token')
    if(str(token) == expected_token):
        client = Client(login='918074368661', password='DvU9XpDTFnry/KUr6tePbiSMsuY=')
        res = client.send_message(to, msg)  
    
    else:
        res = 'Unauthorized'
    
    return str(res)

if __name__ == '__main__':
    app.run()
