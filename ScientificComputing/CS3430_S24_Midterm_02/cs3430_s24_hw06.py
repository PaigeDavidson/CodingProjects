#!/usr/bin/python

#######################################################
# module: cs3430_s24_hw06.py
# bugs to vladimir kulyukin in canvas.
########################################################

### I used math.sqrt, math.atan2, math.floor, and math.ceil in my solution,
### hence the first import.
import math 
from PIL import Image

def lumin(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    """
    Convert rgb pixel to grayscale value.
    """
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

### You can use this function to iterate through image
### pixel by pixel to make sure that you are iterating
### through legal pixels in a PIL image. we are ignoring
### the border and columns.
def is_in_pil_range(pil_img, cr):
    """
    Check if 2-tuple cr references to a legal pixel in a PIl image pil_img
    """
    ncols, nrows = pil_img.size
    c, r = cr
    return c > 0 and c < ncols-1 and r > 0 and r < nrows-1

### a debugging/exploration utility
def display_pil_img_row(pil_img, r):
    """
    Prints pixel values in row r in a PIL image pil_img.
    Useful for debugging.
    """
    ncols, _ = pil_img.size
    for c in range(ncols):
        print(pil_img.getpixel((c, r)))

### a debugging/exploration utility
def display_pil_img_col(pil_img, c):
    """
    Prints pixel values in column c in a PIL image pil_img.
    Useful for debugging.
    """
    _, nrows = pil_img.size
    for r in range(nrows):
        print(pil_img.getpixel((c, r)))

## Remember: in PIL images, c = x, r = y, i.e., columns
## are the x-axis and rows are the y axis; the top left
## corner is [0][0].
def pil_pix_dxdy(pil_img, cr, default_delta):
    """
    Returns dx, dy values for pixel (c, r) in PIL image pil_img.
    If the luminosity values of the horizontal neighbors are the same,
    dx = default_delta.
    If the luminosity values of the vertical neighbors are the same,
    dy = default_delta.
    """
    assert is_in_pil_range(pil_img, cr)

    # cr[0] is the pixel’s column and cr[1] is the pixel’s row
    
    # horizontal change
    # the difference between the luminosities of the pixel’s upper and lower neighbors
    dx = lumin(pil_img.getpixel((cr[0] + 1, cr[1]))) - lumin(pil_img.getpixel((cr[0] - 1, cr[1])))
    if dx == 0:
        dx = default_delta

    # vertical change
    # the difference between the luminosities of the pixel’s right and left neighbors
    dy = lumin(pil_img.getpixel((cr[0], cr[1] - 1))) - lumin(pil_img.getpixel((cr[0], cr[1] + 1)))
    if dy == 0:
        dy = default_delta
    return dx, dy

def grd_magn(dx, dy):
    """
    Gradient magnitude given dx and dy.
    """
    # gradientMag = sqrt(dy^2 + dx^2)
    mag = math.sqrt(dy**2 + dx**2)
    return mag

def grd_deg_theta(dx, dy):
    """
    Gradient orientation (in degrees) given dx and dy.
    """
    # orientation = arctan(dy/dx)
    orientation = math.atan2(dy, dx)
    degrees = math.degrees(orientation)
    rounded = round(degrees)
    # make sure there is no divide by zero error
    if rounded == 0:
        return 1
    return rounded

def dex_pil(pil_img, default_delta=1.0, magn_thresh=20):
    """
    - detects edge pixels in a PIL image pil_img.
    - returns a new binary PIL image where the pixel
    value 255 means that it's a edge pixel and 0 means
    that it's not an edge pixel.
    - default_delta is used in calls to pil_pix_dxdy
    - magn_thresh is a gradient magnitude threshold, i.e.,
    if the computed value is >= magn_thresh, the pixel
    is an edge pixel; otherwise, it's not.
    """
    output_img = Image.new('L', pil_img.size)
    num_cols, num_rows = pil_img.size

    for i in range(1, num_cols - 1):
        for j in range(1, num_rows - 1):
            # Grayscale RGB pixels with luminosity to convert each RGB pixel to grayscale pixel
            lumin(pil_img.getpixel((i, j)))
            # Compute Dy and Dx at each grayscaled pixel
            dx, dy = pil_pix_dxdy(pil_img, (i, j), default_delta)
            # Compute gradient's magnitude and orientation with Dy and dx
            magnitude = grd_magn(dx, dy)
            orientation = grd_deg_theta(dx, dy)
             # Threshold the gradient’s magnitude and/or orientation to set the pixel value to 0 if it’s not an edge pixel and to 255 if it’s an edge pixel
            assert abs(orientation) <= 180
            if magnitude >= magn_thresh:
                # its an edge pixel so change the value to 255 (white)
                output_img.putpixel((i, j), 255)
            else:
                # its not an edge pixel so change the value to 0 (black)
                output_img.putpixel((i, j), 0)
    return output_img



