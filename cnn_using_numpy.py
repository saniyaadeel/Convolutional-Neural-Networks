
"""CNN using Numpy

CNN in libraries like keras are very easy to implement. In this notebook, we will implement a convolution layer used in CNN using numpy library.

We will use a numeric example and find out the result with and without padding.
"""

import numpy as np

"""It is known that despite any number of channels, the output of convolution layer is a single channel, until and unless we use multiple number of filter layers to retain the actual channel size.

In this code, we use one filter layer. 

Writing the convolution function:
"""

def Conv(InpImg, Fltr):
  m = InpImg.shape[1] # rows of input
  l = InpImg.shape[2] # columns of input
  d = InpImg.shape[0] # channels of input and channels of filter
  k = Fltr.shape[1] # rows/columns of filter

  o1 = m-k+1 # rows of output 
  o2 = l-k+1 # columns of output

  #if considering m = l, output dimensions = m-k+1 = o1 = o2
  
  out = np.zeros((o1,o2)) # output will result in a single channel image so we define it as a matrix

  for r in range(0,o1):
    kr = r+k
    for c in range(0, o2):
      kc = c+k
      out[r,c] = ((InpImg[:, r:kr, c:kc])*Fltr).sum()


  return out

"""Let's look at an example"""

i = np.array([[[1,0,0], [1,1,0], [0,1,0]], [[1,0,2], [1,2,0], [2,1,2]]])
f = np.array([[[0,0], [2,0]], [[1,2], [2,0]]])
print('Shape of input image:', i.shape)
print('Shape of filter:', f.shape)

#Applying convolution:
Conv(i,f)

"""We can see that the dimensions have reduced. This is because of border effect. This can result in information loss. Therefore one strategy to prevent this is to do padding.

Convolution with padding

To retain the dimensions of the input image, we use padding strategy. Padding adds margins of zeros around the axes of the input image.
The number of margins of zeros to be added depends on the kernel size. The best practice is to pad using (k-1)/2 zeros, where k is the kernel size (which is usually odd). Basically, the selection of the parameters is such that the image size is retained.

Let's write a function that returns a padded input upon which we can then perform convolution:
"""

# top, bottom, left and right are positions where we want to add desired number of layers of zeros
def ZeroPadding(inp, top, bottom, left, right):
  return np.pad(inp, ((0,0), (top,bottom), (left,right)), mode='constant')

"""By visualizing, we can see that to obtain th eoutput image of the same dimensions as of the input image provided with the filter of kernel size 2, we will have to make the shape (2,4,4)"""

InpPad = ZeroPadding(i, 1,0,1,0)
InpPad

Conv(InpPad, f)

"""Since the spatial dimensions have been retained, there is no information loss."""