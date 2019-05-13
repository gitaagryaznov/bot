from flask import Flask
from flask import Request
from flask import jsonify
import json
import  requests
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
URL='https://api.telegram.org/bot829296538:AAEgtZF4ME9nzLv_mMFoG2SkRWSDUNL4CSE/'
def write_json(data,filename='answer.json'):
    with open(filename,'w') as f:
        json.dump(data,f,indent=2,ensure_ascii=false)

def send_massage(chat_id,text='bla bla bla'):
    answer={"chat_id":chat_id,'text':text}
    r=requests.post(URL+'sendmessage',json=answer)
    return r.json()

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        r=request.get_json()
        chat_id=r['message']['chat']['id']
        message=r['message']['text']
        send_massage(chat_id,text='text')
        #write_json(r)
        return jsonify(r)
    return 'WELCOM TEST курва'

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
