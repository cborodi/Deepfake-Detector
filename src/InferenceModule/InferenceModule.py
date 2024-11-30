# --------------------------------------------------------------------------------
# This module is meant to be the center point of the task of verifying the videos.
# Here, the input videos will be split frame by frame and checked for the real/fake
# validation. This module is also designed for single frame inference too, using
# additional, pre-set variables in the single_frame_inference function.
# --------------------------------------------------------------------------------


import tensorflow as tf
from PIL import Image
import numpy as np
import cv2

from FaceExtractor import FaceExtractor


class InferenceModule:

    def __init__(self):
        self.model = tf.keras.models.load_model('content/model_large')
        self.FaceExtractor = FaceExtractor('/modeldata/deploy.prototxt', '/modeldata/weights.caffemodel')

    def single_frame_inference(self, frame, from_video=False, probability=False):
        labels = ['Fake', 'Real']

        if from_video is False:
            try:
                img = Image.open(frame)
                img = np.asarray(img)
            except:
                return None
        else:
            img = frame

        img = self.FaceExtractor.extractFaces(img)

        if img is None:
            # print("No face found!")
            return None

        try:
            img = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
        except:
            return None
        p = np.true_divide(img, 255)
        p = p.reshape(1, 256, 256, 3)

        # plt.imshow(img)

        prediction = self.model.predict(p)
        # print(prediction)
        ret = None
        if (prediction > 0.5):
            predicted_label = labels[1]
            ret = 1
        else:
            predicted_label = labels[0]
            ret = 0

        # display the result
        # print("Predicted label is {}".format(predicted_label))
        if probability == True:
            return [ret, prediction]

        return ret

    def video_inference(self, video):
        cap = cv2.VideoCapture(video)

        # Check if camera opened successfully
        if (cap.isOpened() == False):
            # print("Error opening video stream or file")
            return [-1]

        totalFrames = 0
        faceFrames = 0
        realFrames = 0

        # Read until video is completed
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            else:
                im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pred = self.single_frame_inference(im_rgb, True)
                totalFrames += 1
                if pred is not None:
                    faceFrames += 1
                    if pred == 1:
                        realFrames += 1

        # When everything done, release the video capture object
        cap.release()

        # print("Percentage of real frames is " + str(realFrames / totalFrames))

        fakeFrames = totalFrames - realFrames
        return [1, totalFrames, faceFrames, realFrames, fakeFrames, realFrames / totalFrames, fakeFrames / totalFrames]


"""
for i, frameName in enumerate(frames):
    print("Photo " + str(i) + ":")
    im.single_frame_inference(frameName)
    print()


for i, videoName in enumerate(videos):
    print("Video " + str(i) + ", " + videoName + ":")
    im.video_inference("testing/" + videoName)
    print()
"""

"""

import os

directory_real = os.fsencode("D:/Code/Computer Vision and Deep Learning/InferenceModule/testing/original_sequences/actors/c23/videos")
directory_fake = os.fsencode("D:/Code/Computer Vision and Deep Learning/InferenceModule/testing/DeepFakeDetection/c23/videos")

for file in os.listdir(directory_real):
    filename = os.fsdecode(file)
    print("Video " + filename + ":")
    im.video_inference("testing/original_sequences/actors/c23/videos/" + filename)
    print()

for file in os.listdir(directory_fake):
    filename = os.fsdecode(file)
    print("Video " + filename + ":")
    im.video_inference("testing/DeepFakeDetection/c23/videos/" + filename)
    print()

"""