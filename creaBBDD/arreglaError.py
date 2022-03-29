import os
import re
import time
import sys

os.chdir("allImagesMask")
imagesMask = os.listdir()
os.chdir("../allImagesNoMask")
images = os.listdir()
for img in images:
    nname = re.sub('\.jpg$', '', img) + '-with-mask.jpg'
    if nname not in imagesMask:
        print("error trobat")
        for l in ("..."):
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.2)
        
        os.remove(img)
        print("error eliminat")