from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

print(Image.__version__)
print(np.__version__)
i = Image.open("number_0.png")
imgArray = np.asarray(i)
# Image._show(i)
print imgArray
print "Size : ", imgArray.size
# plt.imshow(imgArray)
# plt.show()

fig = plt.figure()
ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8, 6), (3, 0), rowspan=4, colspan=3)

ax1.imshow(imgArray)
ax2.imshow(imgArray)
ax3.imshow(imgArray)
ax4.imshow(imgArray)
plt.show()
