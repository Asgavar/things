def shapeArea(n):
    current_n = n - 1
    total_area = (n * 2) - 1
    while current_n > 0:
        total_area += 2 * ((current_n * 2) - 1)
        current_n -= 1
    return total_area
