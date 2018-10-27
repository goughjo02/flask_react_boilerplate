import os
from flask_restful import Api, Resource, reqparse
from flask import Flask, send_from_directory

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import asyncio
import websockets

app = Flask(__name__, static_folder='react_app/build')
api = Api(app)
socketio = SocketIO(app)

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("react_app/build/" + path):
        return send_from_directory('react_app/build', path)
    else:
        return send_from_directory('react_app/build', 'index.html')

@socketio.on('connect')
def connect_handler():
    print("hello world")
    emit('my_response', {'data': 'Connected'})

@socketio.on('my_event')
def connect_handler():
    print("my event")
    emit('my response', {'data': 'Connected'})
# class Data(Resource):
#     def get(self, jwt):
#         print(self)
#         parser = reqparse.RequestParser()
#         parser.add_argument("token", required=False)
#         args = parser.parse_args()
#         if(args["token"] == jwt["token"]):
#             return data, 200
#         return "token incorrect", 401

# api.add_resource(Data, "/data")

if __name__ == '__main__':
    socketio.run(app)
    # app.run(use_reloader=True, port=5000, threaded=True, debug=True)