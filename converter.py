import numpy as np
import cv2


#Read Image


#Show
def show(window_name, image):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, image)
    cv2.resizeWindow(window_name, 256, 256)


def texturate(scale, alternation, targetfile='textures/block/stone.png'):

    img = cv2.imread(targetfile)
    img2 = np.zeros((16*scale,16*scale,3), np.uint8)

    for y in range(16):
    
        for x in range(16):
    
            for y2 in range(scale):
                for x2 in range(scale):
                    rnd = np.random.randint(low = -alternation, high = alternation)
                    for c in range(3):
                        img2[x*scale+x2, y*scale+y2, c] = img[x,y,c] + rnd




#Processing

scale = 4

#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


show('1', img)

alt = 5



for i in range(20):
    texturate(4, i)



        



show('2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()