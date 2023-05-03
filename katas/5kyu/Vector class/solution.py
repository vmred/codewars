# Vector class
# Create a Vector object that supports addition, subtraction, dot products, and norms.
# So, for example:
# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])

# a.add(b)      # should return a new Vector([4, 6, 8])
# a.subtract(b) # should return a new Vector([-2, -2, -2])
# a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
# a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# a.add(c)      # raises an exception
# If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

# Also provide:
# a toString method, so that using the vectors from above,
# a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
# an equals method, to check that two vectors that have the same components are equal
# Note: the test cases will utilize the user-provided equals method.


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def __str__(self):
        return tuple(self.vector).__str__().replace(' ', '')

    def check_length(self, obj):
        if len(self.vector) != len(obj.vector):
            raise ValueError('Vectors of different length')

    def equals(self, obj):
        return self.vector == obj.vector

    def add(self, obj):
        self.check_length(obj)
        return Vector([x + y for x, y in zip(self.vector, obj.vector)])

    def subtract(self, obj):
        self.check_length(obj)
        return Vector([x - y for x, y in zip(self.vector, obj.vector)])

    def dot(self, obj):
        self.check_length(obj)
        return sum(x * y for x, y in zip(self.vector, obj.vector))

    def norm(self):
        return sum(x**2 for x in self.vector) ** 0.5
