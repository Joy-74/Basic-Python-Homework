'''
    PIC 16A Homework 5
    Author: Jiayu Li
    UID: 605-348-766
    Discussion Section: 3B
    Date: 02/25/2023
'''

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def myconv(img, img_filter):
    # Get the shapes of the image and filter
    img_height, img_width, img_color = img.shape
    filter_height, filter_width = img_filter.shape

    # Calculate the padding size
    padding_height = filter_height // 2
    padding_width = filter_width // 2

    # Create a new image with the same shape as the input image (white background)
    blurred_img = np.ones_like(img)

    # Loop through each pixel in the image
    for i in range(padding_height, img_height - padding_height):
        for j in range(padding_width, img_width - padding_width):
            # Loop through each channel in the image
            for c in range(img_color):
                # Apply the convolution to the current pixel and channel
                y = i - padding_height
                end_y = i + padding_height + 1
                x = j - padding_width
                end_x = j + padding_width + 1
                blurred_img[i, j, c] = np.sum(img[y:end_y, x:end_x, c] * img_filter)

    # Return blurred image data
    return blurred_img


# Test
if __name__ == '__main__':
    # Create a test image
    # Read cat image
    cat_img = mpimg.imread('cat.png')
    # Create a test filter
    image_filter = np.ones((5, 5)) * 0.04
    blurred_cat = myconv(cat_img, image_filter)
    # Display result
    plt.imshow(blurred_cat)
    plt.savefig('blurred_cat1.png')

    # Create a test filter
    image_filter = np.ones((3, 3)) * (0.04)
    blurred_cat2 = myconv(cat_img, image_filter)

    # Display result
    plt.imshow(blurred_cat2)
    plt.savefig('blurred_cat2.png')

    # Create a test filter
    image_filter = np.ones((11, 11)) * 0.005
    blurred_cat3 = myconv(cat_img, image_filter)

    # Display result
    plt.imshow(blurred_cat3)
    plt.savefig('blurred_cat3.png')
