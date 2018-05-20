def isLucky(n):
    n_str = str(n)
    half_length = len(n_str) // 2
    left_half = n_str[:half_length]
    right_half = n_str[half_length:]
    left_sum = sum(int(digit) for digit in left_half)
    right_sum = sum(int(digit) for digit in right_half)
    return left_sum == right_sum
