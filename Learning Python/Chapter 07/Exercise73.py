import math
from Exercise72 import *

def test_square_root():
    n = 1
    while n <= 9:
        print(n, square_root(n/2, n), math.sqrt(n), abs(square_root(n/2, n)-math.sqrt(n)))
        n = n+1
        
test_square_root()