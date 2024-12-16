import random
import math


class CityNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []

    def add_neighbor(self, neighbor_node):
        if neighbor_node not in self.neighbors:
            self.neighbors.append(neighbor_node)
    
    def get_neighbors(self):
        return self.neighbors
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __repr__(self):
        return f"CityNode(x={self.x}, y={self.y}, neighbors={len(self.neighbors)})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class CityGraph:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cities = {}
        self.city_locations = [] # amoritized cost of O(1) for choosing random
    
    def generate_unique_city(self):
        total_possible_locations = self.width * self.height
        
        if len(self.cities) >= total_possible_locations:
            raise RuntimeError("All possible unique locations have been used.")
        
        while True:
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            
            location = (x, y)
            
            if location not in self.cities:
                new_node = CityNode(x, y)

                if self.cities:
                    random_city = random.choice(self.city_locations)

                    self.cities[location] = new_node

                    new_node.add_neighbor(self.cities[random_city])
                    self.cities[random_city].add_neighbor(new_node)

                    self.city_locations.append(location)

                else:
                    self.cities[location] = new_node
                    self.city_locations.append(location)

                return
            
    def get_cities(self):
        return self.cities
    
    def populate_graph(self, n_cities):
        for _ in range(n_cities):
            self.generate_unique_city()

# # TEST GRAPH CODE
# city_graph = CityGraph(1000, 1000)
# city_graph.generate_unique_city()
# print(city_graph.get_cities())        # one city with 0 neighbors
# city_graph.generate_unique_city()
# print(city_graph.get_cities())        # two cities with 1 neighbor each
# city_graph.generate_unique_city()
# print(city_graph.get_cities())        # three cities, two 1 neighbors, one 2 neighbor

# # POPULATE 10000x10000 WITH 1000 CITIES
# city_graph_2 = CityGraph(10000, 10000)
# city_graph_2.populate_graph(1000)
# cities = city_graph_2.get_cities()
# print(len(cities))

# # FIND CITY (NODE) WITH MOST NEIGHBORS
# max_neighbors = 0
# max_node = None
# for c in cities.values():
#     neighbors = len(c.get_neighbors())
#     if neighbors > max_neighbors:
#         max_neighbors = neighbors
#         max_node = c
# print(max_node)

