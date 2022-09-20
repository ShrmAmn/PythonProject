arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
# array([[ 5, 10, 15],
#       [20, 25, 30],
#       [35, 40, 45]])

#Indexing row
arr_2d[1]
#array([20, 25, 30])

# Format is arr_2d[row][col] or arr_2d[row,col]

# Getting individual element value
arr_2d[1][0]
# 20

# 2D array slicing

#Shape (2,2) from top right corner
arr_2d[:2,1:]
# array([[10, 15],
#       [25, 30]])

#Shape bottom row
arr_2d[2]
# array([35, 40, 45])

# ********************** Fancy indexing *****************************

#Set up matrix
arr2d = np.zeros((10,10))

#Length of array
arr_length = arr2d.shape[1]

#Set up array

for i in range(arr_length):
    arr2d[i] = i
    
# array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#       [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#       [ 2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.],
#       [ 3.,  3.,  3.,  3.,  3.,  3.,  3.,  3.,  3.,  3.],
#       [ 4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.],
#       [ 5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.],
#       [ 6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.],
#       [ 7.,  7.,  7.,  7.,  7.,  7.,  7.,  7.,  7.,  7.],
#       [ 8.,  8.,  8.,  8.,  8.,  8.,  8.,  8.,  8.,  8.],
#       [ 9.,  9.,  9.,  9.,  9.,  9.,  9.,  9.,  9.,  9.]])

arr2d[[2,4,6,8]]
# array([[ 2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.],
#       [ 4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.],
#       [ 6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.],
#       [ 8.,  8.,  8.,  8.,  8.,  8.,  8.,  8.,  8.,  8.]])

# ********************** Selection *****************

arr = np.arange(1,11)
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

arr > 4
# array([False, False, False, False,  True,  True,  True,  True,  True,  True], dtype=bool)

bool_arr = arr>4
# array([False, False, False, False,  True,  True,  True,  True,  True,  True], dtype=bool)

arr[bool_arr]
# array([ 5,  6,  7,  8,  9, 10])

arr[arr>2]
# array([ 3,  4,  5,  6,  7,  8,  9, 10])

x = 2
arr[arr>x]
# array([ 3,  4,  5,  6,  7,  8,  9, 10])
