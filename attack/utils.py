def get_bounding_box(img_shape, x_center, y_center, height, width):
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
    x_center_pix = x_center * img_shape(0)
    y_center_pix = y_center * img_shape(1)
    width_pix = img_shape(0) * width
    height_pix = img_shape(1) * height
    
    x_min = int(x_center_pix - width_pix/2.0)
    x_max = int(x_center_pix + width_pix/2.0)
    y_min = int(y_center_pix - height_pix/2.0)
    y_max = int(y_center_pix + height_pix/2.0)

    return x_min, x_max, y_min, y_max