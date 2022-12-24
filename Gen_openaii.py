import openai
import webbrowser
import api

OPENAI_API_KEY = api.open_key()
openai.api_key = OPENAI_API_KEY

print()
print()
print("Welcome to the OpenAI Image Generator!")


keep_on = 'y'
while keep_on == 'y':
    print()
    print()
    prompty = input("Enter your prompt for an image to create: ")

    lynxie = openai.Image.create(
        prompt=prompty, n=1, size="1024x1024")

    image_url = lynxie['data'][0]['url']

# print(image_url)

    webby = webbrowser.open_new(image_url)

    print()
    keep_on = input("Would you like to continue? (y/n): ")

print()
print()
print("Thank you for using the OpenAI Image Generator!")
