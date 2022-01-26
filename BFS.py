import collections


def breadth_first_search(graph, root):
    visited, queue = set(), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

if __name__ == '__main__':
    graph = {1: [2, 4, 5], 2: [3, 6, 7], 3: [], 4: [], 5: [], 6: [], 7: []}
    Tr = list(breadth_first_search(graph, 1))
    print (Tr)