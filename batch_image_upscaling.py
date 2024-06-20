import os
from PIL import Image
from realesrgan import RealESRGAN


def upscale_image(input_image_path, output_image_path, model):
    # Open the input image
    image = Image.open(input_image_path)

    # Upscale the image
    sr_image = model.predict(image)

    # Save the upscaled image
    sr_image.save(output_image_path)
    print(f"Upscaled image saved at {output_image_path}")


def batch_upscale(input_dir, output_dir, scale=4, device='cuda'): # Use 'cpu' if you don't have a GPU
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize the RealESRGAN model
    model = RealESRGAN(device=device)
    model.load_weights('weights/RealESRGAN_x4.pth', download=True)  # Ensure the model weights are downloaded

    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, filename)
            upscale_image(input_image_path, output_image_path, model)


# Example usage
input_dir = 'path/to/your/input/directory'
output_dir = 'path/to/your/output/directory'
batch_upscale(input_dir, output_dir, scale=4, device='cuda')  # Use 'cpu' if you don't have a GPU
