from flask import Flask, render_template, request
from flask import jsonify, send_file
from flask_cors import CORS
import glob
import os
import time

ip_addr = open('./ip_addr', encoding="utf8").readlines()[0].replace('\n', '')
public_ip = open('./ip_addr', encoding="utf8").readlines()[1].replace('\n', '')

app = Flask(__name__, static_url_path="/static") 
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app)

@app.route("/upload_docs", methods=['POST'])
def upload_image():
    files = request.files
    image_path = "./static/data/docs/uploaded"
    image_name = str(time.time()) + ".docx"
    try:
        os.makedirs(image_path)
    except OSError:
        pass
    
    for file_name in files:
        files[file_name].save(image_path + "/" + image_name)
    
    res = {'link': 'http://' + public_ip + ':5006/static/data/docs/uploaded/' + image_name}
    
    return jsonify(res)


@app.route("/upload_docs_temp", methods=['POST'])
def upload_image_temp():
    files = request.files
    image_path = "./static/data/docs/temp"
    image_name = str(time.time()) + ".docx"
    try:
        os.makedirs(image_path)
    except OSError:
        pass

    for file_name in files:
        files[file_name].save(image_path + "/" + image_name)

    res = {'link': 'http://' + public_ip + ':5006/static/data/docs/temp/' + image_name}

    return jsonify(res)


@app.route("/delete_docs", methods=['POST'])
def delete_docs():
    files = request.files
    image_path = "./static/data/docs"
    image_name = str(time.time()) + ".docx"
    try:
        os.makedirs(image_path)
    except OSError:
        pass

    for file_name in files:
        files[file_name].save(image_path + "/" + image_name)

    res = {'link': 'http://' + public_ip + ':5005/static/data/images/' + image_name}

    return jsonify(res)


@app.route("/")
def index():
    return render_template("index.html")

if (__name__ == "__main__"): 
    app.run(threaded=True, host=ip_addr, port = 5006)
    