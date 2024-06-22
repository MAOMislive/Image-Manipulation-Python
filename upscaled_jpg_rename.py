import cv2
import os
from pathlib import Path
from PIL import Image


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


def upscale_batch(input_folder, output_folder, scale_factor):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
            input_image_path = os.path.join(input_folder, file)
            output_image_path = os.path.join(output_folder, file)
            upscale_image(input_image_path, output_image_path, scale_factor)


def convert_png_to_jpg(input_folder, output_folder):
    input_path = Path(input_folder)
    input_files = input_path.glob("*.png")
    output_path = Path(output_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for f in input_files:
        output_file = output_path / Path(f.stem + ".jpg")
        im = Image.open(f)
        if im.mode == 'RGBA':
            im = im.convert('RGB')
        im.save(output_file)
        print(f"Converted {f} to {output_file}")


def rename_files(input_folder):
    # Get all files in the input folder
    files = os.listdir(input_folder)

    # Sort files to ensure consistent ordering
    files.sort()

    # Rename files sequentially
    for i, file in enumerate(files):
        if file.endswith('.jpg'):
            # Construct new name
            new_name = f"Image_no-{i + 1}.jpg"

            # Rename file
            os.rename(os.path.join(input_folder, file), os.path.join(input_folder, new_name))

            print(f"Renamed {file} to {new_name}")


# Main function to combine all tasks
def process_images(input_folder, upscale_folder, convert_folder, scale_factor):
    print("Starting upscaling...")
    upscale_batch(input_folder, upscale_folder, scale_factor)

    print("Starting conversion from PNG to JPG...")
    convert_png_to_jpg(upscale_folder, convert_folder)

    print("Starting renaming of files...")
    rename_files(convert_folder)

    print("Done processing!")


# Example usage
input_folder = r'C:\Users\User\Desktop\Images\PNG'
upscale_folder = r'C:\Users\User\Desktop\Images\Upscaled'
convert_folder = r'C:\Users\User\Desktop\Images\JPEG'
scale_factor = 4  # Adjust as needed

process_images(input_folder, upscale_folder, convert_folder, scale_factor)

