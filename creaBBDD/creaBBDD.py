import os
import sys
from shutil import copy, move
import re
import subprocess
from shutil import rmtree
from multiprocessing import Pool

def FesAccio(img):
    #print(img)
    if '-with-mask' not in img:
        subprocess.run(["face-mask", img, "--blue"])
        nname = re.sub('\.jpg$', '', img) + '-with-mask.jpg'
        if(os.path.exists(nname)):
            move(nname, '../allImagesMask/' + nname)
        else:
            os.remove(img)
    else:
        os.remove(img)
        
    return

if __name__ == '__main__':
    #posar totes les fotos en una carpeta
    if "allImagesNoMask" not in os.listdir():
        os.mkdir("allImagesNoMask")
        os.chdir('clip_img')
        dirs = os.listdir()
        for folder in dirs:
            os.chdir(folder)
            sfs = os.listdir()
            for sf in sfs:
                os.chdir(sf)
                imgs = os.listdir()
                for im in imgs:
                    copy(im, "../../../allImagesNoMask/" + im)
                os.chdir('..')
            os.chdir('..')
        print("Fotos copiades!")
    #fer les fotos amb mascareta
    if 'allImagesMask' not in os.listdir():
        os.mkdir("allImagesMask")
        os.chdir('allImagesNoMask')
        photos = os.listdir()

        pool = Pool()
        pool.map(FesAccio, photos)
        print("Fotos amb mascareta creades")