import random
from Config import MIN_WIDTH, MAX_WIDTH, MIN_HEIGHT, MAX_HEIGHT


class Item:
    def __init__(self, min_width=MIN_WIDTH, max_width=MAX_WIDTH, min_height=MIN_HEIGHT, max_height=MAX_HEIGHT):
        self.width = random.randint(min_width, max_width)
        self.height = random.randint(min_height, max_height)
        self.area = self.width * self.height

    @staticmethod
    def is_equal(first_item, second_item):
        return first_item.width == second_item.width and first_item.height == second_item.height
