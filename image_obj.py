import numpy as np
import cv2

class Image():
    def __init__(self, targetfile, filename = 'unknown_filename'):
        self.filename = filename
        self.targetfile = targetfile
        

        if isinstance(targetfile, str):
            self.img = cv2.imread(targetfile)
            self.filename = targetfile.split('/')[-1]
            self.filepath = targetfile.rsplit('/', 1)[0]
        else:
            self.img = targetfile

            
    def show(self):
        window_name = self.filename
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, self.img)
        cv2.resizeWindow(window_name, 256, 256)    

    