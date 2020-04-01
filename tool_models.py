import cv2
from skimage.filters import threshold_local
from skimage.color import rgb2gray
import numpy as np

class ImageTool:
    def __init__(self):
        self.BLOCK_SIZE = 35
        self.color_data = cv2.imread('fish.jpg')
        self.grey_data = rgb2gray(self.color_data)
        self.grey_data_sm = cv2.resize(self.grey_data, (860, 540))

        self.local_threshold = threshold_local(self.grey_data_sm, self.BLOCK_SIZE)
        self.binary_img = np.array((self.grey_data_sm > self.local_threshold)*255, dtype=np.uint8)
    