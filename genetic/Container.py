from genetic.Config import CONTAINER_WIDTH, CONTAINER_HEIGHT


class Container:
    def __init__(self):
        self.width = CONTAINER_WIDTH
        self.height = CONTAINER_HEIGHT
        self.area = self.width * self.height

        self.items = []
        self.items_count = 0
        self.filled_area = 0

    def add_item(self, item):
        if item.area <= self.area - self.filled_area:
            self.items.append(item)
            self.filled_area += item.area
            self.items_count += 1
            return True

        return False
