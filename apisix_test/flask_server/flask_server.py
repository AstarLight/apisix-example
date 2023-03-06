from flask import Flask
import sys  

app = Flask(__name__)

PORT = 9990

@app.route('/get_result_http', methods=["GET"])
def hello_world():
    return 'Hello flask server!'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])
    app.run(host="127.0.0.1", port=PORT)l