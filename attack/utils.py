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


def add_transparent_image(background, foreground, x_offset=None, y_offset=None):
    bg_h, bg_w, bg_channels = background.shape
    fg_h, fg_w, fg_channels = foreground.shape

    assert bg_channels == 3, f'background image should have exactly 3 channels (RGB). found:{bg_channels}'
    assert fg_channels == 4, f'foreground image should have exactly 4 channels (RGBA). found:{fg_channels}'

    # center by default
    if x_offset is None: x_offset = (bg_w - fg_w) // 2
    if y_offset is None: y_offset = (bg_h - fg_h) // 2

    w = min(fg_w, bg_w, fg_w + x_offset, bg_w - x_offset)
    h = min(fg_h, bg_h, fg_h + y_offset, bg_h - y_offset)

    if w < 1 or h < 1: return

    # clip foreground and background images to the overlapping regions
    bg_x = max(0, x_offset)
    bg_y = max(0, y_offset)
    fg_x = max(0, x_offset * -1)
    fg_y = max(0, y_offset * -1)
    foreground = foreground[fg_y:fg_y + h, fg_x:fg_x + w]
    background_subsection = background[bg_y:bg_y + h, bg_x:bg_x + w]

    # separate alpha and color channels from the foreground image
    foreground_colors = foreground[:, :, :3]
    alpha_channel = foreground[:, :, 3] / 255  # 0-255 => 0.0-1.0

    # construct an alpha_mask that matches the image shape
    alpha_mask = np.dstack((alpha_channel, alpha_channel, alpha_channel))

    # combine the background with the overlay image weighted by alpha
    composite = background_subsection * (1 - alpha_mask) + foreground_colors * alpha_mask

    # overwrite the section of the background image that has been updated
    background[bg_y:bg_y + h, bg_x:bg_x + w] = composite
    return background