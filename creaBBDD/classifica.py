import os
from shutil import move

os.chdir("allImagesNoMask")
os.mkdir("train")
images = os.listdir()
for i in range(11371):
    img = images[i]
    move(img, 'train/' + img)

os.mkdir("test")
images = os.listdir()
for i in range(11371):
    img = images[i]
    move(img, 'test/' + img)


os.mkdir("validation")
images = os.listdir()
for img in images:
    if img is not "test" and img is not "train":
        move(img, 'validation/' + img)


os.chdir("..")


###########################################################################
###########################################################################

# os.chdir("allImagesMask")
# os.mkdir("train")
# images = os.listdir()
# for i in range(11371):
#     img = images[i]
#     move(img, 'train/' + img)

# os.mkdir("test")
# images = os.listdir()
# for i in range(11371):
#     img = images[i]
#     move(img, 'test/' + img)


# os.mkdir("validation")
# images = os.listdir()
# for img in images:
#     if img is not "test" and img is not "train":
#         move(img, 'validation/' + img)