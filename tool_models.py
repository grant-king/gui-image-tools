import cv2
from skimage.filters import threshold_local
from skimage.color import rgb2gray
import numpy as np
import os

class ImageTool:
    def __init__(self):
        os.chdir('C:/Users/G/Pictures/image_processing')
        contents = os.listdir()
        self.all_files = [item for item in contents if '.jpg' in item or '.png' in item]#[25:]
        self.current_image_idx = 0
        self.current_image = ImageData(self.all_files[self.current_image_idx])

    def save_bw_image(self):
        filename = self.current_image.filename
        img_data = self.current_image.binary_img
        cv2.imwrite(f'bw_{filename}', img_data)

    def get_current_image(self):
        self.current_image = ImageData(self.all_files[self.current_image_idx])
        return self.current_image

    def get_current_display_size(self):
        return self.current_image.get_display_size()

    def increase_current_image(self):
        if self.current_image_idx < len(self.all_files) - 1:
            self.current_image_idx += 1
        else:
            self.current_image_idx = 0
        self.current_image = ImageData(self.all_files[self.current_image_idx])

    def decrease_current_image(self):
        if self.current_image_idx > 0:
            self.current_image_idx -= 1
        else:
            self.current_image_idx = len(self.all_files) -  1
        self.current_image = ImageData(self.all_files[self.current_image_idx])

class ImageData:
    def __init__(self, filename):
        self.MAX_DISPLAY_SIZE = [1080, 1920]
        self.filename = filename
        self.color_img = cv2.imread(filename)
        self.dispaly_size = self.get_display_size()

    @property
    def grey_img(self):
        return rgb2gray(self.color_img)

    @property
    def binary_img(self):
        return self.get_bw_data()

    def get_bw_data(self):
        BLOCK_SIZE = 35
        self.local_threshold = threshold_local(self.grey_img, BLOCK_SIZE)
        return np.array((self.grey_img > self.local_threshold)*255, dtype=np.uint8)

    def get_display_size(self):
        size = self.color_img.shape
        resize_ratio = min(self.MAX_DISPLAY_SIZE[0] / size[0], self.MAX_DISPLAY_SIZE[1] / size[1])
        return [size[0]*resize_ratio, size[1]*resize_ratio]
