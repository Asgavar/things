from collections import defaultdict

def commonCharacterCount(s1, s2):
    s1_occurences = defaultdict(lambda: 0)
    s2_occurences = defaultdict(lambda: 0)
    for letter in s1:
        s1_occurences[letter] += 1
    for letter in s2:
        s2_occurences[letter] += 1
    common_chars = 0
    for letter in s1_occurences:
        common_chars += min(s1_occurences[letter], s2_occurences[letter])
    return common_chars
