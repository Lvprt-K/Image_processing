# Image Edge Detection using OpenCV

This Python script utilizes OpenCV to perform image edge detection using Sobel filters and non-maximum suppression techniques.

## Features

- **Image Loading:** Read an image file for processing.
- **Grayscale Conversion:** Convert the image to grayscale for edge detection.
- **Gaussian Blurring:** Apply Gaussian blur to reduce noise in the image.
- **Sobel Filter:** Detect horizontal and vertical edges using Sobel filters.
- **Gradient Magnitude and Direction:** Calculate gradient magnitude and direction.
- **Non-Maximum Suppression:** Perform non-maximum suppression to thin edges.
- **Double Thresholding:** Apply double thresholding to detect potential edges.
- **Edge Tracking by Hysteresis:** Perform edge tracking to obtain final edge map.

## Usage

1. Ensure you have Python 3.x and OpenCV library installed.
2. Load an image using `cv2.imread()` and specify its path.
3. Run the script to execute the image processing operations.
4. View and analyze the displayed images representing various stages of edge detection.
5. Adjust threshold values (`low_threshold` and `high_threshold`) for different edge detection results.


## Customization

- Modify the path to a different image file for testing edge detection on various images.
- Experiment with different threshold values to control edge detection sensitivity.
- Explore additional image processing techniques or filters available in OpenCV.

