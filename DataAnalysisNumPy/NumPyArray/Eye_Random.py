# **************************  EYE *********************************** #
# Creates an identity matrix

np.eye(4)
# array([[ 1.,  0.,  0.,  0.],
#      [ 0.,  1.,  0.,  0.],
#      [ 0.,  0.,  1.,  0.],
#      [ 0.,  0.,  0.,  1.]])


# **************************  Random *********************************** #
# Numpy also has lots of ways to create random number arrays:

# Rand
# Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

np.random.rand(2)
# array([ 0.11570539,  0.35279769])

np.random.rand(5,5)
# array([[ 0.66660768,  0.87589888,  0.12421056,  0.65074126,  0.60260888],
#       [ 0.70027668,  0.85572434,  0.8464595 ,  0.2735416 ,  0.10955384],
#       [ 0.0670566 ,  0.83267738,  0.9082729 ,  0.58249129,  0.12305748],
#       [ 0.27948423,  0.66422017,  0.95639833,  0.34238788,  0.9578872 ],
#       [ 0.72155386,  0.3035422 ,  0.85249683,  0.30414307,  0.79718816]])


# Randn
# Return a sample (or samples) from the "standard normal" distribution. 
# Unlike rand which is uniform:
    
np.random.randn(2)
# array([-0.27954018,  0.90078368])

np.random.randn(5,5)
# array([[ 0.70154515,  0.22441999,  1.33563186,  0.82872577, -0.28247509],
#       [ 0.64489788,  0.61815094, -0.81693168, -0.30102424, -0.29030574],
#       [ 0.8695976 ,  0.413755  ,  2.20047208,  0.17955692, -0.82159344],
#       [ 0.59264235,  1.29869894, -1.18870241,  0.11590888, -0.09181687],
#       [-0.96924265, -1.62888685, -2.05787102, -0.29705576,  0.68915542]])

# Randint
# Return random integers from low (inclusive) to high (exclusive).
        
np.random.randint(1,100)
# 44

np.random.randint(1,100,10)
# array([13, 64, 27, 63, 46, 68, 92, 10, 58, 24])
