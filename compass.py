def direction(facing, turn):
    directions = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    if abs(turn) > 1080:
        raise ValueError('Turn can\'t be more then 1080 or less then 1080')
    if turn % 45 != 0:
        raise ValueError('Turn should be divisible by 45')
    if facing not in directions:
        raise ValueError(f'Facing should be equal to one of this: '
                         f'{" ".join(directions)}. Instead it is equal to {facing}')
    result_index = (directions.index(facing) + (turn // 45)) % len(directions)
    return directions[result_index]

