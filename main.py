# This is a sample Python script to show polygon density.

from queue import PriorityQueue


class Design:

    def __init__(self, data) -> None:
        self.parse(data)

    def parse(self, d):
        self.left_bottom_x = int(d[1])
        self.left_bottom_y = int(d[2])
        self.right_top_x = int(d[3])
        self.right_top_y = int(d[4])
        self.polygon_num = int(d[5])
        self.area = (self.right_top_x - self.left_bottom_x) * (self.right_top_y - self.left_bottom_y)
        self.density = self.polygon_num * 1e6 / self.area
        self.name = d[0]
        self.md5 = d[6]

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.density > other.density


class Library:

    def __init__(self, path):
        self.path = path
        self.data = PriorityQueue()

    def output(self):
        while not self.data.empty():
            print(self.data.get())

    def load(self):
        with open(self.path, "r") as f:
            header = f.readline()
            print("Header:", header)
            data = f.read().split("\n")
            for i in data:
                d = i.split("\t")
                if len(d) < 7:
                    continue
                self.data.put(Design(d))


def main():
    library = Library("./testdata.txt")
    library.load()
    library.output()


if __name__ == '__main__':
    main()
