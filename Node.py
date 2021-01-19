class Node:

    def __init__(self, id):

        self.id = id
        self.dist = -1
        self.parent = None
        self.color = "w"
        self.adj = []

    def __repr__(self):

        return "<Label: {}, Color: {} Parent: {}, Distance: {}>".format(self.id, self.color, self.parent.id, self.dist)