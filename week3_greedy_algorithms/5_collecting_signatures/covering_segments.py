from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # sort segments by end
    segments.sort(key=lambda s: s.end)

    # pick the end of the first segment
    current_point = segments[0].end
    points.append(current_point)

    for s in segments:
        # if the current point doesn't cover this segment
        if not (s.start <= current_point <= s.end):
            current_point = s.end
            points.append(current_point)

    return points


if __name__ == '__main__':
    input_data = stdin.read()
    n, *data = map(int, input_data.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

