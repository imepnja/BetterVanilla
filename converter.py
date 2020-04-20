import numpy as np
import cv2
import os 
from image_obj import Image


#Read Image

####################################################################################
#Show Image
####################################################################################

def show(window_name, image):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, image)
    cv2.resizeWindow(window_name, 256, 256)




####################################################################################
#Texturate randomly
####################################################################################

def texturate(scale, alternation, targetfile='textures/block/stone.png'):

    filename = targetfile.split('/')[2]
    img = cv2.imread(targetfile)
    img2 = np.zeros((16*scale,16*scale,3), np.uint8)

    for y in range(16):
        for x in range(16):
            for y2 in range(scale):
                for x2 in range(scale):
                    rnd = np.random.randint(low = -alternation, high = alternation)
                    for c in range(3):
                        img2[x*scale+x2, y*scale+y2, c] = img[x,y,c] + rnd

    return img2




####################################################################################
#Save Image Files
####################################################################################
def Save(images=[]):
    for i in images:
        cv2.imwrite()
    

# newTextures = []

# for i in range(5):
#     newTextures.append(texturate(4, i + 3))


Stone = Image(4,10,'textures/block/stone.png')
Stone.texturate()

show('s', Stone.img)

cv2.waitKey(0)
cv2.destroyAllWindows()