from sys import stdin

def points_cover(starts, ends, points):
    events = []
    
    # Add all segment starts and ends
    for i in range(len(starts)):
        events.append((starts[i], 'L'))
        events.append((ends[i], 'R'))
    
    # Add points with index (so we can output in the right order)
    for i, p in enumerate(points):
        events.append((p, 'P', i))

    # Sort events by coordinate, with order: L < P < R
    events.sort(key=lambda x: (x[0], x[1]))

    active = 0
    result = [0] * len(points)

    # Sweep through all events
    for event in events:
        if event[1] == 'L':
            active += 1
        elif event[1] == 'R':
            active -= 1
        else:  # Point event
            _, _, idx = event
            result[idx] = active

    return result


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts = data[2:2 * n + 2:2]
    input_ends = data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
