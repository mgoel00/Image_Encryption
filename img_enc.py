from PIL import Image
import img_enc_playfair as encrypt
import random

print("\t\t\t*** PLAYFAIR IMAGE ENCRYPTION CIPHER ***")
print("Encrypting Image!!")


img = Image.open('images1.jpg','r')

pixels = list(img.getdata())

size = len(pixels)


key=[ 1,8,25,41,37,98,54,57,69,89,75,111,124,126,139,151,162,175,183,188,198,199,128,203,215,247,255,0,236,228,169,73 ]

new_r = encrypt.cipher(pixels,key,size,value = 0)
new_g = encrypt.cipher(pixels,key,size,value = 1)
new_b = encrypt.cipher(pixels,key,size,value = 2)


new_img = []
for r,g,b in zip(new_r,new_g,new_b):
    tup = (r,g,b)
    new_img.append( tup )
#
#print(str(new_img))
# enc_img_array = numpy.array(new_img,dtype = numpy.uint8)
# enc_img = Image.fromstring(enc_img_array)
# enc_img.save('enc.jpg')
enc_img = Image.new(img.mode,img.size)
enc_img.putdata(new_img)
enc_img.save('enc.jpg')
print("Encryption Done!!")
