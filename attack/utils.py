import numpy as np
import cv2
from random import random, uniform
def get_bounding_box(img_shape, x_center, y_center, width, height):
    """ Converts label dim to pixel coordinates

    Args:
        img_shape (tuple): (width, height)
        x_center (float): _description_
        y_center (float): _description_
        height (float): _description_
        width (float): _description_

    Returns:
        _type_: _description_
    """
    x_center_pix = x_center * img_shape[1]
    y_center_pix = y_center * img_shape[0]
    width_pix = img_shape[1] * width
    height_pix = img_shape[0] * height
    
    x_min = int(x_center_pix - width_pix/2.0)
    x_max = int(x_center_pix + width_pix/2.0)
    y_min = int(y_center_pix - height_pix/2.0)
    y_max = int(y_center_pix + height_pix/2.0)

    return x_min, y_min, x_max, y_max

def add_random_noise(image, noise_amount, bbox):
    noise = np.random.randint(-noise_amount, noise_amount, (bbox[3]-bbox[1], bbox[2]-bbox[0], 3))
    print("Here", noise.shape)
    image_vals = image[bbox[1]:bbox[3], bbox[0]:bbox[2], :]
    print("here2", image_vals.shape)
    modded_vals = np.add(image_vals, noise)
    image[bbox[1]:bbox[3], bbox[0]:bbox[2], :] = modded_vals
    return np.clip(image, 0, 255)

def add_line(image, noise_amount, bbox):
    width = uniform(.1, 0.99)
    y_val = random()
    pix_width = width* (bbox[2]-bbox[0])
    new_bbox_left = int(((bbox[2]-bbox[0])/2+bbox[0]) - pix_width/2)
    new_bbox_right = int(((bbox[2]-bbox[0])/2+bbox[0]) + pix_width/2)
    y_val_pix = int(y_val*(bbox[3]-bbox[1]))+bbox[1]
    image[y_val_pix, new_bbox_left:new_bbox_right, :] = np.zeros((1,new_bbox_right-new_bbox_left,3))
    # image_vals = image[bbox[1]:bbox[3], bbox[0]:bbox[2], :]
    
    # noise = np.random.randint(-noise_amount, noise_amount, (bbox[3]-bbox[1], bbox[2]-bbox[0], 3))
    # print("Here", noise.shape)
    # image_vals = image[bbox[1]:bbox[3], bbox[0]:bbox[2], :]
    # print("here2", image_vals.shape)
    # modded_vals = np.add(image_vals, noise)
    # image[bbox[1]:bbox[3], bbox[0]:bbox[2], :] = modded_vals
    return np.clip(image, 0, 255)

def display_images(old_img, new_img):
    image = np.hstack((old_img, new_img))
    # image = cv2.rectangle(image, (y_min, x_min), (y_max, x_max), [0,0,255], 2) 
    cv2.imshow("Window", image)
    cv2.waitKey(0)
    
def draw_bounding_box(image, bbox, color=(0, 255, 0), thickness=2):
    """
    Draw a bounding box on the image.

    Parameters:
        image (numpy.ndarray): The input image.
        bbox (tuple): A tuple containing (x_min, y_min, x_max, y_max) coordinates of the bounding box.
        color (tuple): The color of the bounding box in BGR format. Default is green.
        thickness (int): The thickness of the bounding box lines. Default is 2.
    
    Returns:
        numpy.ndarray: The image with the bounding box drawn.
    """
    x_min, y_min, x_max, y_max = bbox
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, thickness)
    return image