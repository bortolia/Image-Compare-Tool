from PIL import Image
import numpy as np
import sys

try:
	img1 = Image.open('new_imgd.png')
	img2 = Image.open('g1.png')
except FileNotFoundError:
	print("The file was not found")
	sys.exit(1)

#if img1.size != img2.size:

print(img1.mode)
print(img2.mode)

img1 = img1.convert('L')
img2 = img2.convert('L')

imgArr1 = np.asarray(img1)
imgArr2 = np.asarray(img2)

print(imgArr1.shape)
#for x in np.nditer(imgArr1[107:108]):
#	print(x)

diff_count = 0
for x, y in np.nditer([imgArr1, imgArr2]):
	if(x != y):
		#print(x,y)
		if abs(int(x) - int(y)) > 10:
			#print(str(int(x) - int(y)) + " > 10")
			diff_count += 1

sim = diff_count/(imgArr1.shape[0] * imgArr1.shape[1])

if sim == 0:
	print("Similarity: " + str(int(sim)))
else:
	print("Similarity: " + "{0:.5f}".format(sim))

