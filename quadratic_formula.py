# solves the quadratic formula ax^2 + bx + c = 0

import cmath

# note: use operand ** instead of ^ 
# note: In Python 3 the / operator is for floating point division. Use // for integer division.

def solveQuadratic(a, b, c):
    # calculating the discriminant
    disc = (b**2) - (4*a*c)

    root1 = (-b+cmath.sqrt(disc))/(2*a)
    root2 = (-b-cmath.sqrt(disc))/(2*a)
    rootpair = (root1, root2)

    if root1 != root2:
        return print(rootpair)  
    else:
        return print(root1)

solveQuadratic(1, -5, 6)