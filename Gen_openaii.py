import openai
import webbrowser
import api
import urllib.request as ulr
import os
import ssl

OPENAI_API_KEY = api.open_key()
openai.api_key = OPENAI_API_KEY
ssl._create_default_https_context = ssl._create_unverified_context


print()
print()
print("Welcome to the OpenAI Image Generator!")


colors = [
    ##"brown", 
    ##"white", 
    "tuxedo",
    "black", 
    "striped", 
    "orange", 
    "black"
    ]
animals = [ 
           "cat",
           "kitten",
            "kitty"
           ]
poses = ["facing camera", "walking to camera",
          "looking left", "looking right"
         ]
mouths =[
    "mouth closed",  
   ## "lizard in mouth", ##"rat in mouth",
    ## "mouse in mouth", "bird in mouth"
    "mouth open"
    ]

for color in colors:
    for animal in animals:
        for pose in poses:
            for mouth in mouths:
                n = 10
                prompt = f"{color} {animal} {pose} {mouth}"
                folder_path = '/Volumes/Elements/GitHub/cats_with_birds/For_Training/gen_ai/'
                image_prefix = str(prompt.replace(" ", "_"))
    ##image_count = 0
                lynxie = openai.Image.create(prompt= image_prefix, n=n, size="256x256")
                print("the prompt this time is " , prompt, "    ")
                for i in range(n):
                    image_url = lynxie['data'][i]['url']
                 ##webby = webbrowser.open_new(image_url)
                    ulr.urlretrieve(lynxie['data'][i]['url'], folder_path + image_prefix + str(i) + '.jpg')


print("competed")




keep_on = 'y'
while keep_on == 'y':
    print()
    print()
    prompty = input("Enter your prompt for an image to create: ")
    n = int(input('and how many?   '))
    folder_path = '/Volumes/Elements/GitHub/cats_with_birds/For_Training/gen_ai/'
    image_prefix = str(prompty.replace(" ", "_"))
    ##image_count = 0
    lynxie = openai.Image.create(
        prompt=prompty, n=n, size="256x256")
    for i in range(n):
        image_url = lynxie['data'][i]['url']
        ##webby = webbrowser.open_new(image_url)
        ulr.urlretrieve(lynxie['data'][i]['url'], folder_path + image_prefix + str(i) + '.jpg')

    

    print()
    print("the number saved is ", n)
    keep_on = input("Do you want to continue? y/n  ")

print()
print()
print("Thank you for using the OpenAI Image Generator!")
