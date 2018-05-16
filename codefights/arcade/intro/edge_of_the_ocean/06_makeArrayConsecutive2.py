def makeArrayConsecutive2(statues):
    min_statue_number = min(statues)
    max_statue_number = max(statues)
    missing_statues = set(_ for _ in range(min_statue_number, max_statue_number + 1))
    for statue in statues:
        missing_statues.discard(statue)
    return len(missing_statues)
