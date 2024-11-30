import unittest

from InferenceModule import *


class TestInferenceModule(unittest.TestCase):

    def test_InferenceModule_NoVideo(self):
        im = InferenceModule()
        res = im.video_inference("testing/test_dir/nothing")

        self.assertEquals(res, [-1])

    def test_InferenceModule_RealVideo(self):
        im = InferenceModule()
        res = im.video_inference("testing/test_dir/short_real.mov")

        self.assertTrue(res[5] > 0.5)

    def test_InferenceModule_FakeVideo(self):
        im = InferenceModule()
        res = im.video_inference("testing/test_dir/short_fake.mp4")

        self.assertTrue(res[5] < 0.5)

    def test_InferenceModule_NoFrame(self):
        im = InferenceModule()
        res = im.single_frame_inference("testing/test_dir/nothing")

        self.assertEquals(res, None)

    def test_InferenceModule_FakeFrame(self):
        im = InferenceModule()
        res = im.single_frame_inference("testing/test_dir/fake.jpg")

        self.assertEquals(res, 0)

    def test_InferenceModule_RealFrame(self):
        im = InferenceModule()
        res = im.single_frame_inference("testing/test_dir/real.jpg")

        self.assertEquals(res, 1)
