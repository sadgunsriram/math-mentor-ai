import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'])

def extract_text_from_image(uploaded_file):

    image = Image.open(uploaded_file)
    image = np.array(image)

    result = reader.readtext(image)

    text = " ".join([item[1] for item in result])

    return text