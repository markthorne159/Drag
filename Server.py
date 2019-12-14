from flask import Flask
import os

ServerApp = Flask(__name__)
port = int(os.environ["PORT"])

@ServerApp.route('/',methods=['POST'])
def Hello():
    return "Hello world!"

ServerApp.run(port=port,host="0.0.0.0")
