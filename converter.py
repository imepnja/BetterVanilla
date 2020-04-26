import numpy as np
import cv2
import os 
import sys
from image_obj import Image
from tqdm import tqdm
from tqdm import trange
import datetime






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

def Texturate(scale, alternation, image):
    filename = image.filename

    img = image.img
    image_x = img.shape[0]
    image_y = img.shape[1]
    image_c = img.shape[2]

    img2 = np.zeros((image_x*scale,image_y*scale,image_c), np.uint8)

    if image.lower_alt != '':
        alternation = image.lower_alt

    
    for y in range(image_y):#Img Y cordinate
        for x in range(image_x):#Img X cordinate
            for y2 in range(scale):#New (high res) Img Y cordinate
                for x2 in range(scale): #New (high res) Img X cordinate
                    
                    ##Png (alpha chanel)
                    if image_c == 4:

                        if img[x,y, 3] != 0: #check for alpha chanel
                            rnd = np.random.randint(low = -alternation, high = alternation) 

                            for c in range(3): #change Color by random
                                if int(img[x,y,c] + rnd) > 255 or int(img[x,y,c] + rnd) < 0:
                                    rnd = -rnd
                                # if 0 <= (img[x,y,c] + rnd) <= 255: # limit to 
                                img2[x*scale+x2, y*scale+y2, c] = img[x,y,c] + rnd

                            img2[x*scale+x2, y*scale+y2, 3] = img[x,y,3]
                    
                    ##For jpgs
                    else:
                        
                        rnd = np.random.randint(low = -alternation, high = alternation)

                        for c in range(3): #change Color by random
                                if int(img[x,y,c] + rnd) > 255 or int(img[x,y,c] + rnd) < 0:
                                    rnd = -rnd
                                # if 0 <= (img[x,y,c] + rnd) <= 255: # limit to 
                                img2[x*scale+x2, y*scale+y2, c] = img[x,y,c] + rnd

    new_image = Image(img2, '',  image.filename, image.filepath)
    return new_image
   




####################################################################################
#Save Image Files
####################################################################################

def Load(root, blacklist, lower_textures, lower_alt):
    images = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(root):
        for idx, file in enumerate(f):
            if not '.mcmeta' in file:
                blacklisted = False
                is_lower_texture = False
                for b in blacklist:
                    if  b in file:
                        blacklisted = True
                for lt in lower_textures:
                    if  lt in file:
                        is_lower_texture = True
                if not blacklisted:
                    if is_lower_texture:
                        images.append(Image(os.path.join(r, file).replace('\\', '/'), lower_alt))
                    else:
                        images.append(Image(os.path.join(r, file).replace('\\', '/')))
                    
                    print(str(idx) + ' ' + os.path.join(r, file).replace('\\', '/'))
                    
    return images
    

####################################################################################
#Save Image Files
####################################################################################

def Save(images=[]):
    rootdir = os.getcwd()
    for i in range(len(images)):
        # print(str(i) + images[i].filename)
        try:
            os.chdir('new_' + images[i].filepath)
        except:
            os.makedirs('new_' + images[i].filepath)
            os.chdir('new_' + images[i].filepath)
        
        cv2.imwrite(images[i].filename, images[i].img, [cv2.IMWRITE_PNG_COMPRESSION, 6])
        os.chdir(rootdir)
        # for x in range(len(images[i].filepath.split('/'))):
        #     os.chdir('..')





############################
scale = 2
alt = 6
lower_alt = 2
target_folder = 'test'

blacklist = ['concrete.png', 'debug', '.ini', 'water', 'sun', 'moon']
lower_textures = ['quartz', 'terracotta',]
############################



#Load all files
files = Load(target_folder, blacklist, lower_textures, lower_alt)

print("Loaded %s Files" % int(len(files)))
print("Converting...")


#Texturate all files
start_time = datetime.datetime.now()

new_images = []


with trange(len(files)) as t:
    for i in t:
        t.set_description(str(i))
        _reserved_space = 30 
        _len = len(files[i].filename)
        t.set_postfix(file=files[i].filename + ("_" * (_reserved_space - _len)), refresh=False)
        new_images.append(Texturate(scale, alt, files[i]))
        t.update()


stop_time = datetime.datetime.now()


print("\nProcessed %s Files in %s " % (str(len(files)), str(stop_time-start_time)))
print("\nSaving...")
Save(new_images)
print("Saved")

cv2.waitKey(0)
cv2.destroyAllWindows()