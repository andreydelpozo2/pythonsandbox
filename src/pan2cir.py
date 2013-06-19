import numpy as np
import Image
import math
import sys
#from collections import defaultdict #multimap aprox
inputFile = 'IMG_0134.jpg'
#'panorama.jpg'
outputFile = 'result3.jpg'
pan = np.array(Image.open(inputFile))
w = pan.shape[1]
h = pan.shape[0]

cir = np.zeros((2*h,2*h,3))

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
print 'mapping'
for cc in range(3):
	print 'Channel:',cc
	a = pan[:,:,cc]
	b = cir[:,:,cc]
	#rows
	for i in xrange(b.shape[0]):
		print i,'/',b.shape[0]

		for j in xrange(b.shape[1]):
			dstCirs = []
			dstCirs.append(car2cir(i-b.shape[0]/2+.5,j-b.shape[1]/2+.5));
			dstCirs.append(car2cir(i-b.shape[0]/2+.5,j-b.shape[1]/2));
			dstCirs.append(car2cir(i-b.shape[0]/2,j-b.shape[1]/2+.5));
			dstCirs.append(car2cir(i-b.shape[0]/2,j-b.shape[1]/2));
			
			ps = [];		
			for dstCir in dstCirs:
				srcCar = cir2Pan(dstCir[0],dstCir[1],[a.shape[1],a.shape[0]])
				if srcCar == None:
					continue

				ps.append(a[srcCar[1],srcCar[0]]);
			
			if len(ps) != 0:
				b[i,j] = sum(ps)/len(ps)
			else:
				b[i,j] = 0


print 'saving'
result = Image.fromarray(np.uint8(cir))
# result.show()
result.save(outputFile)


#mappings = defaultdict(list)
#
#for i in xrange(cir.shape[0]):
#	for j in xrange(cir.shape[1]):
# 		dstCir = car2cir(i-cir.shape[0]/2,j-cir.shape[1]/2)
# 		srcCar = cir2Pan(dstCir[0],dstCir[1],[pan.shape[1],pan.shape[0]])
# 		if srcCar == None:
# 			continue

# 		mappings[srcCar].append((i,j))


# xx = []
# for k in mappings:
# 	xx.append(len(mappings[k])) 
