import requests

import json

SUBSCRIPTION_KEY = "61ca29eb5a654dff98b6f4bf96f2aff5"

vision_service_address = "https://pythonimageanalizejonatas.cognitiveservices.azure.com/vision/v2.0/ocr?"
address = vision_service_address + "analyze"

parameters  = {'detalls':'text',
               'language':'pt', 
                'detectOrientation' : 'true'}


image_path = "./flamengo.jpg"
image_data = open(image_path, "rb").read()


headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}


response = requests.post(address, headers=headers, params=parameters, data=image_data)


response.raise_for_status()


results = response.json() 
print(json.dumps(results))

