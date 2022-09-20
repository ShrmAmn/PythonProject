#  *************** Array Attributes and Methods ***********************

arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
print(arr)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#       17, 18, 19, 20, 21, 22, 23, 24])

print(ranarr)
# array([10, 12, 41, 17, 49,  2, 46,  3, 19, 39])

#  *************** Reshape ***********************
#  Returns an array containing the same data with a new shape.

arr.reshape(5,5)
# array([[ 0,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14],
#       [15, 16, 17, 18, 19],
#       [20, 21, 22, 23, 24]])

# MAX , MIN , ARGMAX , ARGMIN 
# These are useful methods for finding max or min values. 
# Or to find their index locations using argmin or argmax

ranarr.max()
# 49

ranarr.argmax()
# 4

ranarr.min()
# 2

ranarr.argmin()
# 5

#  *************** Shape ***********************
#  Shape is an attribute that arrays have (not a method):

# Vector
arr.shape
# (25,)

# Notice the two sets of brackets
arr.reshape(1,25)
# array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#        17, 18, 19, 20, 21, 22, 23, 24]])

arr.reshape(1,25).shape
# (1, 25)

# *************************** DataType ****************************

arr.dtype
#  dtype('int64')


