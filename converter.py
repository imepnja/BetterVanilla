import numpy as np
import cv2
import os 
from image_obj import Image


#Read Image

####################################################################################
#Show Image
####################################################################################

def Show(window_name, image):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, image)
    cv2.resizeWindow(window_name, 256, 256)




####################################################################################
#Texturate randomly
####################################################################################

def TexturateSingle(scale, alternation, targetfile='textures/block/stone.png'):

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

def Texturate(scale, alternation, images=[]):
    newimages = []

    for i in range(len(images)):
        filename = images[i].filename
        img2 = np.zeros((16*scale,16*scale,3), np.uint8)
        img = images[i].img
    
        for y in range(16):
            for x in range(16):
                for y2 in range(scale):
                    for x2 in range(scale):
                        rnd = np.random.randint(low = -alternation, high = alternation)
                        for c in range(3):
                            img2[x*scale+x2, y*scale+y2, c] = img[x,y,c] + rnd
        img2obj = Image(img2, images[i].filename)
        newimages.append(img2obj)
    return newimages




####################################################################################
#Save Image Files
####################################################################################

def Load()


####################################################################################
#Save Image Files
####################################################################################

def Save(images=[]):
    print(len(images))
    for i in range(len(images)):
        print(i)
        print(images[i].filename)
        try:
            os.chdir('new_' + images[i].filepath)
        except:
            os.makedirs('new_' + images[i].filepath)
            os.chdir('new_' + images[i].filepath)
        
        cv2.imwrite(images[i].filename, images[i].img)
        for x in range(len(images[i].filepath.split('/'))):
            os.chdir('..')
        print(os.getcwd())



scale = 2
alt = 10
images = []

stone = Image('textures/block/stone.png')
oak_planks = Image('textures/block/oak_planks.png')

images.extend([stone, oak_planks])


#images = [stone, oak_planks]


###Saving
images = Texturate(scale, alt, images)
Show(images[0].filename, images[0].img)
Show(images[1].filename, images[1].img)
Save(images = [stone, oak_planks])

cv2.waitKey(0)
cv2.destroyAllWindows()