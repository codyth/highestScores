from model.Node import Node


def append(d, tail):
    append_node = Node(d)
    tail.set_next(append_node)


def insert(d, left, right):
    insert_node = Node(d, right)
    left.set_next(insert_node)


class LinkedList(object):
    def __init__(self, r=None):
        self.root = r

    def add(self, d):
        add_node = Node(d, self.root)
        self.root = add_node

    def insert_in_descending_order(self, d):
        if self.root is None:
            self.add(d)
        else:
            pointer_node = self.root
            prev_node = None
            while pointer_node:
                if int(pointer_node.get_data()['score']) <= int(d['score']):
                    if prev_node:
                        insert(d, prev_node, pointer_node)
                    else:
                        self.add(d)
                    return
                else:
                    prev_node = pointer_node
                    pointer_node = pointer_node.get_next()
            append(d, prev_node)

    def get_as_list(self):
        ordered_list = []
        pointer_node = self.root
        while pointer_node:
            ordered_list.append(pointer_node.get_data())
            pointer_node = pointer_node.get_next()
        return ordered_list