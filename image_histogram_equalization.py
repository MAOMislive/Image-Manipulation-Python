import cv2
import numpy as np

def histogram_equalization(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path, 0)  # Load as grayscale

    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(image)

    # Save the result
    cv2.imwrite(output_path, equalized_image)
    print(f"Histogram equalized image saved as {output_path}")

# Example usage
histogram_equalization('input_image.jpg', 'equalized_image.jpg')
