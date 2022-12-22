import openai
import os

api_secret_key = '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'

openai.api_key = api_secret_key

lynxie = openai.Image.create(
    prompt="Ogre giving flower to small girl", n=1, size="1024x1024")

image_url = lynxie['data'][0]['url']

print(image_url)
