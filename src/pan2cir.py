import numpy as np
import Image
import math

#Image.fromarray(pix).
pan = np.array(Image.open('panorama.jpg'))
w = pan.shape[1]
h = pan.shape[0]

cir = np.zeros((h,h,3))

def car2cir(x,y):
	theta = math.atan2(y,x)
	r = math.sqrt(x*x+y*y)
	return (theta,r)

def cir2car(theta,r):
	x = r*math.cos(theta)
	y = r*math.sin(theta)
	return (x,y)

def cir2Pan(theta,r,panSize,flip=True):
	if r > panSize[1]:
		return None
	if flip:
		y = panSize[1]-r-1
	else:
		y = r
	x = panSize[0]*theta/(2*math.pi)
	return (x,y)

for cc in range(3):
	a = pan[:,:,cc]
	b = cir[:,:,cc]
	#rows
	for i in xrange(b.shape[0]):
		for j in xrange(b.shape[1]):
			dstCir = car2cir(i-b.shape[0]/2,j-b.shape[1]/2)
			srcCar = cir2Pan(dstCir[0],dstCir[1],[a.shape[1],a.shape[0]])
			if srcCar == None:
				continue

			p = a[srcCar[1],srcCar[0]];
			b[i,j] = p;

result = Image.fromarray(np.uint8(cir))
result.show()
result.save('result.jpg')


