from sys import maxsize
import random
import json


# class SolveTSPUsingRandom(cities, iterations, matrixDistance, coords, s=0):
class SolveTSPUsingRandom():
    def __init__(self, edges, iterations, labels=None, s=0):
        self.edges = edges
        self.iterations = iterations
        self.num_nodes = len(self.edges)
        self.global_best_tour = []
        self.global_best_distance = maxsize
        if labels is not None:
            self.labels = labels
        else:
            self.labels = range(1, self.num_nodes + 1)
        self.result = {}

    def get_distance(self, route):
        distance = 0.0
        for i in range(self.num_nodes):
            distance += self.edges[route[i]
                                   ][route[(i + 1) % self.num_nodes]].weight
        return distance

    def run(self):
        # print('Started : {0}'.format("Random"))
        logs = []
        for _ in range(0, self.iterations):
            vertex = list(range(0, len(self.edges)))
            vertex = sorted(vertex, key=lambda k: random.random())
            vertex.append(vertex[0])

            current_pathweight = self.get_distance(vertex)

            if current_pathweight < self.global_best_distance:
                self.global_best_distance = current_pathweight
                self.global_best_tour = vertex

            if _ % 5 == 0:
                logs.append({
                    "iteration": _,
                    "route": self.global_best_tour,
                    "value": self.global_best_distance
                })

        # print('Sequence : <- {0} ->'.format(' - '.join(
        #     str(self.labels[i]) for i in self.global_best_tour)))
        # print('Total distance travelled to complete the tour : {0}'.format(
        #     round(self.global_best_distance, 2)))
        # print('Ended : {0}\n'.format("Random"))

        return json.dumps({
            "route": self.global_best_tour,
            "value": self.global_best_distance,
            "logs": logs
        })
