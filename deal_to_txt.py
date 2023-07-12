import imager, ocrspace, os


def main():
    imager.main()
    api = ocrspace.API(api_key=os.getenv('API_KEY'))
    deals = ['image\deal1.jpg','image\deal2.jpg', 'image\deal3.jpg']

    text = []
    for deal in deals:
        image_file = deal
        txt = api.ocr_file(deal)
        text.append(txt)
    return text

    







