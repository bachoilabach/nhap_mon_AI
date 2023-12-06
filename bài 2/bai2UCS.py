import queue

def ucs_shortest_path(graph, start, end):
    # Tạo một hàng đợi ưu tiên (Priority Queue) để duyệt các đỉnh theo chi phí tối ưu
    pq = queue.PriorityQueue()
    pq.put((0, [start]))  # Đưa đỉnh ban đầu vào hàng đợi với chi phí 0

    while not pq.empty():
        cost, path = pq.get()
        node = path[-1]

        if node == end:
            return path  # Trả về đường đi nếu tìm thấy đích

        for neighbor, edge_cost in graph.get(node, {}).items():
            if neighbor not in path:
                new_cost = cost + edge_cost
                new_path = list(path)
                new_path.append(neighbor)
                pq.put((new_cost, new_path))

    return None  # Trả về None nếu không tìm thấy đường đi

graph = {
    "LS": {"HB": 17},
    "QN": {"HP": 15, "HB": 90, "V": 90},
    "LC": {"ST": 90, "V": 100},
    "HB": {"HP": 30, "HN": 7,"QN": 90,"LS": 17},
    "ST": {"HN": 5,"LC": 20},
    "HP": {"TH": 80,"TB": 10,"HB": 30, "QN": 15},
    "TB": {"HN": 15,"ND": 10,"NB": 15,"HP":10},
    "HN": {"ND": 10,"TB": 15,"HB": 7,"ST": 5},
    "ND": {"TB": 10,"NB": 15,"HN": 10},
    "NB": {"TH": 25,"TB": 15,"ND": 15},
    "TH": {"V": 15,"NB": 25},
    "V": {"LC": 100,"TH": 15,"QN":  90},
}


start_node = "HN"
end_node = "V"

shortest_path = ucs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print("Đường đi ngắn nhất từ {} đến {}: {}".format(start_node, end_node, shortest_path))
else:
    print("Không có đường đi từ {} đến {}.".format(start_node, end_node))
