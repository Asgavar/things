def sortByHeight(a):
    heights = []
    for person_or_tree in a:
        if not person_or_tree == -1:
            heights.append(person_or_tree)
    heights.sort(reverse=True)
    for index in range(len(a)):
        if not a[index] == -1:
            a[index] = heights.pop()
    return a
