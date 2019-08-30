# Given an array of integers, return a new array such
# that each element at index i
# of the new array is the product of all the numbers
# in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

import math


def mul_except(xs):
    product = 1.0
    for x in xs:
        product *= x

    ys = []
    for x in xs:
        ys.append(int(product // x))

    return ys


def mul_except_without_division(xs):
    product = 1.0
    for x in xs:
        product *= x
    product = math.log(product)

    ys = []
    for x in xs:
        ys.append(round(math.exp(product - math.log(x))))

    return ys


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5]
    print(f'mul_except({test}) is ' f'{mul_except(test)}')
    print(f'mul_except_without_division({test}) is '
          f'{mul_except_without_division(test)}')
