def valid(point_1, point_2) -> bool:
    """
    Returns True if line is horizontal or vertical
    """
    x_1, y_1 = point_1
    x_2, y_2 = point_2
    return x_1 == x_2 or y_1 == y_2

def low_to_heigh(v_1, v_2):
    """
    Returns low, high
    """
    if v_1 > v_2:
        return v_2, v_1
    return v_1, v_2


def line(point_1, point_2):
    """
    Returns coords of horizontal or vertical lines
    """
    points = set()
    if not valid(point_1, point_2):
        return points

    x_1, y_1 = point_1
    x_2, y_2 = point_2

    if x_1 == x_2:
        fr, to = low_to_heigh(y_1, y_2)
        points = {(x_1, i) for i in range(fr, to+1)}
    else:
        fr, to = low_to_heigh(x_1, x_2)
        points = {(i, y_1) for i in range(fr, to+1)}

    return points


class Board:
    def __init__(self, height, width):
        self.board = {(x, y): 0 for x in range(height) for y in range(width)}

    def __add__(self, points):
        from_, to = points
        new_points = line(from_, to)
        for point in new_points:
            self.board[point] += 1

        return self


    def dangerous(self, limit=1):
        return len([value for key, value in self.board.items() if value > limit])

def get_points_from_line(line):
    first, second = line.split(" -> ")
    x_1, y_1 = map(int, first.split(","))
    x_2, y_2 = map(int, second.split(","))
    return (x_1, y_1), (x_2, y_2)

with open("input.txt") as f:
    b = Board(1000, 1000)
    for l in f:
        p_1, p_2 = get_points_from_line(l)
        b += (p_1, p_2)

    print(b.dangerous())


