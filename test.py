# pip install tensorflow keras pillow numpy pytesseract opencv-python

import cv2
import numpy as np
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use adaptive thresholding to segment the text and logo
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    return image, gray, thresh


def extract_text(gray_image):
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(gray_image)
    return text


full_image_path = r".\raw_images\Reliance-Smart-Bill.webp"
image, gray, thresh = preprocess_image(full_image_path)
# Display the image in a window
# Display the image in a window
cv2.imshow('Image', image)
text = extract_text(gray)

print(text)
# Wait for the user to press a key
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
