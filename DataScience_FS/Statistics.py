#region imports
from    typing         import List, Tuple, Callable
from    collections    import Counter
from    LinearAlgebra  import *
import  math
import  matplotlib.pyplot as plt
#EndRegion
#Region types
#endregion
#region definitions
def mean(xs: List[float]) -> float:
    """Return average value"""
    return sum(xs) / len(xs)

def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, returns average of middle two elements"""
    sorted_xs   = sorted(xs)
    hi_midpoint = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, returns middle element"""
    return sorted(xs)[len(xs) // 2]

def median(v: List[float]) -> float:
    """Finds the middle-most value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

def quantile(xs: List[float], p: float) -> float:
    """Returns the p-th percentile value in xs"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)

def mode(xs: List[float]) -> List[float]:
    """Returns a list of mode values"""
    counts = Counter(xs)
    max_count = max(counts.values())
    return[xi for xi, count in counts.items() if count == max_count]

def data_range(xs:List[float]) -> float:
    """ Returns the difference between the largest and smallest elements"""
    return max(xs) - min(xs)

def deviation_from_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    """Returns the expectation of the squared deviation of a random variable from its mean.
    https://en.wikipedia.org/wiki/Variance """
    n           = len(xs)
    assert n >= 2,  "variance() requires at least two elements"
    deviations  = deviation_from_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(xs: List[float]) -> float:
    """ Returns  measure of the amount of variation or dispersion of a set of values."""
    return math.sqrt(variance(xs))

def covariance(xs: List[float], ys: List[float]) -> float:
    """Returns a measure of the joint variability of two random variables."""
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    return dot_product(deviation_from_mean(xs), deviation_from_mean(ys)) /( len(xs) - 1)

def correlation(xs: List[float], ys: List[float]) -> float:
    """Measures how much xs and ys vary in tandem about their means"""
    std_dev_x = standard_deviation(xs)
    std_dev_y = standard_deviation(ys)
    if std_dev_x > 0 and std_dev_y > 0  : return covariance(xs, ys) / std_dev_x / std_dev_y
    else                                : return 0
#endregion