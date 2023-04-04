from images import Image

i = Image("img.gif")
for y in range(i.getHeight()):
	for x in range(i.getWidth()):
		(r,g,b) = i.getPixel(x,y)
		#avg = (r+g+b)//3
		#i.setPixel(x,y,(avg,avg,avg))
		r = int(r * 0.299)
		g = int(g * 0.587)
		b = int(b * 0.114)
		lum = r+g+b
		i.setPixel(x,y,(lum,lum,lum))
		
i.draw()
