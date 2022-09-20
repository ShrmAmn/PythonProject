# ************************ BroadCasting ***************************
# Broadcasting
# Numpy arrays differ from a normal Python list because of their ability to broadcast:

arr = np.arange(0,11)

#Setting a value with index range (Broadcasting)
arr[0:5]=100
# array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])

# Reset array, we'll see why I had to reset in  a moment
arr = np.arange(0,11)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

#Important notes on Slices
slice_of_arr = arr[0:6]
# array([0, 1, 2, 3, 4, 5])

#Change Slice
slice_of_arr[:]=99
# array([99, 99, 99, 99, 99, 99])

#To get a copy, need to be explicit
arr_copy = arr.copy()
# array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])
