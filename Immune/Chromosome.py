class Chromosome:
    def __init__(self, items=None, containers=None, best_containers_count=1, filled_area=0):
        if items is None:
            items = []

        if containers is None:
            containers = []

        self.items = items
        self.filled_area = filled_area

        self.containers = containers
        self.containers_count = len(self.containers)
        self.best_containers_count = best_containers_count

        self.evaluation = 0

    def calculate_evaluation(self):
        if self.containers_count == 1:
            self.evaluation = 100.0
        else:
            self.evaluation = (self.best_containers_count / self.containers_count) * 100

    def add_container(self, container):
        self.containers.append(container)
        self.containers_count += 1
