'''
Problem:
Given a cube of size n*n*n (i.e made up of n^3 smaller cubes), find the
number of smaller cubes on the surface. Extend this to k-dimension.
'''


def surface(n, k=3):
    return n**k - (n - 2)**k


print(surface(3))
print(surface(3, 2))
