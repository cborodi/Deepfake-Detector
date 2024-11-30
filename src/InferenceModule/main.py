# --------------------------------------------------------------------------------
# This is the starting point of the program. It is designed as a server and
# instantiates the InferenceModule class. This is basically a Flask backend.
# It handles POST requests on /videocheck and /framecheck destinations receiving
# files in format .mp4, .avi, .mov and .jpg, .jpeg, .png respectively.
# In terms of returns, the messages have code 200 for success and 400 for error.
# The response is json encoded. For the video part, the result contains total frames
# fake frames, real frames and percentages. For the frame part, the prediction is returned.
# --------------------------------------------------------------------------------


from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin
import os

from InferenceModule import InferenceModule

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
im = InferenceModule()

@app.route('/videocheck', methods = ['POST'])
@cross_origin()
def video_check():
    file_name = str(request.files.get('file').filename)
    file_storage = request.files['file']
    file_storage.save(file_name)

    extension = file_name.split(".")[-1]

    if extension not in ['mp4', 'MOV', 'avi', 'mov', 'MP4', 'AVI']:
        os.remove(file_name)
        return jsonify(isError=True,
                       message="File Format Error",
                       statusCode=400), 400


    result = im.video_inference(file_name)

    if len(result) == 1:
        os.remove(file_name)
        return jsonify(isError=True,
                       message="Error opening the file",
                       statusCode=400), 400

    os.remove(file_name)
    return jsonify(isError=False,
                   message="Success",
                   totalFrames=result[1],
                   faceFrames=result[2],
                   realFrames=result[3],
                   fakeFrames=result[4],
                   realProbability=result[5],
                   fakeProbability=result[6],
                   statusCode=200), 200

@app.route('/framecheck', methods = ['POST'])
@cross_origin()
def frame_check():
    file_name = str(request.files.get('file').filename)
    file_storage = request.files['file']

    file_storage.save(file_name)
    extension = file_name.split(".")[-1]

    if extension not in ['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG']:
        os.remove(file_name)
        return jsonify(isError=True,
                       message="File Format Error",
                       statusCode=400), 400

    result = im.single_frame_inference(file_name, probability=True)

    if result is None:
        os.remove(file_name)
        return jsonify(isError=True,
                       message="Error Processing Photo",
                       statusCode=400), 400

    predicted = None

    if result[0] == 0:
        predicted = 'Fake'
    else:
        predicted = 'Real'

    probability = float(result[1])

    os.remove(file_name)
    return jsonify(isError=False,
                   message="Success",
                   predicted=predicted,
                   probability=probability,
                   statusCode=200), 200
