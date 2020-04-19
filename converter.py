import numpy as np
import cv2


#Read Image
img = cv2.imread('texture_pack/assets/minecraft/textures/block/stone.png')


def show(window_name):
    #Show
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, img)
    cv2.resizeWindow(window_name, 256, 256)

    



#Processing

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pxs = []

#for i in range(16*16):
 #   pxs [i]
show('1')
print(img[5,5])

""" rnd = np.random.randint(low = -100, high = 100)
img[5,5,0] = img[5,5,0] + rnd
img[5,5,1] = img[5,5,1] + rnd
img[5,5,2] = img[5,5,2] + rnd """
rnd = np.random.randint(low = -100, high = 100)
img[5,5,0] = 0
img[5,5,1] = 0
img[5,5,2] = 0

print(img[5,5])
show('2')

cv2.waitKey(0)
cv2.destroyAllWindows()