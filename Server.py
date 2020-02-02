from flask import Flask,render_template
import os
import sqlite3

ServerApp = Flask(__name__)
port = int(os.environ["PORT"])

@ServerApp.route('/',methods=['GET'])
def Hello():
    print ("Homepage loaded!")
    return render_template("index.html")

ServerApp.run(port=port,host="0.0.0.0")
