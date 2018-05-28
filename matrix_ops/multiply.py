def multiple(a, b):
    if a and b and a[0] and b[0]:
        if isinstance(a[0], list):
            num_row_a, num_col_a = len(a), len(a[0])
        else:
            num_row_a, num_col_a = 1, len(a)
            a = [a]
        if isinstance(b[0], list):
            num_row_b, num_col_b = len(b), len(b[0])
        else:
            num_row_b, num_col_b = 1, len(b)
            b = [b]

        if num_col_a != num_row_b:
            raise Exception("the number of columns for the first matrix"
                            "must be equal to the number of rows in the second")
        ret = [[0] * num_col_b for _ in range(num_row_a)]
        for row in range(num_row_a):
            for col in range(num_col_b):
                total = 0
                for i in range(num_col_a):
                    total += a[row][i] * b[i][col]
                ret[row][col] = total
        return ret
    return None
