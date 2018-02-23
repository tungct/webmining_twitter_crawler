class Queue:
    def __init__(self):
        self.items = []

    def insert(self, x):
        self.items.append(x)
        return self.items

    def pop(self):
        first =  self.items[0]
        del self.items[0]
        return first