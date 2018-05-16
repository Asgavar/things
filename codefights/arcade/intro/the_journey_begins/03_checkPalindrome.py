def checkPalindrome(inputString):
    remaining_letters = len(inputString)
    left_side = 0
    right_side = -1
    while remaining_letters > 1:
        if inputString[left_side] != inputString[right_side]:
            return False
        remaining_letters -= 2
        left_side += 1
        right_side -= 1
    return True
