def dfs_shortest_path(graph, start, end, path=None):
    if path is None:
        path = [start]

    if start == end:
        return path  # Trả về đường đi nếu tìm thấy đích

    shortest_path = None

    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_path = dfs_shortest_path(graph, neighbor, end, path + [neighbor])

            if new_path is not None:
                if shortest_path is None or len(new_path) < len(shortest_path):
                    shortest_path = new_path

    return shortest_path

graph = {
    "LS": ["HB"],
    "QN": ["HP", "HB", "V"],
    "LC": ["ST", "V"],
    "HB": ["HP", "HN","QN","LS"],
    "ST": ["HN","LC"],
    "HP": ["TH","TB","HB", "QN"],
    "TB": ["HN","ND","NB","HP"],
    "HN": ["ND","TB","ST","HB"],
    "ND": ["TB","NB","HN"],
    "NB": ["TH","TB","ND"],
    "TH": ["V","NB"],
    "V": ["LC","TH","QN"],
}

start_node = "HN"
end_node = "V"

shortest_path = dfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print("Đường đi ngắn nhất từ {} đến {}: {}".format(start_node, end_node, shortest_path))
else:
    print("Không có đường đi từ {} đến {}.".format(start_node, end_node))
