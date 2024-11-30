# --------------------------------------------------------------------------------
# This module is meant to be the center point of the task of creating the dataset.
# Here, the input videos will be split frame by frame and reconverted to RGB format.
# The frames will be forwarded one by one to the FaceExtractor module for inference.
# --------------------------------------------------------------------------------

from FaceExtractor import *
from PIL import Image

class VideoProcessing:

    def __init__(self, face_extractor):
        self.framesExtracted = 0 # 0 for empty folder
        self.paths = []
        self.destinations = []
        self.FaceExtractor = face_extractor

    def setPaths(self, path):
        self.paths = path

    def setDestinations(self, destinations):
        self.destinations = destinations

    def process(self):
        if len(self.paths) != len(self.destinations):
            raise Exception("The length of the path array and destination array must be equal")
        pd_length = len(self.paths)

        for i in range(pd_length):
            path = self.paths[i]
            destination = self.destinations[i]

            if not os.path.exists(destination):
                os.makedirs(destination)
                print("New directory created")

            frameNumberInDirectory = 0
            videoNumberInDirectory = 0
            for file in os.listdir(base_dir + '/' + path):
                videoNumberInDirectory += 1
                cap = cv2.VideoCapture(base_dir + '/' + path + '/' + file)

                # Check if camera opened successfully
                if (cap.isOpened() == False):
                    print("Error opening video stream or file")

                skip = 0

                # Read until video is completed
                while (cap.isOpened()):
                    ret, frame = cap.read()
                    if ret == False:
                        break
                    else:
                        im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        extract = self.FaceExtractor.extractFaces(im_rgb)
                        if extract is not None:
                            self.framesExtracted += 1
                            frameNumberInDirectory += 1
                            # This is added for having the frames ordered alphabetically and lexicographically
                            saveStringLexi = self.numberToString(self.framesExtracted)
                            # save RGB
                            try:
                                Image.fromarray(extract).save(destination + '/frame' + saveStringLexi + '.jpg')
                            except:
                                self.framesExtracted -= 1
                                frameNumberInDirectory -= 1
                        skip += 7
                        cap.set(cv2.CAP_PROP_POS_FRAMES, skip)

                # When everything done, release the video capture object
                cap.release()
                print(videoNumberInDirectory, frameNumberInDirectory)

            self.framesExtracted += frameNumberInDirectory

    def numberToString(self, number):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        result = ""
        for i in range(5):
            order = number % 26
            number //= 26
            result = alphabet[order] + result

        return result