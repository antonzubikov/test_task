import math


def find_unique_elements(input_list):
    unique_elements = []

    for num in input_list:
        if input_list.count(num) == 1:
            unique_elements.append(num)

    return unique_elements

# Пример использования функции
input_list = [1, 2, 3, 2, 4, 5, 3, 6]
result = find_unique_elements(input_list)
print(result)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_prime_numbers(minimum, maximum):
    prime_numbers = []

    for num in range(minimum, maximum + 1):
        if is_prime(num):
            prime_numbers.append(num)

    return prime_numbers

# Пример использования функции
min_num = 10
max_num = 30
result = find_prime_numbers(min_num, max_num)
print(result)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance_to_point(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

# Пример использования класса Point
point1 = Point(1, 2)
point2 = Point(4, 6)

print("Координаты точки 1:", point1.get_coordinates())
print("Координаты точки 2:", point2.get_coordinates())

distance = point1.distance_to_point(point2)
print("Расстояние между точками 1 и 2:", distance)

point1.set_coordinates(3, 5)
print("Новые координаты точки 1:", point1.get_coordinates())


def sort_strings_by_length(strings):
    sorted_strings_asc = sorted(strings, key=len)  # Сортировка по возрастанию длины
    sorted_strings_desc = sorted(strings, key=len, reverse=True)  # Сортировка по убыванию длины
    return sorted_strings_asc, sorted_strings_desc

# Пример использования программы
strings = ["apple", "banana", "cherry", "dates", "fig", "grapefruit"]

sorted_asc, sorted_desc = sort_strings_by_length(strings)

print("Список строк, отсортированный по длине в порядке возрастания:")
print(sorted_asc)

print("Список строк, отсортированный по длине в порядке убывания:")
print(sorted_desc)
