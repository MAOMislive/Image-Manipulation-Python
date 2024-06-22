import cv2
import os


def upscale_image(input_image_path, output_image_path, scale_factor):
    # Read the input image
    image = cv2.imread(input_image_path)

    # Resize the image
    new_width = int(image.shape[1] * scale_factor)
    new_height = int(image.shape[0] * scale_factor)
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

    # Save the resized image
    cv2.imwrite(output_image_path, resized_image)
    print(f"Upscaled image saved at {output_image_path}")


# Example usage
input_folder = r'C:\Users\User\Desktop\Images\PNG'
output_folder = r'C:\Users\User\Desktop\Images\JPEG'
scale_factor = 4  # Adjust as needed

upscale_image(input_folder, output_folder, scale_factor)


print('Done Upscaling!')
