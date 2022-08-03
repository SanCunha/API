import tsp.acoTSP as acoTSP
import tsp.randomTSP as randomTSP


class TSP:
    def __init__(self, edges, iterations, colony_size, alpha, beta, rho, pheromone_deposit_weight):
        self.aco = acoTSP.SolveTSPUsingACO(edges, iterations, colony_size, alpha, beta,
                                           rho, pheromone_deposit_weight)
        self.random = randomTSP.SolveTSPUsingRandom(edges, iterations)
        self.result = {}

    def run(self):
        return {
            "random": self.random.run(),
            "aco": self.aco.run()
        }
