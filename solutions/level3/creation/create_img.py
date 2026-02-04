from PIL import Image, ImageDraw, ImageFont, ExifTags

img = Image.new("RGB",(1000,1000),(0,0,0))

I1 = ImageDraw.Draw(img) # call method to add 2d to pic
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",30)
I1.text((100,500),"you found the solution [1nvis1ble_1nk.html]", font=font, fill=(0,0,1))
img.save(f"challenge.png")
img.show()

# this creates challenge_img
