# --------------------------------------------------------------------------------
# FaceExtractor uses the function extractFaces for returning the facial zone of a
# frame. As there might be more faces recognized, previous experience on the usage
# of the model on this dataset dictates that the first frame is usually the correct
# one, the others being most of the time false positives.
# --------------------------------------------------------------------------------

import cv2
import os
import numpy as np

base_dir = os.path.dirname(__file__)


class FaceExtractor:

    def __init__(self, txtPath, modelPath):
        self.__prototxt_path = os.path.join(base_dir + txtPath)
        self.__caffemodel_path = os.path.join(base_dir + modelPath)
        self.__model = cv2.dnn.readNetFromCaffe(self.__prototxt_path, self.__caffemodel_path)

    def extractFaces(self, frame):
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

        self.__model.setInput(blob)
        detections = self.__model.forward()

        for i in range(0, detections.shape[2]):
            box = detections[0, 0, 0, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            confidence = detections[0, 0, 0, 2]

            # If confidence > 0.5, save it as a separate file
            if confidence > 0.5:
                try:
                    # frame = frame[startY - 10:endY + 10, startX - 10:endX + 10]
                    return frame[startY:endY, startX:endX]
                except:
                    return frame[startY:endY, startX:endX]

        return None
