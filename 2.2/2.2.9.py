class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.path = list(args)

    def get_path(self):
        return self.path

    def get_length(self):
        length = 0
        prev = LineTo(0, 0)
        for dot in self.path:
            length += ((dot.x - prev.x)**2 + (dot.y - prev.y)**2)**0.5
            prev = dot
        return length

    def add_line(self, line):
        self.path.append(line)
