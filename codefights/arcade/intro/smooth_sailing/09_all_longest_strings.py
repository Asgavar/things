def allLongestStrings(inputArray):
    longest_strings = []
    current_longest_length = 0
    for word in inputArray:
        word_length = len(word)
        if word_length == current_longest_length:
            longest_strings.append(word)
        if word_length > current_longest_length:
            current_longest_length = word_length
            longest_strings.clear()
            longest_strings.append(word)
    return longest_strings
