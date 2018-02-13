#!/home/grail/anaconda3/bin/python

class Matrix():

    def __init__(self, m):
        self.m = m

    def __iter__(self):
        for row in self.m:
            yield row

    def shape(self):
        num_rows = len(self.m)
        num_cols = len(self.m[0]) if self.m else 0
        return num_rows, num_cols

    def get_row(self, i):
        return self.m[i]

    def get_column(self, j):
        return [row[j] for row in self.m]

    def make_matrix(self, nrows, nclos, entry_fn):
        return [[entry_fn(i, j) for j in range(nclos)] for i in range(nrows)]

    def is_diagonal(self, i, j):
        return 1 if i==j else 0

if __name__ == '__main__':
    A = Matrix([])
    A = A.make_matrix(5, 5, A.is_diagonal)
    print(A)