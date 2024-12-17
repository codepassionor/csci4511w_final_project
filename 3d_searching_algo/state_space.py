import random
import math


class CheckpointNode:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
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
    
    def get_z(self):
        return self.z
    
    def distance_to(self, other_node):
        return math.sqrt(
            (self.x - other_node.x)**2 + 
            (self.y - other_node.y)**2 + 
            (self.z - other_node.z)**2
        )
    
    def __repr__(self):
        return f"CheckpointNode(x={self.x}, y={self.y}, z={self.z}, neighbors={len(self.neighbors)})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


class CheckpointGraph:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.checkpoints = {}
        self.checkpoint_locations = [] # amoritized cost of O(1) for choosing random
    
    def generate_unique_checkpoint(self):
        total_possible_locations = self.length * self.width * self.height
        
        if len(self.cities) >= total_possible_locations:
            raise RuntimeError("All possible unique locations have been used.")
        
        while True:
            x = random.randint(0, self.length)
            y = random.randint(0, self.width)
            z = random.randint(0, self.height)
            
            location = (x, y, z)
            
            if location not in self.checkpoints:
                new_node = CheckpointNode(x, y, z)

                if self.checkpoints:
                    random_checkpoint = random.choice(self.checkpoint_locations)

                    self.checkpoints[location] = new_node

                    new_node.add_neighbor(self.checkpoints[random_checkpoint])
                    self.checkpoints[random_checkpoint].add_neighbor(new_node)

                    self.checkpoint_locations.append(location)

                else:
                    self.checkpoints[location] = new_node
                    self.checkpoint_locations.append(location)

                return
            
    def get_checkpoints(self):
        return self.checkpoints
    
    def populate_graph(self, n_checkpoints):
        for _ in range(n_checkpoints):
            self.generate_unique_checkpoint()