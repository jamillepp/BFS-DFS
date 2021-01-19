from Node import Node

def convert(G, rootId):

    nodes = G[0]
    edges = G[1]

    for i in range(len(nodes)):

        nodes[i] = Node(nodes[i])

        if i == rootId:

            root = nodes[i]
            root.dist = 0
            root.parent = Node(None)

        for j in range(len(edges)):

            if nodes[i].id in edges[j]:

                if edges[j].index(nodes[i].id) == 0:

                    nodes[i].adj.append( edges[j][1] )
                else:
                    nodes[i].adj.append( edges[j][0] )

    return (nodes, root)