from flask import Flask,render_template
import os

ServerApp = Flask(__name__)
port = int(os.environ["PORT"])

@ServerApp.route('/',methods=['GET'])
def Hello():
    return render_template("index.html")

ServerApp.run(port=port,host="0.0.0.0")
