# -*- coding: utf-8 -*-
"""Image_Processing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F1Y32QuUhMGmjCp7I_WHmL4c9z4JauiP
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

# reading image
img = cv2.imread("/content/uni back.jpg",1)
g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#blur image by gaussian filter
gaus_img = cv2.GaussianBlur(g_img,(3,3),0)
cv2_imshow(img)
cv2_imshow(g_img)
cv2_imshow(gaus_img)

#sobel filter
grdx = cv2.Sobel(gaus_img,-1,1,0)
grdy = cv2.Sobel(gaus_img,-1,0,1)
grd_xy = cv2.addWeighted(grdx,0.5,grdy,0.5,0)
cv2_imshow(grdx)
cv2_imshow(grdy)
cv2_imshow(grd_xy)

#gradient magnitude and direction
mag_grd = np.sqrt(grdx**2 + grdy**2)
grd_dir = np.arctan2(grdy, grdx) * (180 / np.pi) % 180
cv2_imshow(mag_grd)
cv2_imshow(grd_dir)
#non maximum suppression
def non_maximum_suppression(mag_grd, grd_dir):
    rows, cols = mag_grd.shape
    suppressed = np.zeros_like(mag_grd)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            angle = grd_dir[i, j]

            # Determine the neighboring pixels based on the gradient direction
            if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                nbr = [mag_grd[i, j+1], mag_grd[i, j-1]]
            elif 22.5 <= angle < 67.5:
                nbr = [mag_grd[i-1, j+1], mag_grd[i+1, j-1]]
            elif 67.5 <= angle < 112.5:
                nbr = [mag_grd[i-1, j], mag_grd[i+1, j]]
            else:
                nbr = [mag_grd[i-1, j-1], mag_grd[i+1, j+1]]

            # Perform non-maximum suppression
            if mag_grd[i, j] >= max(nbr):
                suppressed[i, j] = mag_grd[i, j]

    return suppressed
    # Apply non-maximum suppression
suppressed = non_maximum_suppression(mag_grd, grd_dir)

# Define threshold values for edge detection
low_threshold = 50
high_threshold = 150

# Apply double threshold to identify potential edges
edges = np.zeros_like(suppressed)
edges[(suppressed >= low_threshold) & (suppressed <= high_threshold)] = 255

 #Convert edges to uint8 data type
edges = cv2.convertScaleAbs(edges)
# Perform edge tracking by hysteresis
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)

# Display the resulting edges
cv2_imshow(edges)
cv2.waitKey(0)
cv2.destroyAllWindows()