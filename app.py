from flask import Flask
from flask import request

#WA[
from whatsapp import Client
expected_token = 'pavan123'
#]WA

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/msg', methods = ['POST'])
def msg():
    to = request.form['to']
    return str(to)

@app.route('/sendmsg')
def sendmsg():
    to = 919787125779
    msg = 'hello from salesforce'
    token = 'pavan123'
    if(str(token) == expected_token):
        client = Client(login='919494850241', password='wedn6jcBJIWl9a7IpXME1iKAEm0=')
        res = client.send_message(to, msg)  
    
    else:
        res = 'Unauthorized'
    
    return str(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
