from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            print("Đang xét:", node)
            visited.add(node)
            for neighbor in graph.get(node, []):  # Sử dụng danh sách kề để lấy các đỉnh kề
                if neighbor not in visited:  # Chỉ xét các đỉnh chưa được thăm
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    return None
# graph = {
#     "LS": {"HB"},
#     "QN": {"HP": 15, "HB": 90, "V": 90},
#     "LC": {"ST": 20, "V": 100},
#     "HB": {"HP": 30, "HN": 7},
#     "ST": {"HN": 5},
#     "HP": {"TH": 80,"TB": 10},
#     "TB": {"HN": 15,"ND": 10,"NB": 15},
#     "HN": {"ND": 10},
#     "ND": {"TB": 10,"NB": 15},
#     "NB": {"TH": 25},
#     "TH": {"V": 15},
#     "V": {},
# }

graph = {
    "LS": ["HB"],
    "QN": ["HP", "HB", "V"],
    "LC": ["ST", "V"],
    "HB": ["HP", "HN","QN","LS"],
    "ST": ["HN","LC"],
    "HP": ["TH","TB","HB", "QN"],
    "TB": ["HN","ND","NB","HP"],
    "HN": ["ND","TB","HB","ST"],
    "ND": ["TB","NB","HN"],
    "NB": ["TH","TB","ND"],
    "TH": ["V","NB"],
    "V": ["LC","TH","QN"],
}

start_node = "HN"
end_node = "V"

shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print("Đường đi ngắn nhất từ {} đến {}: {}".format(start_node, end_node, shortest_path))
else:
    print("Không có đường đi từ {} đến {}.".format(start_node, end_node))
