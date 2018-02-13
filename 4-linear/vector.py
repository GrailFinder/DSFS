#!/home/grail/anaconda3/bin/python

import math

class Vector():

    def __init__(self, v):
        self.v = v

    def __iter__(self):
        for e in self.v:
            yield e

    def add(self, w):
        if len(self.v) != len(w):
            raise IndexError("vector_add takes only vectors of the same length")
        else:
            return [self.v[i] + w[i] for i in range(len(self.v))]

    def subtract(self, w):
        return [v_i - w_i for v_i, w_i in zip(self.v, w)]

    def sum(self, vectors):
        result = vectors[0]
        for vector in vectors[1:]:
            result = self.v.add(result, vector)
            print(vector, result)
        return result

    def scalar_multiply(self, c, v):
        return [c * v_i for v_i in v]

    def mean(self, vectors):
        n = len(vectors)
        return self.scalar_multiply(1/n, self.sum(vectors))

    def dot(self, w):
        """v_1 * w_1 + ... + v_n * w_n"""
        return sum(v_i * w_i for v_i, w_i in zip(self.v, w))

    def sum_of_squares(self, v):
        return self.dot(v)

    def magnitude(self, v):
        return math.sqrt(self.sum_of_squares(v))

    def squared_distance(self, v):
        return self.sum_of_squares(self.subtract(v))

    def distance(self, v):
        return math.sqrt(self.squared_distance(v))

if __name__ == "__main__":
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    #print(vector_add(a, b))
    print(b.subtract(a))

    print(a.dot(b))
