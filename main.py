from random import randint

import numpy as np


class BurkeBinPacking:
    items = []
    start_items_count = 0
    capacity = 10  # Ширина контейнера
    items_heights = [0 for _ in range(capacity)]  # Карта высот полубесконечной ленты

    def init_data(self):
        # self.set_static_items()
        self.generate_items(100, 9)
        self.start_items_count = len(self.items)
        self.items = self.quick_sort(self.items)
        self.capacity = 10

    # Генерация предметов
    def generate_items(self, items_count=100, max_width=capacity, max_height=15, min_width=1, min_height=1):
        if max_width > self.capacity:
            max_width = self.capacity

        for i in range(items_count):
            width = randint(min_width, max_width)
            height = randint(min_height, max_height)
            self.items.append([width, height])

    # Установка конкретных начальных значений
    def set_static_items(self):
        self.items = [
            (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 1), (2, 2), (7, 3), (9, 4), (2, 5),
            (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
            (4, 1), (4, 2), (5, 1), (6, 3), (6, 1),
        ]

    # Быстрая сортировка
    def quick_sort(self, array, increasing=False):
        if len(array) < 2:
            return array

        lower, same, higher = [], [], []
        central_item = array[randint(0, len(array) - 1)]

        for item in array:
            if item[0] < central_item[0]:
                lower.append(item)
            elif item[0] == central_item[0]:
                same.append(item)
            elif item[0] > central_item[0]:
                higher.append(item)

        if increasing:
            return self.quick_sort(lower, increasing) + same + self.quick_sort(higher, increasing)
        else:
            return self.quick_sort(higher, increasing) + same + self.quick_sort(lower, increasing)

    # Поиск самой низкой области
    def get_lower_place(self):
        min_height_index = 0
        place_width = 0
        min_height = self.items_heights[min_height_index]

        current_min_height_index = min_height_index
        current_place_width = place_width
        broken = False

        for index in range(0, self.capacity):
            height = self.items_heights[index]

            if height < min_height:
                min_height = height
                min_height_index = index
                place_width = 1

                current_place_width = place_width
                current_min_height_index = min_height_index
                broken = False
            elif height == min_height:
                if broken:
                    current_min_height_index = index
                    broken = False
                current_place_width += 1

            if place_width < current_place_width:
                place_width = current_place_width
                min_height_index = current_min_height_index

            if height > min_height:
                current_place_width = 0
                broken = True

        return {
            'index': min_height_index,
            'width': place_width
        }

    # Ищем наиболее подходящий предмет, который будет занимать максимальное количество как по ширине, так и по высоте
    def search_best_item(self, lower_place):
        best_item = None
        founded = False

        for index in range(len(self.items)):
            item = self.items[index]
            is_better = False

            if item[0] <= lower_place['width']:
                if not founded:
                    founded = True
                    is_better = True
                    best_item = {
                        'index': index,
                        'width': item[0],
                        'height': item[1],
                    }
                else:
                    if item[0] > best_item['width']:
                        is_better = True
                    elif item[0] == best_item['width'] and item[1] > best_item['height']:
                        is_better = True

                if is_better:
                    best_item = {
                        'index': index,
                        'width': item[0],
                        'height': item[1],
                    }

        if not founded:
            self.fill_lower_place(lower_place)
            return self.search_best_item(self.get_lower_place())

        return best_item

    # Приравнивает высоту нижнего уровня к высоте ближайшего уровня
    def fill_lower_place(self, lower_place):
        difference = self.get_level_height(2) - self.items_heights[lower_place['index']]
        print(self.items_heights)
        print(difference)
        for i in range(lower_place['index'], lower_place['index'] + lower_place['width']):
            self.items_heights[i] += difference
        print(self.items_heights)

    # Возвращает высоту конкретного уровня (1 - минимальный)
    def get_level_height(self, level):
        # Список уникальных значений высот, отсортированный от меньшего к большему
        levels = sorted(list(set(self.items_heights)))
        print('Levels')
        print(levels)
        levels_count = len(levels)

        if levels_count < level:
            print(f"Get level - {level}, but levels count - {levels_count}. Changed to {levels_count}!")
            level = levels_count
        elif level < 1:
            print(f"Get level - {level}, it's less than 1 and changed to 1!")
            level = 1

        return levels[level - 1]

    # Поиск лучшего места для расположения предмета
    # Располагается ближе к более высокому соседу. Если один из соседей — край полосы, то ближе к краю
    def put(self, lower_place, best_item):
        if lower_place['index'] == 0:
            for i in range(best_item['width']):
                self.items_heights[i] += best_item['height']
        elif (lower_place['index'] + lower_place['width']) == self.capacity:
            right_line_end = self.capacity - 1

            for i in range(right_line_end, right_line_end - best_item['width'], -1):
                self.items_heights[i] += best_item['height']
        else:
            place_right_end_index = lower_place['index'] + lower_place['width'] - 1

            # Отдаем предпочтение расположению ближе к левой части полубесконечной полосы
            if self.items_heights[lower_place['index'] - 1] >= self.items_heights[place_right_end_index + 1]:
                for i in range(lower_place['index'], lower_place['index'] + lower_place['width']):
                    self.items_heights[i] += best_item['height']
            else:
                for i in range(place_right_end_index, place_right_end_index - best_item['width'], -1):
                    self.items_heights[i] += best_item['height']

        self.items.pop(best_item['index'])

    # Упаковка
    def packing(self):
        self.init_data()

        for i in range(0, self.start_items_count):
            print(f"Step - {i + 1}")
            # print(f"Items - {self.items}")
            lower_place = self.get_lower_place()
            # print(f"Lower - {lower_place}")
            best_item = self.search_best_item(lower_place)
            # print(f"Best item - {best_item}")
            self.put(lower_place, best_item)
            # print(f"Updated items - {self.items}")

            print(f"Heights - {self.items_heights}")
            print()


if __name__ == '__main__':
    burke = BurkeBinPacking()
    burke.packing()
