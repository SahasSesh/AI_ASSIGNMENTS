import heapq

def dijkstra(graph, start):
    # Initialize distances
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    # Priority queue
    pq = [(0, start)]

    while pq:
        cost, city = heapq.heappop(pq)

        # Skip if already found better path
        if cost > distances[city]:
            continue

        # Explore neighbors
        for neighbor, dist in graph[city]:
            new_cost = cost + dist

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return distances


# Example graph (India cities)
graph = {
    "Delhi": [("Agra", 233), ("Jaipur", 280)],
    "Agra": [("Delhi", 233), ("Lucknow", 335)],
    "Jaipur": [("Delhi", 280), ("Udaipur", 400)],
    "Lucknow": [("Agra", 335)],
    "Udaipur": [("Jaipur", 400)]
}

# Run algorithm
result = dijkstra(graph, "Delhi")

# Print output
for city, dist in result.items():
    print(f"Delhi → {city} : {dist} km")
