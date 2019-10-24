# Create a class Vector that has simple (3D) vector operators.

# In your class, you should support the following operations, given Vector a and Vector b:

# a + b # returns a new Vector that is the resultant of adding them
# a - b # same, but with subtraction
# a == b # returns true if they have the same magnitude and direction
# a.cross(b) # returns a new Vector that is the cross product of a and b
# a.dot(b) # returns a number that is the dot product of a and b
# a.to_tuple() # returns a tuple representation of the vector.
# str(a) # returns a string representation of the vector in the form "<a, b, c>"
# a.magnitude # returns a number that is the magnitude (geometric length) of vector a.
# a.x # gets x component
# a.y # gets y component
# a.z # gets z component
# Vector([a,b,c]) # creates a new Vector from the supplied 3D array.
# Vector(a,b,c) # same as above
# The test cases will not mutate the produced Vector objects, so don't worry about that.


class Vector:
    def __init__(self, *args):
        self.vector = list(args[0]) if len(args) == 1 else list(args)
        self.x, self.y, self.z = self.vector
        self.magnitude = sum(i ** 2 for i in self.vector) ** 0.5

    def __str__(self):
        return '<{}>'.format(', '.join(map(str, self.vector)))

    def __add__(self, vector):
        return Vector([i + j for i, j in zip(self.vector, vector.vector)])

    def __sub__(self, vector):
        return Vector([i - j for i, j in zip(self.vector, vector.vector)])

    def __eq__(self, vector):
        return self.vector == vector.vector

    def to_tuple(self):
        return tuple(self.vector)

    def dot(self, vector):
        return sum(i[0] * i[1] for i in zip(self.vector, vector.vector))

    def cross(self, vector):
        a = self.vector
        b = vector.vector

        dim = len(a)
        r = []
        for i in range(dim):
            if i == 0:
                j, k = 1, 2
                r.append(a[j] * b[k] - a[k] * b[j])
            elif i == 1:
                j, k = 2, 0
                r.append(a[j] * b[k] - a[k] * b[j])
            else:
                j, k = 0, 1
                r.append(a[j] * b[k] - a[k] * b[j])

        return Vector(r)
