import heapq
class Graph:
    def __init__ (self):
        self.vertices = {}
    def add_vertex (self, vertex):
        self.vertices[vertex] = {}

    def add_edge (self, start, end, weight):
        self.vertices[start][end] = weight
    def print_graph(self):
        print(f"Các đỉnh của đồ thị là {self.vertices}")
    def dijkstra(self, start, end):
        # Khởi tạo khoảng cách ban đầu và hàng đợi ưu tiên
        distances = {v: float('inf') for v in self.vertices}
        distances[start] = 0
        queue = [(0, start)]
        visited = set()
        previous = {}
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_vertex == end:
                break

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))
        
        path_shortest = []
        current = end
        while current != start:

            path_shortest.insert(0, f'->{current}')
            current = previous[current]
        path_shortest.insert(0,start)

        return path_shortest, distances[end]
    def print_shortest_path(self, start, end):
        path_shortest, shortest_distance = self.dijkstra(start, end)
        print("Đường đi ngắn nhất:", *path_shortest, ':', shortest_distance)
    def print_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            print("Đường đi:", "->".join(path))
        else:
            for neighbor in self.vertices[start]:
                if neighbor not in path:
                    self.print_all_paths(neighbor, end, path)




graph = Graph()
vertices = []
vet = int(input("Bạn muốn bao nhiêu đỉnh?"))
edg = int(input("Bạn muốn bao nhiêu cạnh?"))
print(f"Nhập các cạnh, cách nhau bằng dấu cách và số cuối là trọng số")
for i in range(edg):
    graph.add_vertex(str(i+1))
    edge = input().split()
    graph.add_edge(edge[0],edge[1],int(edge[2]))
print(f"Nhập đỉnh bắt đầu, sau đó là đỉnh kết thúc để tìm tất cả đường đi")
allpath = input().split()
graph.print_all_paths(allpath[0],allpath[1])

print(f"Nhập đỉnh bắt đầu, sau đó là đỉnh kết thúc để tìm đường đi ngắn nhất")
shortest = input().split()
graph.print_shortest_path(shortest[0], shortest[1])

graph.print_graph()