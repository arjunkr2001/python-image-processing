from images import Image
#from functools import reduce

i = Image("img.gif")

#def tripleSum(t1,t2):
#	return (t1[0]+t2[0],t1[1]+t2[1],t1[2]+t2[2])

for y in range(1,i.getHeight()-1):
	for x in range(1,i.getWidth()-1):
	
		oldP = i.getPixel(x,y)
		left = i.getPixel(x-1,y)
		right = i.getPixel(x+1,y)
		top = i.getPixel(x,y-1)
		bottom = i.getPixel(x,y+1)
		
		#sums = reduce(tripleSum,[oldP,left,right,top,bottom])
		sums = (
			oldP[0]+left[0]+right[0]+top[0]+bottom[0],
			oldP[1]+left[1]+right[1]+top[1]+bottom[1],
			oldP[2]+left[2]+right[2]+top[2]+bottom[2]
		)
		
		#averages = tuple(map(lambda x: x//5, sums))
		averages = (sums[0]//5,sums[1]//5,sums[2]//5)
		
		i.setPixel(x,y, averages)
		
i.draw()
