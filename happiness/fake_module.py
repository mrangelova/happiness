import random

HAPPINESS = {
    'grumpy': (0, 2),
    'not happy': (3, 4),
    'somewhat happy': (5, 6),
    'happy': (7, 8),
    'euphoric': (9, 10),
}

def evaluate_happiness(happiness_level):
    for state, limits in HAPPINESS.items():
        if limits[0] <= happiness_level <= limits[1]:
            return HAPPINESS[happiness_level]

def make_happier():
    print """
In every life we have some trouble
But when you worry you make it double
Don't worry, be happy
Don't worry, be happy now
"""
