from PIL import Image

file = r"/home/siredgar20/Schreibtisch/coding_challenge/solutions/level3/original_img.png"
with Image.open(file) as img:
    x,y = img.size
    img = img.convert("RGB")
cord_x = []
cord_y = []
for i in range(0,x):
    for g in range(0,y):
        if img.getpixel((i,g)) != (255,255,255): 
            continue 
        elif img.getpixel((i,g)) <= (255,255,255) and img.getpixel((i,g)) >= (240,240,240):
            cord_x.append(i)
            cord_y.append(g)
            
       # elif img.getpixel(i,g) ==
print(cord_x)
print(cord_y)

img_new = Image.new("RGB",(x,y),(255,255,255))

px = img_new.load() # always with () otherwise error

for x,y in  zip(cord_x,cord_y):
    px[x,y] = (254,254,254)  

img_new.show()
