from PIL import Image
from tkinter import filedialog
import matplotlib.pyplot as plt

def resizeImage(im, filtr, width, height, skipdialog=False):
    image = im
    if filtr == "Nearest Neighbour":
        image = im.resize((width, height), Image.NEAREST)      # nearest neighbour
    elif filtr == "Bilinear":
        image = im.resize((width, height), Image.BILINEAR)     # bilinear interpolation
    elif filtr == "Bicubic":
        image = im.resize((width, height), Image.BICUBIC)      # bicubic interpolation
    elif filtr == "Anti-Alias":
        image = im.resize((width, height), Image.ANTIALIAS)    # antialiasing

    return image
def plot(image , new):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 4),
                                    sharex=False, sharey=False)
    ax[0].set_title('old')
    ax[1].set_title('new')
    
    ax[0].imshow(image)
    ax[1].imshow(new)
    plt.show()
