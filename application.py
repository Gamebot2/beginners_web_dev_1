from flask import Flask, send_file, request

app = Flask(__name__, static_folder="./")

@app.route('/', methods=['GET'])
def render_index():
    return(send_file("index.html"))

@app.route('/example', methods=['GET'])
def return_example():
    return "THIS IS THE RESPONSE"

@app.route('/name', methods=['POST'])
def return_greeting():
    name = request.args['fname']
    greeting = "Hi there, " + name + "!"
    return greeting