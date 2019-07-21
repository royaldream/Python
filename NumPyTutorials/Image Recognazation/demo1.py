from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

print(Image.__version__)
print(np.__version__)
i = Image.open("number_0.jpg")
imgArray = np.asarray(i)
print imgArray
plt.imshow(imgArray)
plt.show()
