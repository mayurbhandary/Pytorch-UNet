from os import listdir
from os.path import splitext
from os.path import exists
import shutil
from PIL import Image
import numpy as np

images_dir  = './data/imgs'
masks_dir  = './data/masks'
images_cells_dir  = './data/imgs_cells'
masks_cells_dir  = './data/masks_cells'
mask_ids = [splitext(file)[0][7:10] for file in listdir(masks_cells_dir) if not file.startswith('.')]

original = True #toggle preprocessing

# moves and renames mask and image files
for file in listdir(images_cells_dir):
    id = splitext(file)[0]
    dest = images_dir+'/'+id[1:]+'.tif'
    if not exists(dest) and id[1:] in mask_ids:
        if original:
            shutil.copy(images_cells_dir+'/'+file, dest)
        else: 
            im = Image.open(images_cells_dir+'/'+file)
            im.save(dest) 

for file in listdir(masks_cells_dir):
    id = splitext(file)[0]
    dest = masks_dir+'/'+id[7:10]+'_mask'+'.tif'
    if not exists(dest):
        if original:
            shutil.copy(masks_cells_dir+'/'+file, dest)
        else:
            im = Image.open(masks_cells_dir+'/'+file)
            im = im.convert('L')
            im.save(dest)



