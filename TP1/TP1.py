import PIL as Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# read a jpg image file
A = Image.open('../images/tensorflow.jpg')

# show the image
plt.imshow(A)
plt.show()

# show the dimentions of the image
print(A.size)

# save the image as PNG and TIFF
A.save('tensorflow.png')
A.save('tensorflow.tif')

# show their dimentions
B = Image.open('tensorflow.png')
print(B.size)

C = Image.open('tensorflow.tif')
print(C.size)

# Compare the three formats
plt.subplot(1,3,1)
plt.imshow(A)
plt.subplot(1,3,2)
plt.imshow(B)
plt.subplot(1,3,3)
plt.imshow(C)
plt.show()

# show the levels of the image, red, blue and green
plt.subplot(1,3,1)
plt.imshow(A[:,:,0])
plt.subplot(1,3,2)
plt.imshow(A[:,:,1])
plt.subplot(1,3,3)
plt.imshow(A[:,:,2])

# convert the image to grayscale
A = A.convert('L')
plt.imshow(A)
plt.show()


# convert image to binary
A = A.convert('1')
plt.imshow(A)
plt.show()


# show the histogram of the image
plt.hist(A)
plt.show()

# find the inverse image of A
A = np.array(A)
A = 255 - A
plt.imshow(A)
plt.show()


