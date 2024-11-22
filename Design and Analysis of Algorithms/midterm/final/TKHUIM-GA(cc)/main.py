import random


class GeneticAlgorithm:
    def __init__(self, dataset, population_size, max_generations, top_k):
        self.dataset = dataset
        self.population_size = population_size
        self.max_generations = max_generations
        self.top_k = top_k

    def initialize_population(self):
        return [
            random.sample(self.dataset, random.randint(1, len(self.dataset)))
            for _ in range(self.population_size)
        ]

    def fitness_function(self, individual):
        return sum(item["utility"] for item in individual if item in self.dataset)

    def select_parents(self, population, fitness_scores):
        return random.choices(population, weights=fitness_scores, k=2)

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, min(len(parent1), len(parent2)) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, individual):
        if random.random() < 0.1:
            mutation_index = random.randint(0, len(individual) - 1)
            new_item = random.choice(self.dataset)
            individual[mutation_index] = new_item
        return individual

    def run(self):
        population = self.initialize_population()
        best_solutions = []
        for generation in range(self.max_generations):
            fitness_scores = [self.fitness_function(ind) for ind in population]
            next_generation = []
            for _ in range(self.population_size // 2):
                parent1, parent2 = self.select_parents(population, fitness_scores)
                child1, child2 = self.crossover(parent1, parent2)
                next_generation.extend([self.mutate(child1), self.mutate(child2)])
            population = next_generation
            best_solutions.extend(
                sorted(population, key=self.fitness_function, reverse=True)[
                    : self.top_k
                ]
            )
        return sorted(best_solutions, key=self.fitness_function, reverse=True)[
            : self.top_k
        ]


# Example usage:
dataset = [
    {"item": "a", "utility": 10},
    {"item": "b", "utility": 20},
    {"item": "c", "utility": 5},
]
ga = GeneticAlgorithm(dataset, population_size=10, max_generations=50, top_k=5)
top_k_solutions = ga.run()

print("Top-K High Utility Itemsets:", top_k_solutions)
