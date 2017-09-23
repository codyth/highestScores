class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next = n

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d
