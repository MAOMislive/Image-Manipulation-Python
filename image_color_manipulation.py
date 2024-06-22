import cv2
import numpy as np

def convert_to_grayscale(image_path, output_path):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, grayscale_image)
    print(f"Grayscale image saved to {output_path}")

def apply_sepia(image_path, output_path):
    image = cv2.imread(image_path)
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_image = cv2.transform(image, sepia_filter)
    sepia_image = np.clip(sepia_image, 0, 255)
    cv2.imwrite(output_path, sepia_image)
    print(f"Sepia tone image saved to {output_path}")

def adjust_brightness_contrast(image_path, output_path, alpha=1.0, beta=0):
    image = cv2.imread(image_path)
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    cv2.imwrite(output_path, adjusted_image)
    print(f"Brightness/Contrast adjusted image saved to {output_path}")

# Example usage
convert_to_grayscale('input_image.jpg', 'grayscale_image.jpg')
apply_sepia('input_image.jpg', 'sepia_image.jpg')
adjust_brightness_contrast('input_image.jpg', 'adjusted_image.jpg', alpha=1.2, beta=50)

print("Done Manipulating!!")
