from os import listdir
from os.path import splitext
from os.path import exists
import shutil
from PIL import Image
import numpy as np
from skimage.measure import block_reduce

images_dir  = './data/imgs'
masks_dir  = './data/masks'
images_cells_dir  = './data/imgs_cells'
masks_cells_dir  = images_cells_dir # Masks are now original images downsampled
mask_ids = [splitext(file)[0][7:10] for file in listdir(masks_cells_dir) if not file.startswith('.')]

original = True #toggle preprocessing

def downsample(x):
    N = 8
    for r in range(1, x.shape[0],N):
        for c in range(1, x.shape[1],N):
            val = x[r][c]

            for r_w in range(1,N):
                for c_w in range(1,N):
                    x[r-r_w][c-c_w] = val
    return x 

def main():
    # moves and renames images files
    for file in listdir(images_cells_dir):
        id = splitext(file)[0]
        dest = images_dir+'/'+id[1:]+'.tif'
        if not exists(dest):
            if original:
                shutil.copy(images_cells_dir+'/'+file, dest)
            else: 
                im = Image.open(images_cells_dir+'/'+file)
                im.save(dest) 
    # downsamples, moves, and renames image files to create "masks"
    for file in listdir(masks_cells_dir):
        id = splitext(file)[0]
        dest = masks_dir+'/'+id[1:]+'_mask'+'.tif'
        if not exists(dest):
            im = Image.open(masks_cells_dir+'/'+file)
            im_arr = np.asarray(im)
            downsample_arr = downsample(im_arr)
            im_downsampled = Image.fromarray(downsample_arr)
            im_downsampled.save(dest)

if __name__ == "__main__":
    main()