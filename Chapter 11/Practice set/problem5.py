class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        # Element-wise addition of two vectors
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimension")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        # Dot product of two vectors
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimension")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        return str(self.components)

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([7, 8, 9])
print(v1 + v2)        # Vector addition
print(v1 * v2)       # Dot product

print(v1 + v3)
print(v1 * v3)