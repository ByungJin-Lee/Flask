from flask import Flask

app = Flask(__name__)

#url routing -> url 접근시, 해당 함수가 실행됨
@app.route('/')
def hello():
    return "Hello pybo!"