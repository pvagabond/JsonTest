from matrix_ops import multiply
import math


def frobenius_norm(a):
    if a:
        a = map(lambda x: x * x, a)
        return math.sqrt(sum(a))
    return None


def flatten_list(l):
    flat_list = [item for sublist in l for item in sublist]
    return flat_list


def mean_squared_error(a, b):
    if a and b and isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        total = 0
        for index in range(len(a)):
            total += a[index] * a[index] - b[index] * b[index]
        return math.sqrt(total)
    raise Exception("Invalid input")


def main():
    a = [1, 2]
    b = [[3, 4], [4, 6]]
    while True:
        c = multiply.multiple(a, b)
        c = flatten_list(c)
        fn = frobenius_norm(c)
        c = list(map(lambda x: x / fn, c))
        mqe = mean_squared_error(a, c)
        if mqe < 0.001:
            break
        a = c
    print(a)


if __name__ == '__main__':
    main()
