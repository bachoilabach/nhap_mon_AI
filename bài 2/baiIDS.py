def dfs(graph, node, end_node, visited, path):
    if node == end_node:
        path.append(node)
        return True

    visited.add(node)
    path.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, end_node, visited, path):
                return True

    path.pop()
    return False

def ids_shortest_path(graph, start, end):
    for depth in range(len(graph)):
        visited = set()
        path = []
        if dfs(graph, start, end, visited, path):
            return path
    return None

graph = {
    "LS": ["HB"],
    "QN": ["HP", "HB", "V"],
    "LC": ["ST", "V"],
    "HB": ["HP", "HN", "QN", "LS"],
    "ST": ["HN", "LC"],
    "HP": ["TH", "TB", "HB", "QN"],
    "TB": ["HN", "ND", "NB", "HP"],
    "HN": ["ND", "TB", "HB", "ST"],
    "ND": ["TB", "NB", "HN"],
    "NB": ["TH", "TB", "ND"],
    "TH": ["V", "NB"],
    "V": ["LC", "TH", "QN"],
}

start_node = "HN"
end_node = "V"

shortest_path = ids_shortest_path(graph, start_node, end_node)

if shortest_path:
    print("Đường đi ngắn nhất từ {} đến {}: {}".format(start_node, end_node, shortest_path))
else:
    print("Không có đường đi từ {} đến {}.".format(start_node, end_node))
