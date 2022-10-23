from flask import Flask, request, abort
import requests
import json
from project.Config import *

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello', 200

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        input = request.json
        reply_token = input['events'][0]['replyToken']
        message = input['events'][0]['message']['text']
        send = "your message is " + message
        ReplyMessage(reply_token, send, token)
        return request.json, 200

    elif request.method == 'GET':
        return 'This is method GET', 200


def ReplyMessage(Reply_token, TextMessage, Token):
    API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Token)
    print(Authorization)
    headers = {
        'Content-Type' : 'application/json; charset=UTF-8',
        'Authorization' : Authorization
    }

    data = {
        'replyToken' : Reply_token,
        'messages' : [{'type':'text','text':TextMessage}]
    }

    data = json.dumps(data)
    r = requests.post(API, headers=headers, data=data)
    return 200
