import numpy as np

# Generating random vector with values in the range of 1 and 15.
x = np.random.random_integers(1,15,15)
print(x)

# Replacing max value with zero.
x[x.argmax()]=0

print(x)



