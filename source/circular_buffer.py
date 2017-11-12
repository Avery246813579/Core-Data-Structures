class CircularBuffer:
    def __init__(self, size):
        self.nodes = [None] * size
        self.insertion_point = 0
        self.size = size

    def insert(self, data):
        self.nodes[self.insertion_point] = data
        self.insertion_point += 1

        if self.insertion_point >= self.size:
            self.insertion_point = 0

    def values(self):
        return self.nodes

    def get_at_index(self, index):
        return self.nodes[index]

    def __str__(self):
        return str(self.nodes)
