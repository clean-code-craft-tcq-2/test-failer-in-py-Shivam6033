def size(cms: int):
    if cms in range(36, 47):
        if cms <= 38:
            return 'S'
        elif 38 < cms <= 40:
            return 'M'
        elif 40 < cms <= 42:
            return 'L'
        elif 42 < cms <= 44:
            return 'XL'
        else:
            return 'XXL'
    return None


assert (size(37) == 'S')
assert (size(40) == 'M')
assert (size(3) is None)
assert (size(434) is None)
assert (size(46) == 'XXL')
assert (size(43) == 'XL')

