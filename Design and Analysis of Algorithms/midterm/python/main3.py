import time
from collections import defaultdict
from typing import List, Tuple
import random


class AlgoTKUCEP:
    def __init__(self):
        self.startTimestamp = 0
        self.endTimestamp = 0
        self.transactionCount = 0
        self.CUV = 0
        self.K = 0
        self.rho = 0.2
        self.SF = 0.2
        self.sampleSize = 2000
        self.maxIteration = 2000
        self.twuPattern = []
        self.database = []
        self.mapItemToU = {}
        self.mapItemToTWU = {}
        self.samples = []
        self.TopKHuiParticle = []
        self.huiSets = []
        self.p = []

    def runAlgorithm(self, input_file: str, output_file: str, TopK: int):
        self.startTimestamp = time.time()
        self.K = TopK
        self.mapItemToU = defaultdict(int)
        self.mapItemToTWU = defaultdict(int)

        # First pass: Calculate TWU
        with open(input_file, "r") as file:
            for line in file:
                if not line.strip() or line[0] in "#%@":
                    continue

                self.transactionCount += 1
                parts = line.strip().split(":")
                items = list(map(int, parts[0].split()))
                transactionUtility = int(parts[1])
                utilities = list(map(int, parts[2].split()))

                for item, utility in zip(items, utilities):
                    self.mapItemToU[item] += utility
                    self.mapItemToTWU[item] += transactionUtility

        self.calculateCUV()
        self.twuPattern = [
            item for item, twu in self.mapItemToTWU.items() if twu >= self.CUV
        ]

        # Second pass: Create reduced database
        with open(input_file, "r") as file:
            for line in file:
                if not line.strip() or line[0] in "#%@":
                    continue

                parts = line.strip().split(":")
                items = list(map(int, parts[0].split()))
                utilities = list(map(int, parts[2].split()))

                transaction = []
                for item, utility in zip(items, utilities):
                    if item in self.twuPattern:
                        transaction.append((item, utility))
                self.database.append(transaction)

        self.p = [0] * len(self.twuPattern)
        self.generateSample(1.0)

        for _ in range(self.maxIteration):
            self.samples.sort(key=lambda x: -x["fitness"])
            max_min = (
                self.samples[0]["fitness"]
                - self.samples[int(self.rho * self.sampleSize) - 1]["fitness"]
            )
            if max_min == 0:
                break
            proportion = max_min / self.samples[0]["fitness"]
            self.update((1 - self.SF) * proportion)

        self.writeOutput(output_file)
        self.endTimestamp = time.time()
        self.printStats()

    def calculateCUV(self):
        sorted_utilities = sorted(self.mapItemToU.values(), reverse=True)
        self.CUV = sorted_utilities[min(len(sorted_utilities), self.K) - 1]

    def generateSample(self, proportion):
        for _ in range(int(proportion * self.sampleSize)):
            particle = {"bitset": [0] * len(self.twuPattern), "fitness": 0}
            k = random.randint(1, len(self.twuPattern))
            for _ in range(k):
                pos = random.randint(0, len(self.twuPattern) - 1)
                particle["bitset"][pos] = 1
            self.calculateFitness(particle)
            self.samples.append(particle)
            self.updateTopKHui(particle)

    def calculateFitness(self, particle):
        particle["fitness"] = 0
        for transaction in self.database:
            transaction_utility = sum(
                utility
                for (item, utility) in transaction
                if self.twuPattern.index(item)
                in [i for i, bit in enumerate(particle["bitset"]) if bit == 1]
            )
            particle["fitness"] += transaction_utility

    def update(self, proportion):
        num = [0] * len(self.twuPattern)
        for i in range(int(self.rho * self.sampleSize)):
            for j, bit in enumerate(self.samples[i]["bitset"]):
                if bit == 1:
                    num[j] += 1

        self.CUV = self.samples[int(self.rho * self.sampleSize) - 1]["fitness"]
        for i in range(len(self.p)):
            self.p[i] = num[i] / (self.rho * self.sampleSize)

        for _ in range(int(proportion * self.sampleSize)):
            particle = {"bitset": [0] * len(self.twuPattern), "fitness": 0}
            for j in range(len(self.p)):
                if random.random() < self.p[j]:
                    particle["bitset"][j] = 1
            self.calculateFitness(particle)
            if particle["fitness"] > self.CUV:
                self.samples.append(particle)
                self.updateTopKHui(particle)

    def updateTopKHui(self, particle):
        if len(self.TopKHuiParticle) < self.K:
            self.TopKHuiParticle.append(particle)
        else:
            self.TopKHuiParticle.sort(key=lambda x: x["fitness"])
            if particle["fitness"] > self.TopKHuiParticle[0]["fitness"]:
                self.TopKHuiParticle[0] = particle

    def writeOutput(self, output_file):
        with open(output_file, "w") as file:
            for particle in self.TopKHuiParticle:
                itemset = " ".join(
                    str(self.twuPattern[i])
                    for i, bit in enumerate(particle["bitset"])
                    if bit == 1
                )
                file.write(f"{itemset} #UTIL:{particle['fitness']}\n")

    def printStats(self):
        print("============ TKU-CE+ Algorithm ===========")
        print(f"Total time: {self.endTimestamp - self.startTimestamp:.3f} seconds")
        print(f"High-utility itemsets count: {len(self.TopKHuiParticle)}")
        print("==========================================")


if __name__ == "__main__":
    input_file = "DB_Utility.txt"
    output_file = "output.txt"
    algo = AlgoTKUCEP()
    algo.runAlgorithm(input_file, output_file, 3)
