#!/usr/bin/env python3

# --- Imports -------
import math
import random
import statistics
import keyword

# -------------------

# Math Import
print(math.pow(2,3))
print()

# Random Import
print(random.randint(0,100))
print()

# Statistics Import
# mean
nums = [1,5,33,12,46,33,2]
print(statistics.mean(nums))
print()

# median
print(statistics.median(nums))
print()

# mode
print(statistics.mode(nums))
print()

# Keyword Import
print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))
