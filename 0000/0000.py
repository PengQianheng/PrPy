from PIL import Image, ImageDraw, ImageFont

icon = Image.open("me.jpg")
font = "C:\Windows\Fonts\Calibri.ttf" #选择字体
fontsize = int(icon.size[0] / 4) #设定字体大小
truetype = ImageFont.truetype(font,fontsize) 

draw = ImageDraw.Draw(icon) #获取绘图对象
draw.text((icon.size[0]-fontsize, 0), "6", fill=0X0000FF, font=truetype)
del draw
icon.save('.\me0.jpg')
icon.show()
