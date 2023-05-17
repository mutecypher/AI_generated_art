import pixabay.core

# https://pixabay.com/api/docs/


pixabay_api_key =  '36349277-0c5e01bc2a22b4c5536158515'

catz = pixabay.core(pixabay_api_key)

kitty = catz.query('cat')




# get len of hits len(space)
print("{} hits".format(len(kitty)))

# downalod fisrt image
kitty[0].download("kitty.jpg", "largeImage")