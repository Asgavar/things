def almostIncreasingSequence(sequence):
    throwouts = set()
    for _ in range(len(sequence) - 1):
        if sequence[_] >= sequence[_ + 1]:
            throwouts.add(_)
            throwouts.add(_ + 1)
    if len(throwouts) > 2:
        return False
    bad_index_one = throwouts.pop()
    bad_index_two = throwouts.pop()
    maybe_good_list_one = sequence[:bad_index_one] + sequence[bad_index_one + 1:]
    maybe_good_list_two = sequence[:bad_index_two] + sequence[bad_index_two + 1:]
    return all(maybe_good_list_one[_] < maybe_good_list_one[_ + 1] for _ in range(len(maybe_good_list_one) - 1)) or \
           all(maybe_good_list_two[_] < maybe_good_list_two[_ + 1] for _ in range(len(maybe_good_list_two) - 1))
