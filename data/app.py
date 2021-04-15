from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import logging

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        header_data = {}
        _headers_dic  = dict(request.headers)

        header_data['Client IP'] =  request.remote_addr
        header_data['Host'] =  request.host
        header_data['User-Agent'] = _headers_dic['User-Agent']

        if 'Accept' in _headers_dic:
            header_data['Accept'] = _headers_dic['Accept']

        return jsonify(header_data)


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
    logging.basicConfig(format = logFormatStr, filename = "requests.log", level=logging.DEBUG)
    formatter = logging.Formatter(logFormatStr,'%m-%d %H:%M:%S')
    fileHandler = logging.FileHandler("summary.log")
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter(formatter)
    app.logger.addHandler(fileHandler)
    app.logger.addHandler(streamHandler)
    app.logger.info("Logging is set up.")
    app.run(debug=True, host='0.0.0.0', port=80)
