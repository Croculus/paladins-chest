import imager, cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException


api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '23559cb9-24a0-4781-b0ac-fcae3d6247bb'

imager.main()

deals = ['image\deal1.jpg','image\deal2.jpg', 'image\deal3.jpg']

text = []
for deal in deals:
    image_file = deal # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.
    try:
        # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
        api_response = api_instance.image_ocr_post(image_file)
        print(api_response)
        text.append(api_response)
    except ApiException as e:
        print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)
    







