from images import Image

i = Image("img.gif")
for y in range(i.getHeight()):
	for x in range(i.getWidth()):
		(r,g,b) = i.getPixel(x,y)
		if (r+g+b)//3 >= 100:
			i.setPixel(x,y,(255,255,255))
		else:
			i.setPixel(x,y,(0,0,0))
i.draw()
