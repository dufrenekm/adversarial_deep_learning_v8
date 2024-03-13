import os
import cv2
import numpy as np
from utils import *


# add some random noise to bounding boxes of all of the images

name='test2'
copy = True
# Go into the dataset directory
os.chdir("../coco126")
# Check if directory already exists
current_files = os.listdir('images')
print(current_files)

if copy:
    if name in current_files:
        print("Directory already exists!!")
        exit()

    # Copy clean data
    os.mkdir('images/'+name)
    os.system(f'cp -r images/train_clean_2017/* images/{name}/')

# Get all images
image_files = os.listdir(f'images/{name}')
images = [img.split('.')[0] for img in image_files] # Strip file type

label_files = os.listdir(f'labels/train_clean_2017')
labels = [img.split('.')[0] for img in label_files] # Strip file type


for img in images:
    # Get the label
    data = np.genfromtxt(f'labels/train_clean_2017/{img}.txt')
    # Load the image
    im_array = cv2.imread(f'images/{name}/{img}.jpg')
    print("Image "+img)
    print("Shape: ", im_array.shape)
    # print(len(data.shape))
    if len(data.shape) == 1:
        num_boxes = 1
    else:
        num_boxes = data.shape[0]
    
    # Get bounding box of image
    for row_index in range(num_boxes):
        im_array = cv2.imread(f'images/{name}/{img}.jpg')
        if len(data.shape) == 1:
            # Only one row
            data_row = data
        else:
            data_row = data[row_index,:]
        # print(data_row)
        
        print(data_row)
        bbox = get_bounding_box(im_array.shape, data_row[1], data_row[2], data_row[3], data_row[4])
        print(bbox)
        # new_image = add_random_noise(np.copy(im_array), 10, x_min, x_max, y_min, y_max)
        # display_images(im_array, im_array, x_min, x_max, y_min, y_max)
        
        
        # Choose random noise or line!
        # image = add_random_noise(np.copy(im_array), 10, bbox)
        image = add_line(im_array, 10, bbox)
        
        
        # image = draw_bounding_box(image, bbox)
        # display_images(im_array, image)
        cv2.imwrite(f'images/{name}/{img}.jpg', image)
        
        # # Get the coordinates in pixels
    #     # 
    # break
    
    
    