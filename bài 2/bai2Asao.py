import queue

# Hàm heuristic h(n) là khoảng cách theo đường chim bay từ tỉnh n đến V
heuristic = {
    "HN": 50,
    "ST": 60,
    "LC": 75,
    "HB": 65,
    "LS": 70,
    "HP": 80,
    "QN": 80,
    "TB": 55,
    "ND": 45,
    "NB": 20,
    "TH": 15,
    "V": 0
}

def a_star_shortest_path(graph, start, end, heuristic):
    open_set = queue.PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    while not open_set.empty():
        _, current = open_set.get()
        
        if current == end:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)
            return path
        
        for neighbor, edge_cost in graph.get(current, {}).items():
            tentative_g_score = g_score[current] + edge_cost
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = g_score[neighbor] + heuristic[neighbor]
                open_set.put((f_score, neighbor))
                came_from[neighbor] = current
    
    return None

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

shortest_path = a_star_shortest_path(graph, start_node, end_node, heuristic)

if shortest_path:
    print("Đường đi ngắn nhất từ {} đến {}: {}".format(start_node, end_node, shortest_path))
else:
    print("Không có đường đi từ {} đến {}.".format(start_node, end_node))
