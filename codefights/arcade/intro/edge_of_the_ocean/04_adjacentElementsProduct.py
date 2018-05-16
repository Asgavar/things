def adjacentElementsProduct(inputArray):
    max_so_far = inputArray[0] * inputArray[1]
    for _ in range(1, len(inputArray) - 1):
        left_product = inputArray[_] * inputArray[_ - 1]
        right_product = inputArray[_] * inputArray[_ + 1]
        larger = max(left_product, right_product)
        print(larger)
        if larger > max_so_far:
            max_so_far = larger
    return max_so_far
