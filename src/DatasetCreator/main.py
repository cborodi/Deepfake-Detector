# --------------------------------------------------------------------------------
# This is the starting point of the program. FaceExtractor and VideoProcessing is
# initialized here and the source and destination paths are set.
# --------------------------------------------------------------------------------

from VideoProcessing import *


def start():
    fe = FaceExtractor('/modeldata/deploy.prototxt', '/modeldata/weights.caffemodel')
    vp = VideoProcessing(fe)
    vp.setPaths(['FaceForensics++/manipulated_sequences/Deepfakes/c23/videos',
                 'FaceForensics++/manipulated_sequences/Deepfakes_Validation',
                 'FaceForensics++/manipulated_sequences/Deepfakes_Test',
                 'FaceForensics++/manipulated_sequences/Face2Face/c23/videos',
                 'FaceForensics++/manipulated_sequences/Face2Face_Validation',
                 'FaceForensics++/manipulated_sequences/Face2Face_Test',
                 'FaceForensics++/manipulated_sequences/FaceSwap/c23/videos',
                 'FaceForensics++/manipulated_sequences/FaceSwap_Validation',
                 'FaceForensics++/manipulated_sequences/FaceSwap_Test',
                 'FaceForensics++/manipulated_sequences/NeuralTextures/c23/videos',
                 'FaceForensics++/manipulated_sequences/NeuralTextures_Validation',
                 'FaceForensics++/manipulated_sequences/NeuralTextures_Test',
                 'FaceForensics++/original_sequences/youtube/c23/videos',
                 'FaceForensics++/original_sequences/youtube/c23/Real_Validation',
                 'FaceForensics++/original_sequences/youtube/c23/Real_Test'])
    vp.setDestinations(['SampleDatasetFaceForensicsWide++/train/fake', 'SampleDatasetFaceForensicsWide++/validation/fake', 'SampleDatasetFaceForensicsWide++/test/fake',
                        'SampleDatasetFaceForensicsWide++/train/fake', 'SampleDatasetFaceForensicsWide++/validation/fake', 'SampleDatasetFaceForensicsWide++/test/fake',
                        'SampleDatasetFaceForensicsWide++/train/fake', 'SampleDatasetFaceForensicsWide++/validation/fake', 'SampleDatasetFaceForensicsWide++/test/fake',
                        'SampleDatasetFaceForensicsWide++/train/fake', 'SampleDatasetFaceForensicsWide++/validation/fake', 'SampleDatasetFaceForensicsWide++/test/fake',
                        'SampleDatasetFaceForensicsWide++/train/real', 'SampleDatasetFaceForensicsWide++/validation/real', 'SampleDatasetFaceForensicsWide++/test/real'])
    vp.process()


if __name__ == '__main__':
    start()
