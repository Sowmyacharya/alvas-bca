import sys
def nearest_neighbour(graph,start_city):
    num_cities=len(graph)
    visited=[False]*num_cities
    tour=[start_city]
    total_cost=0
    visited[start_city]=True
    for _ in range(num_cities-1):
        current_city=tour[-1]
        nearest_city=None
        min_distance=sys.maxsize
        for next_city in range(num_cities):
            if not visited[next_city] and graph[current_city][next_city]<min_distance:
                nearest_city=next_city
                min_distance=graph[current_city][next_city]
    visited[nearest_city]=True
    tour.append(nearest_city)
    total_cost+=min_distance
    tour.append(start_city)
    total_cost+=graph[tour[-2]][start_city]
    return tour,total_cost
num_cities=int(input("Enter the number of cities:"))
start_city=int(input(f"Enter the starting city(0 to {num_cities-1}):"))
graph=[]
print("Enter the cost matrix:")
for i in range(num_cities):
    row=list(map(int,input(f"Enter the cost of city {i}:").split()))
    graph.append(row)
optimal_tour,min_cost=nearest_neighbour(graph,start_city)
print(f"Optimal tour:{optimal_tour}")
print(f"Minimum cost:{min_cost}")         
