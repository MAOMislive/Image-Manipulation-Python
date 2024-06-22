import cv2

def reduce_noise(image_path, output_path, method='gaussian', ksize=5):
    image = cv2.imread(image_path)
    
    if method == 'gaussian':
        denoised_image = cv2.GaussianBlur(image, (ksize, ksize), 0)
    elif method == 'median':
        denoised_image = cv2.medianBlur(image, ksize)
    elif method == 'bilateral':
        denoised_image = cv2.bilateralFilter(image, ksize, 75, 75)
    else:
        print(f"Error: Unknown method '{method}'")
        return
    
    cv2.imwrite(output_path, denoised_image)
    print(f"Noise reduced image saved to {output_path}")

# Example usage
reduce_noise('input_image.jpg', 'denoised_image.jpg', method='gaussian', ksize=5)
reduce_noise('input_image.jpg', 'denoised_image_median.jpg', method='median', ksize=5)
reduce_noise('input_image.jpg', 'denoised_image_bilateral.jpg', method='bilateral', ksize=15)
