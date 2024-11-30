

"""
import os
import cv2
import numpy as np

base_dir = os.path.dirname(__file__)
prototxt_path = os.path.join(base_dir + '/modeldata/deploy.prototxt')
caffemodel_path = os.path.join(base_dir + '/modeldata/weights.caffemodel')

model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

def createDataset(source, destination):
    if not os.path.exists(destination):
        print("New directory created")
        os.makedirs(destination)

    count = 0
    for file in os.listdir(base_dir + '/' +  source):
        file_name, file_extension = os.path.splitext(file)
        if (file_extension in ['.png', '.jpg']):
            image = cv2.imread(base_dir + '/' +  source + '/' + file)

            (h, w) = image.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

            model.setInput(blob)
            detections = model.forward()

            # Identify each face
            for i in range(0, detections.shape[2]):
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                confidence = detections[0, 0, i, 2]

                # If confidence > 0.5, save it as a separate file
                if (confidence > 0.5):
                    count += 1
                    frame = image[startY:endY, startX:endX]
                    cv2.imwrite(base_dir + '/' + destination + '/' + str(i) + '_' + file, frame)

    print("Extracted " + str(count) + " faces from all images")

def frameSplit(source, destination):
    if not os.path.exists(destination):
        print("New directory created")
        os.makedirs(destination)

    # for file in os.listdir(base_dir + source):

    cntImg = 0
    cc = 0
    for file in os.listdir(base_dir + '/' + source):
        cc += 1
        cap = cv2.VideoCapture(base_dir + '/' + source + '/' + file)

        # Check if camera opened successfully
        if (cap.isOpened() == False):
            print("Error opening video stream or file")

        cnt = 0

        # Read until video is completed
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            else:
                cv2.imwrite(destination + '/frame%d.jpg' % cntImg, frame)
                cntImg += 1
                cnt += 3
                cap.set(cv2.CAP_PROP_POS_FRAMES, cnt)

        # When everything done, release the video capture object
        cap.release()
        print(cc, cntImg)

# frameSplit('FaceForensics++/manipulated_sequences/Deepfakes/c23/videos', 'deepfakesSplitted')
# createDataset('deepfakesSplitted', 'deepfakes')

# frameSplit('FaceForensics++/manipulated_sequences/Face2Face/c23/videos', 'face2faceSplitted')
# createDataset('face2faceSplitted', 'face2face')

# frameSplit('FaceForensics++/manipulated_sequences/FaceSwap/c23/videos', 'faceswapSplitted')
# createDataset('faceswapSplitted', 'faceswap')

frameSplit('FaceForensics++/manipulated_sequences/NeuralTextures/c23/videos', 'neuraltexturesSplitted')
createDataset('neuraltexturesSplitted', 'neuraltextures')

frameSplit('FaceForensics++/original_sequences/youtube/c23/videos', 'realSplitted')
createDataset('realSplitted', 'real')



def convertBGR_RGB():
    paths = ['/real', '/deepfakes', '/face2face', '/faceswap', '/neuraltextures']
    cnt = 0
    for e in paths:
        for file in os.listdir(base_dir + e):
            im_cv = cv2.imread(base_dir + e + '/' + file)
            try:
                im_rgb = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)
                Image.fromarray(im_rgb).save(base_dir + e + '/' + file)
                print(base_dir + e + '/' + file)
            except:
                os.remove(base_dir + e + '/' + file)
            cnt += 1
        print(cnt)

convertBGR_RGB()

# dataset mai mare
# model pentru face extraction antrenat de mine (care sa contina si fete fake)
# *dataset impartit in functie de tehnica de falsificare folosita
# *partea vizuala
"""

from VideoProcessing import *


def FaceExtractorwa():
    fe = FaceExtractor('/modeldata/deploy.prototxt', '/modeldata/weights.caffemodel')
    vp = VideoProcessing(fe)

    vp.setPaths(['ceva'])
    vp.setDestinations(['altceva'])
    vp.framesExtracted = 773
    vp.process()

FaceExtractorwa()