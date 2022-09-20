# ************************   CREATING NUMPY ARRAYS ****************************** #

# ************************   From Python List ****************************** #
my_list = [1,2,3]
print(my_list)
# [1, 2, 3]

np.array(my_list)
# array([1, 2, 3])

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

np.array(my_matrix)
# array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# ************************   Built-in Methods ****************************** #

# ************************     Arange   ****************************** #

np.arange(0,10)  # arange( start , till )
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

np.arange(0,11,2)  # arange( start , till , steps )
# array([ 0,  2,  4,  6,  8, 10])
