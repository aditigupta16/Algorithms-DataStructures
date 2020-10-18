


def depth_first_traversal(graph, node, visited):

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph[node]:
            depth_first_traversal(graph, neighbour, visited)


if __name__ == '__main__':

    graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
    }

    visited = set()
    depth_first_traversal(graph, 'A', visited)
