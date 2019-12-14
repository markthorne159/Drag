from flask import Flask

ServerApp = Flask(__name__)

@ServerApp.route('/')
def Hello():
    return "Hello world!"

if __name__ == '__main__':
    ServerApp.run()
