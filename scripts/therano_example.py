""" A theano example, as found in chapter 2 """
import theano
from theano import tensor

# Define tensors as 2 symbolic floating point scalars

a = tensor.dscalar()
b = tensor.dscalar()

# create a symbolic expression and store it in c
c = a + b

# convert it into a callable object, a function, that takes a,b and returns the
# result
f = theano.function([a, b], c)

# call the function, by passing a = 10.5, b = 25.5, and evaluate c
result = f(10.5, 25.5)

print(result)
