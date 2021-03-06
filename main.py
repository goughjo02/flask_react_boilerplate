import os
from flask_restful import Api, Resource, reqparse
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='react-app/build')
api = Api(app)

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("react-app/build/" + path):
        return send_from_directory('react-app/build', path)
    else:
        return send_from_directory('react-app/build', 'index.html')


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
    app.run(host= '0.0.0.0', use_reloader=True, port=33, threaded=True, debug=True)