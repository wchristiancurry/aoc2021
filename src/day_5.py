def problem1():
    lines = get_input()
    overlap_spots = find_overlap_spots(lines)
    print("problem1 answer: " + str(overlap_spots))

def problem2():
    lines = get_input(consider_diagonal=True)
    overlap_spots = find_overlap_spots(lines)
    print("problem2 answer: " + str(overlap_spots))

def get_input(consider_diagonal=False):
    lines = []
    with open("../input/day5/problem1.in") as f:
        lines_in_file = f.readlines()

        for l in lines_in_file:
            l_split = l.split(" -> ")

            coords_1 = l_split[0].split(",")
            coords_2 = l_split[1].split(",")
            
            line = Line(consider_diagonal, coords_1[0].strip(), coords_1[1].strip(), coords_2[0].strip(), coords_2[1].strip())
            lines.append(line)

    return lines

def find_overlap_spots(lines):
    max_x = -1
    max_y = -1
    for line in lines:
        for point in line.points_covered:
            if point.x > max_x:
                max_x = point.x

            if point.y > max_y:
                max_y = point.y

    max_x += 1
    max_y += 1
    board = [ [0] * max_x for i in range(max_y)]
    for line in lines:
        for point in line.points_covered:
            board[point.y][point.x] += 1

    overlap_spots = 0
    for x in range(max_x):
        for y in range(max_y):
            if board[y][x] >= 2:
                overlap_spots += 1

    return overlap_spots

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
        
class Line():
    def __init__(self, consider_diagonal, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

        self.points_covered = []
        if (self.x1 == self.x2 or self.y1 == self.y2) or consider_diagonal:
            self.points_covered.append(Point(self.x1, self.y1))
            self.points_covered.append(Point(self.x2, self.y2))

            if self.x1 == self.x2:
                min_y = min(self.y1, self.y2)
                max_y = max(self.y1, self.y2)
                for i in range(min_y+1, max_y):
                    self.points_covered.append(Point(self.x1, i))
            elif self.y1 == self.y2:
                min_x = min(self.x1, self.x2)
                max_x = max(self.x1, self.x2)
                for i in range(min_x+1, max_x):
                    self.points_covered.append(Point(i, self.y1))
            else:
                x_diff = abs(self.x1 - self.x2)
                y_diff = abs(self.y1 - self.y2)
                if x_diff == y_diff:
                    if self.x1 == self.y1 and self.x2 == self.y2:
                        min_x = min(self.x1, self.x2)
                        max_x = max(self.x1, self.x2)
                        for i in range(min_x+1, max_x):
                            self.points_covered.append(Point(i, i))
                    else:
                        for i in range(1, x_diff):
                            if self.x1 < self.x2:
                                x = self.x1 + i
                            else:
                                x = self.x1 - i

                            if self.y1 < self.y2:
                                y = self.y1 + i
                            else:
                                y = self.y1 - i

                            self.points_covered.append(Point(x, y))

if __name__ == "__main__":
    problem1()
    problem2()