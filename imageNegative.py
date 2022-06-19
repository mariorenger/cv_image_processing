from PIL import Image
import cv2
import sys
import numpy as np

S = 255

def negativeImage(im):
    img = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    B,G,R = cv2.split(img)
    B[:] = [S-x for x in B]     #inverting blue
    G[:] = [S-x for x in G]     #inverting green    
    R[:] = [S-x for x in R]     #inverting red

    #saving image
    my_img = cv2.merge((B, G, R))
    my_img = Image.fromarray(my_img)
    return my_img
