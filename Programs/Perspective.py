import cv2
import numpy as np

def perspective_transform(image_path, output_path, perspective_matrix):
    # Read the image
    image = cv2.imread(image_path)

    # Apply the perspective transformation
    transformed_image = cv2.warpPerspective(image, perspective_matrix, (image.shape[1], image.shape[0]))

    # Save the transformed image
    cv2.imwrite(output_path, transformed_image)

# Example usage:
if __name__ == "__main__":
    # Specify the path to your input image
    input_image_path = r"C:\Users\tamil\OneDrive\Documents\Computer Vision\images.jpeg"

    # Define the perspective transformation matrix
    # You may need to calculate this matrix based on your specific requirements
    perspective_matrix = np.array([[1, 0, 0],
                                   [0, 1, 0],
                                   [0, 0, 1]])

    # Specify the path for the output transformed image
    output_image_path = r"C:\Users\tamil\OneDrive\Documents\Computer Vision\images.jpeg"

    # Perform the perspective transformation
    perspective_transform(input_image_path, output_image_path, perspective_matrix)
    cv2.destroyAllWindows()
