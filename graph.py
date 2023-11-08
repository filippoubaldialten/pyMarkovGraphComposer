"""
Implemented Markov Chain Composer Graph object by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random

class Vertex(object):
    def __init__(self, value):
        self.value = value  # value == words!
        self.adjacent = {}  # nodes that it points to:
        # it's a dict like {word_a: weight_a, word_b: weight_b}
        # the weights are RESPECT TO the node (value)
        # any instance of Vertex will have its adjacents
        self.neighbors = []  # usato dalla mappa di probabilità
        self.neighbors_weights = []

    def __str__(self):
        return self.value + ' '.join([node.value for node in self.adjacent.keys()])

    def add_edge_to(self, vertex, weight=0):
        # adjacent is a dict and vertex is the key (a word in our case)
        # vertex is a vertex adjacent to "vertex value"
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        # increment by one of weight of a "vertex" adjacent to "value"
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        # returns the words adjacent to Vertex(value), they are the keys of a dict
        return self.adjacent.keys()

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        # qui sto scegliendo la parola successiva da inserire nel mio testo
        # prodotto in output (scelta random dei vicini pesata sui weight)
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]



class Graph(object):
    def __init__(self):
        # the dict containing all words of our text
        self.vertices = {} # NON HO CAPITO COM'È FATTO QUESTO, COSA C'È AL SECONDO
        # POSTO DELLA COPPIA DEL DIZIONARIO?

    def get_vertex_values(self):
        # banally get the set of all words (the keys of the dict "vertices")
        # QUINDI IL GRAPH HA TUTTI I VERTICI MENTRE I VERTEX HANNO OGNUNO
        # I PROPRI ADJACENTS
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        #
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
