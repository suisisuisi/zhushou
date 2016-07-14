from PIL import Image
image = Image.open("‪E:\imgColor\jinshuxiaoguogaodangmingpian_379592_small.jpg")
c = image.getcolors()

print (c)