from PIL import Image
from realesrgan import RealESRGAN

def upscale_image(input_image_path, output_image_path, scale=4):
    # Open the input image
    image = Image.open(input_image_path)
    
    # Initialize the RealESRGAN model
    model = RealESRGAN(device='cuda')  # Use 'cpu' if you don't have a GPU
    model.load_weights('weights/RealESRGAN_x4.pth', download=True)  # Ensure the model weights are downloaded
    
    # Upscale the image
    sr_image = model.predict(image)
    
    # Save the upscaled image
    sr_image.save(output_image_path)
    print(f"Upscaled image saved at {output_image_path}")

# Example usage
input_image_path = 'path/to/your/input/image.jpg'
output_image_path = 'path/to/your/output/upscaled_image.jpg'
upscale_image(input_image_path, output_image_path)
