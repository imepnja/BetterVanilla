import numpy as np
import cv2

class Image():
    def __init__(self, scale=1, alternation=1, targetfile='', fileName = 'unknown_filename', img = np.zeros((16,16,3), np.uint8)):
        self.img = img
        self.fileName = fileName
        self.targetfile = targetfile
        self.scale = scale
        self.alternation = alternation
        # 

        if targetfile != '':
            self.img = cv2.imread(targetfile)
            filename = targetfile.split('/')[-1]
            

    def texturate(self):

        scale = self.scale
        alternation = self.alternation
        img2 = np.zeros((16*scale,16*scale,3), np.uint8)

        for y in range(16):
            for x in range(16):
                for y2 in range(scale):
                    for x2 in range(scale):
                        rnd = np.random.randint(low = -alternation, high = alternation)
                        for c in range(3):
                            img2[x*scale+x2, y*scale+y2, c] = self.img[x,y,c] + rnd

        self.img = img2