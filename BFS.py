from convertToNode import convert

def BFS( G, rootId ):

    (nodes, root) = convert(G, rootId)

    queue = []

    queue.append( root )

    while len(queue) != 0:

        u = queue.pop(0)

        for num in u.adj:

            v = nodes[num]

            if v.color == "w":

                v.color = "g"
                v.dist = u.dist + 1
                v.parent = u
                queue.append(v)

        u.color = "b"

    return nodes
