import math
import random
import sys
from Container import Container
from Chromosome import Chromosome
from Item import Item
from Config import *


class ImmunePacking:
    def __init__(self):
        self.populations_count = POPULATIONS_COUNT
        self.items_count = ITEMS_COUNT
        self.select = SELECT
        # self.mutation_chance = MUTATION_CHANCE
        self.iterations_count = ITERATIONS_COUNT
        self.container_width = CONTAINER_WIDTH
        self.container_height = CONTAINER_HEIGHT

        self.population = []
        self.items = []
        self.items_dict = {}

        self.filled_area = 0
        self.best_containers_count = 0

    def quick_sort_by_eval(self, array=None, increasing=False):
        if array is None:
            array = self.population

        if len(array) < 2:
            return array

        lower, same, higher = [], [], []
        central_chromosome = array[random.randint(0, len(array) - 1)]

        for chromosome in array:
            if chromosome.evaluation < central_chromosome.evaluation:
                lower.append(chromosome)
            elif chromosome.evaluation == central_chromosome.evaluation:
                same.append(chromosome)
            elif chromosome.evaluation > central_chromosome.evaluation:
                higher.append(chromosome)

        if increasing:
            return self.quick_sort_by_eval(lower, increasing) + same + self.quick_sort_by_eval(higher, increasing)
        else:
            return self.quick_sort_by_eval(higher, increasing) + same + self.quick_sort_by_eval(lower, increasing)

    def generate_items(self):
        for _ in range(self.items_count):
            item = Item()
            self.items.append(item)
            self.filled_area += item.area

            key_exists = False if self.items_dict.get(f"[{item.width}, {item.height}]") is None else True
            self.items_dict.update({
                f"[{item.width}, {item.height}]":
                    self.items_dict.get(f"[{item.width}, {item.height}]") + 1 if key_exists else 1
            })

        self.best_containers_count = math.ceil(self.filled_area / (CONTAINER_WIDTH * CONTAINER_HEIGHT))

    def init_population(self):
        self.generate_items()

        for _ in range(self.populations_count):
            chromosome = self.pack(self.items)
            self.population.append(chromosome)
            random.shuffle(self.items)

    def pack(self, items):
        chromosome = Chromosome(items=items, best_containers_count=self.best_containers_count,
                                filled_area=self.filled_area)
        container = Container()

        for item in items:
            if not container.add_item(item):
                chromosome.add_container(container)
                container = Container()

                if not container.add_item(item):
                    sys.exit('Item area more than empty container area')

        chromosome.add_container(container)
        chromosome.calculate_evaluation()

        # for i in self.population:
        # for item in chromosome.items:
        #     print(f"[{item.width}, {item.height}]")
        # print('Init end -------------------------')

        return chromosome

    def selection(self):
        self.population = self.quick_sort_by_eval()[:int(self.populations_count * self.select)]

    def clone(self, original_items):
        for i in range(CLONE_COUNT):
            clone = self.pack(original_items)

            # if random.random() <= self.mutation_chance:
            clone = self.mutation(clone)
            # Repack
            clone = self.pack(clone.items)

            self.population.append(clone)

        self.population = self.quick_sort_by_eval()[0:self.populations_count]

    def mutation(self, chromosome):
        mutation_index = random.randint(1, 3)

        if mutation_index == 1:
            # print(f"Mutation 1")
            ids = random.sample(range(self.items_count), 2)
            chromosome.items[ids[0]], chromosome.items[ids[1]] = chromosome.items[ids[1]], chromosome.items[ids[0]]
        elif mutation_index == 2:
            # print(f"Mutation 2")
            middle = self.items_count // 2
            chromosome.items = chromosome.items[middle:self.items_count] + chromosome.items[0:middle]
        elif mutation_index == 3:
            # print(f"Mutation 3")
            random.shuffle(chromosome.items)

        return chromosome

    def start(self):
        first_best = self.population[0]

        num = 0
        # while True:
        for _ in range(self.iterations_count):
            num += 1
            print(f"Iteration - {num}")
            if self.population[0].evaluation >= 100.0:
                break

            self.selection()
            print(self.population[0].evaluation)
            print('-------------------------')

            random_chromosome_index = random.randint(0, len(self.population) - 1)

            self.clone(self.population[random_chromosome_index].items)

        print('The first best population:')
        print(first_best.evaluation)

        print('The best population now:')
        print(self.population[0].evaluation)

        print('Updated on:')
        print(self.population[0].evaluation - first_best.evaluation)
