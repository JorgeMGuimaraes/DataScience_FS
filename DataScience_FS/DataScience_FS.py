import enum, random

class Kid(enum.Enum):
    Boy     = 0,
    Girl    = 1

def random_kid() -> Kid:
    return random.choice([Kid.Boy, Kid.Girl])

both_girls, older_girl, either_girl = 0, 0, 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older   = random_kid()

    if older == Kid.Girl                            : older_girl += 1
    if older == Kid.Girl and younger == Kid.Girl    : both_girls += 1
    if older == Kid.Girl or younger == Kid.Girl     : either_girl += 1

print("P(both | older): %f"%(both_girls / older_girl))
print("P(both | either): %f"%(both_girls / either_girl))

from collections import Counter
from Probabilty import binomial, normal_cdf
import matplotlib.pyplot as plt
import math

def binomial_histogram(p: float, n: int, num_points: int) -> None:
    data = [binomial(n, p) for _ in range(num_points)]
    
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()], [v / num_points for v in histogram.values()], 0.8, color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.show()
    return

binomial_histogram(0.75, 100, 10000)