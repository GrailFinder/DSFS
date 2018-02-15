
from collections import Counter
import sys, math


# dirty hack
sys.path.append('/home/grail/PycharmProjects/DSFS/')

from four_linear.vector import Vector

def mean(x):
    return sum(x) / len(x)

def median(v):
    n = len(v)
    midpoint = n//2

    if n % 2 == 1:
        return sorted(v)[midpoint]
    else:
        return (sorted(v)[midpoint-1] + sorted(v)[midpoint]) / 2

def quantile(x, p):
    per_index = int(p * len(x))
    return sorted(x)[per_index]

def mode(x):
    # there is no room for second item
    c = Counter(x)
    return c.most_common(1)[0][0]

def data_range(x):
    return max(x) - min(x)

def delta_mean(x):
    mx = mean(x)
    return [xi - mx for xi in x]

def variance(x):
    n = len(x)
    deviations = delta_mean(x)
    v = Vector(deviations)
    return v.sum_of_squares() / (n - 1)

def std(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    return quantile(x, .75) - quantile(x, .25)

# correlation
def covariance(x, y):
    n = len(x)
    x = Vector(delta_mean(x))    
    return x.dot(delta_mean(y)) / (n - 1)

def correlation(x, y):
    std_x = std(x)
    std_y = std(y)

    if std_x > 0 and std_y > 0:
        return covariance(x, y) / std_x / std_y
    else:
        return 0

if __name__ == "__main__":
    a = [1, 2, 3, 2, 5, 3, 6, 7, 5, 8, 9]
    b = [6, 5, 5, 5, 5, 3, 6, 7, 5, 8, 9]

    print(variance(a))
    print(std(a))
    print(covariance(a, b))
