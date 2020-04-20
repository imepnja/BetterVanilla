import numpy as np
import cv2
import os 
from image_obj import Image


#Read Image

####################################################################################
#Show Image
####################################################################################

def Show(window_name, image):
    ym =  256* image.shape[0]/image.shape[1]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, image)
    x = cv2.getWindowImageRect(window_name)[2]*4
    y = cv2.getWindowImageRect(window_name)[3]*4
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
        img = images[i].img
        image_x = img.shape[0]
        image_y = img.shape[1]
        image_c = img.shape[2]
        print(img.shape)
        img2 = np.zeros((image_x*scale,image_y*scale,image_c), np.uint8)

        for y in range(image_y):
            for x in range(image_x):
                for y2 in range(scale):
                    for x2 in range(scale):
                        if image_c == 4:
                            if img[x,y, 3] != 0: 
                                rnd = np.random.randint(low = -alternation, high = alternation)
                                for c in range(3):
                                    if 0 <= (img[x,y,c] + rnd) <= 255:
                                        img2[x*scale+x2, y*scale+y2, c] = img[x,y,c] + rnd
                                    else:
                                        img2[x*scale+x2, y*scale+y2, c] = img[x,y,c]
                        else:
                            rnd = np.random.randint(low = -alternation, high = alternation)
                            for c in range(3):
                                if 0 <= (img[x,y,c] + rnd) <= 255:
                                    img2[x*scale+x2, y*scale+y2, c] = img[x,y,c] + rnd
                                else:
                                    img2[x*scale+x2, y*scale+y2, c] = img[x,y,c]
        img2_obj = Image(img2, images[i].filename, images[i].filepath)
        newimages.append(img2_obj)
    return newimages    




####################################################################################
#Save Image Files
####################################################################################

def Load(root):
    files = []
    images = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(root):
        for file in f:
            if not '.mcmeta' in file:
                files.append(os.path.join(r, file))



    for i in range(len(files)):
        images.append(Image(files[i]))
        print(str(i) + files[i])
    return images
    

####################################################################################
#Save Image Files
####################################################################################

def Save(images=[]):
    rootdir = os.getcwd()
    for i in range(len(images)):
        print(str(i) + images[i].filename)
        try:
            os.chdir('new_' + images[i].filepath)
        except:
            os.makedirs('new_' + images[i].filepath)
            os.chdir('new_' + images[i].filepath)
        
        cv2.imwrite(images[i].filename, images[i].img)
        os.chdir(rootdir)
        # for x in range(len(images[i].filepath.split('/'))):
        #     os.chdir('..')


scale = 2
alt = 10
new_images = []
files = Load('textures')




new_images = Texturate(scale, alt, files)

# for i in new_images:
#     Show(i.filename, i.img)

Save(new_images)

#for f in files:
 #   new_images.append(Texturate(scale, alt, f))
    



###Saving
# images = Texturate(scale, alt, images)
# Show(images[0].filename, images[0].img)
# Show(images[1].filename, images[1].img)
# Save(images = [stone, oak_planks])
# 
cv2.waitKey(0)
cv2.destroyAllWindows()