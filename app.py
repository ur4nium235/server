import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from scripts import label_image

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2>Image classifier!</h2>'

@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    if request.method == "GET":
        return  '<h2>Real-time predictions</h2>'

    data = request.json
    print("data", data)

    pathToImagePrediction = data.get('path')

    if checkingIfFileExists(pathToImagePrediction) == False:
        return jsonify("File not found!")
    else:
        return jsonify(label_image.prediction(pathToImagePrediction))

def checkingIfFileExists(pathToFile) :
    return os.path.isfile(pathToFile)

if __name__ == '__main__':
    app.run()
