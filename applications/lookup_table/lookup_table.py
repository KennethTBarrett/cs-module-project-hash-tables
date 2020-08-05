import math
import random
import time

# def slowfun_too_slow(x, y):
#     v = math.pow(x, y)
#     v = math.factorial(v)
#     v //= (x + y)
#     v %= 982451653

#     return v

# Empty dict to populate.
cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # If entry doesn't exist...
    if (x, y) not in cache:
        # Make same calculations
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        # Store in cache.
        cache[x, y] = v
        # Doing this will allow for values to be stored in the dictionary
        # for quicker access with values already known.
    return cache[(x, y)]


# Do not modify below this line!

start = time.time()
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
print("Execution time:", time.time() - start)