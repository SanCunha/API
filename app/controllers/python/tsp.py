import tsp.solverTSP as SolverTSP
# import app.controllers.python.tsp.solverTSP as SolverTSP
import json
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
from sys import maxsize
from random import randint
from random import seed
import datetime
import sys


# importing datetime module for now()
# generate random integer values

# V = 50


class Solver:
    class EdgeTSP:
        def __init__(self, a, b, weight, initial_pheromone):
            self.a = a
            self.b = b
            self.weight = weight
            self.pheromone = initial_pheromone

        def print(self):
            print(self.a)
            print(self.b)
            print(self.weight)
            print("___________________________")

    def __init__(self, nodes, algorithm, iterations, colony_size=10,
                 alpha=1.0, beta=3.0, rho=0.1, pheromone_deposit_weight=1.0, initial_pheromone=1.0) -> None:
        self.cities = nodes
        self.iterations = iterations
        self.algorithm = algorithm
        if algorithm == "TSP":
            self.alpha = alpha
            self.beta = beta
            self.colony_size = colony_size
            self.rho = rho
            self.pheromone_deposit_weight = pheromone_deposit_weight

        self.num_nodes = len(nodes)
        self.nodes = nodes
        self.edges = [[None] * self.num_nodes for _ in range(self.num_nodes)]
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                self.edges[i][j] = self.edges[j][i] = self.EdgeTSP(i, j, math.sqrt(
                    pow(self.nodes[i][0] - self.nodes[j][0], 2.0) + pow(self.nodes[i][1] - self.nodes[j][1], 2.0)),
                    initial_pheromone)

    def returnResult(self, _solution):
        result = _solution.run()
        result["random"] = json.loads(result["random"])
        result["aco"] = json.loads(result["aco"])

        xRandom = []
        yRandom = []
        for i in range(len(result["random"]["route"])):
            xRandom.append(self.nodes[result["random"]["route"][i]][0])
            yRandom.append(self.nodes[result["random"]["route"][i]][1])

        coords = [xRandom, yRandom]

        result["random"]["coords"] = coords
        # print(result)
        xACO = []
        yACO = []
        for i in range(len(result["aco"]["route"])):
            xACO.append(self.nodes[result["aco"]["route"][i]][0])
            yACO.append(self.nodes[result["aco"]["route"][i]][1])

        coords = [xACO, yACO]

        result["aco"]["coords"] = coords

        print(json.dumps(result))

    def execute(self, s=0):

        if self.algorithm == "TSP":
            _solution = SolverTSP.TSP(self.edges, self.iterations, self.colony_size,
                                      self.alpha, self.beta, self.rho, self.pheromone_deposit_weight)
            return self.returnResult(_solution)

    def plot(self):
        plt.scatter(self.route[0], self.route[1])
        for i in range(0, len(self.cities[0])):
            plt.annotate(i, (self.cities[0][i], self.cities[1][i]))
        plt.plot(self.route[0], self.route[1])
        plt.show()


def main():
    _cities = int(sys.argv[1])
    _iterations = int(sys.argv[2])
    _algorithm = sys.argv[3]

    if _algorithm == "TSP":
        _colony_size = int(sys.argv[4])
        _alpha = float(sys.argv[5])
        _beta = float(sys.argv[6])
        _rho = float(sys.argv[7])
        _pheromone_deposit_weight = float(sys.argv[8])

    _nodes = [(random.uniform(0, 100), random.uniform(0, 100))
              for _ in range(0, _cities)]
    acs = Solver(_nodes, _algorithm, _iterations, _colony_size,
                 _alpha, _beta, _rho, _pheromone_deposit_weight)
    acs.execute()

    sys.stdout.flush()


if __name__ == "__main__":
    main()
