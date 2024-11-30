import unittest

from VideoProcessing import *

class TestDatasetCreator(unittest.TestCase):

    def test_FaceExtractor_FaceFrame(self):
        fe = FaceExtractor('/modeldata/deploy.prototxt', '/modeldata/weights.caffemodel')
        image = cv2.imread('TestDir/sample_1.jpg')
        result = fe.extractFaces(image)

        self.assertFalse(result is None)

    def test_FaceExtractor_NoFaceFrame(self):
        fe = FaceExtractor('/modeldata/deploy.prototxt', '/modeldata/weights.caffemodel')
        image = cv2.imread('TestDir/sample_2.png')
        result = fe.extractFaces(image)

        self.assertTrue(result is None)

    def test_VideoProcessing_WrongPaths(self):
        fe = FaceExtractor('/modeldata/deploy.prototxt', '/modeldata/weights.caffemodel')
        vp = VideoProcessing(fe)
        vp.setPaths(['TestDir/data'])
        vp.setDestinations(['TestDir/result', 'nd'])

        self.assertRaises(Exception, vp.process)

    def test_VideoProcessing(self):
        fe = FaceExtractor('/modeldata/deploy.prototxt', '/modeldata/weights.caffemodel')
        vp = VideoProcessing(fe)
        vp.setPaths(['TestDir/data'])
        vp.setDestinations(['TestDir/result'])
        vp.process()

        self.assertTrue(vp.framesExtracted > 0)
