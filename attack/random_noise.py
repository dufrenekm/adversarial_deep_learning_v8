import os
import cv2
import numpy as np
from utils import *
from random import uniform, randint
from time import sleep


# add some random noise to bounding boxes of all of the images

name='test7_copy'
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

stop_img = cv2.imread('/home/kyle/adversarial_deep_learning_v8/attack/unnamed.png', cv2.IMREAD_UNCHANGED)


for img in images:
    # Get the label
    data = np.genfromtxt(f'labels/train_clean_2017/{img}.txt')
    # Load the image
    sleep(.001)
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
        
        
        # Get the size of the bounding box and we will create a patch of a random size within it
        width_pix = bbox[2]-bbox[0]
        height_pix = bbox[3]-bbox[1]
        # Rescale size 
        scale = min(width_pix,height_pix)
        # Randomize
        rand_scale = int(uniform(.3, 1.0)*scale)
        
        new_stop_img = cv2.resize(stop_img, (rand_scale,rand_scale))  
        # Adjust transparency to random
        new_stop_img[:,:,3] = new_stop_img[:,:,3]/randint(2, 5) 
        
        # Calculate x,y positions 
        # X possible range = 
        x_shift_max = (width_pix - rand_scale)//2
        y_shift_max = (height_pix - rand_scale)//2
        x_shift = randint(-x_shift_max, x_shift_max)
        y_shift = randint(-y_shift_max, y_shift_max)
        x_pos = int((bbox[2]-bbox[0])/2+bbox[0]-new_stop_img.shape[0]/2) + x_shift
        y_pos = int((bbox[3]-bbox[1])/2+bbox[1]-new_stop_img.shape[1]/2) + y_shift
        # Choose random noise or line!
        # image = add_random_noise(np.copy(im_array), 10, bbox)
        # image = add_line(im_array, 10, bbox)o
        # new_stop_img = cv2.resize(stop_img, (100,100))
        # new_stop_img[:,:,3] = new_stop_img[:,:,3]/10
        # exit()
        # new_stop_img = cv2.cvtColor(new_stop_img, cv2.COLOR_BGR2BGRA)
        # height_max, width_max = im_array.shape[:2]
        # h, w = new_stop_img.shape[:2]
        # print("Size")
        # print(h,w)
        
        # diff_vert = height_max - h
        # pad_top = diff_vert//2
        # pad_bottom = diff_vert - pad_top
        # diff_hori = width_max - w
        # pad_left = diff_hori//2
        # pad_right = diff_hori - pad_left
        # stop_image_padded = cv2.copyMakeBorder(np.copy(new_stop_img), pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_CONSTANT, value=[0,0,0,255])
        new_img = add_transparent_image(np.copy(im_array), new_stop_img, x_pos,y_pos)
        
        
        # alpha_image = np.copy(im_array)
        # alpha_image = cv2.cvtColor(alpha_image, cv2.COLOR_BGR2BGRA)
        # added_image = cv2.addWeighted(alpha_image,0.4,stop_image_padded,0.1,0)
        # image = draw_bounding_box(image, bbox)
        # display_images(im_array, new_img)
        cv2.imwrite(f'images/{name}/{img}.jpg', new_img)
        # exit()
        
        # # Get the coordinates in pixels
    #     # 
    # break
    
    
    