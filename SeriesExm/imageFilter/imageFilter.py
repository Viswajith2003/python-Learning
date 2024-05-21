from PIL import Image, ImageFilter

# Function to resize an image
def resize_image(image_path, width, height, output_path):
    image = Image.open(image_path)  # Open the image
    resized_image = image.resize((width, height))  # Resize to specified dimensions
    resized_image.save(output_path)  # Save the resized image

# Function to rotate an image
def rotate_image(image_path, angle, output_path):
    image = Image.open(image_path)  # Open the image
    rotated_image = image.rotate(angle)  # Rotate by a given angle
    rotated_image.save(output_path)  # Save the rotated image

# Function to convert an image to grayscale
def grayscale_image(image_path, output_path):
    image = Image.open(image_path)  # Open the image
    grayscale_image = image.convert("L")  # Convert to grayscale
    grayscale_image.save(output_path)  # Save the grayscale image

# Function to apply a filter to an image
def filter_image(image_path, filter_type, output_path):
    image = Image.open(image_path)  # Open the image
    filtered_image = image.filter(filter_type)  # Apply the specified filter
    filtered_image.save(output_path)  # Save the filtered image

# Function to crop an image to a specified bounding box (bbox)
def crop_image(image_path, bbox, output_path):
    image = Image.open(image_path)  # Open the image
    cropped_image = image.crop(bbox)  # Crop the image to the given bbox
    cropped_image.save(output_path)  # Save the cropped image

# Main function to demonstrate the image operations
def main():
    image_path = "/home/tufa15/Documents/PYTHON_pgms/SeriesExm/imageFilter/images/inputImg.jpg"  # Path to the input image

    # Resize the image
    resize_image(image_path, 300, 200, "resized_image.jpg")

    # Rotate the image by 90 degrees
    rotate_image(image_path, 90, "rotated_image.jpg")

    # Convert the image to grayscale
    grayscale_image(image_path, "grayscale_image.jpg")

    # Apply a blur filter to the image
    filter_image(image_path, ImageFilter.BLUR, "blurred_image.jpg")

    # Crop the image to a bounding box
    crop_bbox = (100, 100, 400, 300)  # (left, top, right, bottom)
    crop_image(image_path, crop_bbox, "cropped_image.jpg")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
