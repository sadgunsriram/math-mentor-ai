import easyocr

reader = easyocr.Reader(['en'])

def extract_text_from_image(image):

    result = reader.readtext(image)

    text = " ".join([r[1] for r in result])

    return text