import random

def generate_random_list(length, negative=False, dispersion=100000, range_start=1, range_end=100000, float_numbers=False):
    if float_numbers:
        return [random.uniform(range_start, range_end) for _ in range(length)]
    elif negative:
        return [random.randint(-dispersion, dispersion) for _ in range(length)]
    else:
        return [random.randint(range_start, range_end) for _ in range(length)]

List_1 = generate_random_list(100, dispersion=1000)
List_2 = generate_random_list(5000, dispersion=1000)
List_3 = generate_random_list(100000, dispersion=100)
List_4 = generate_random_list(100000, dispersion=1000000)
List_5 = generate_random_list(5000, negative=True, dispersion=1000)
List_6 = generate_random_list(100000, negative=True, range_end=100)
List_7 = generate_random_list(100, float_numbers=True, range_end=1000)
List_8 = generate_random_list(100000, float_numbers=True, range_end=100)
List_9 = generate_random_list(100000, float_numbers=True, range_end=1000000)

#print(List_7)

import random

def generate_random_list(length, negative=False, dispersion=100000, range_start=1, range_end=100000, float_numbers=False):
    if negative:
        return [random.randint(-dispersion, -1) for _ in range(length)]
    else:
        return [random.randint(range_start, range_end) for _ in range(length)]

# Create a list containing only negative numbers
List_10 = generate_random_list(1000, float_numbers=True, negative=True, range_end=1000)
List_11 = generate_random_list(1000, negative=True, dispersion=1000)
List_12 = generate_random_list(100000, negative=True, dispersion=1000)
