import openai
import os
import sys
import api

OPENAI_API_KEY = api.open_key()
openai.api_key = OPENAI_API_KEY

lynxie = openai.Image.create(
    prompt="Ogre giving flower to small girl", n=1, size="1024x1024")

image_url = lynxie['data'][0]['url']

print(image_url)
