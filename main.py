# Coffee Machine
class CoffeeMachine:
    def __init__(self, water_level, coffe_level, milk_level, sugar_level, cups):
        self.water_level = water_level
        self.coffe_level = coffe_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.cups = cups

    def add_water(self, amount):
        self.water_level += amount

    def add_coffee(self, amount):
        self.coffe_level += amount

    def add_milk(self, amount):
        self.milk_level += amount

    def add_sugar(self, amount):
        self.sugar_level += amount

    def add_cups(self, amount):
        self.cups += amount

    def check_resources(self):
        if self.water_level > 0 and self.coffe_level > 0 and self.milk_level > 0 and self.sugar_level > 0 and self.cups > 0:
            return True
        return False

    def make_coffe(self):
        if self.check_resources():
            self.water_level -= 1
            self.coffe_level -= 1
            self.milk_level -= 1
            self.sugar_level -= 1
            self.cups -= 1
            print('Кофе готов')
        else:
            print('Недостаточно ингредиентов')

# Camera
class PhotoCamera:
    def __init__(self, brand, model, resolution, memory_capacity, is_on=False, photos=[]):
        self.brand = brand
        self.model = model
        self.resolution = resolution
        self.is_on = is_on
        self.memory_capacity = memory_capacity
        self.photos = photos

    def take_photo(self):
        print(f'Сделана фотография с разрешением {self.resolution[0]}x{self.resolution[1]}')

    def get_camera_info(self):
        print(f'Марка: {self.brand}, Модель: {self.model}, Разрешение: {self.resolution[0]}x{self.resolution[1]}')

    def turn_on(self):
        self.is_on = True
        print('Фотокамера включена')

    def turn_off(self):
        self.is_on = False
        print('Фотокамера выключена')

    def is_camera_on(self):
        return self.is_on

    def store_photo(self, photo):
        if len(self.photos) < self.memory_capacity:
            self.photos.append(photo)
            return True
        return False

    def view_photos(self):
        print(self.photos)

    def clear_memory(self):
        self.photos = []

# Revolver
import random

class Revolver():
    def __init__(self, indicator, capacity=6, barrel=[None]*6):
        self.indicator = indicator
        self.capacity = capacity
        self.barrel = barrel

    def add_bullet(self, bullet):
        for i in range(self.indicator, self.indicator + self.capacity + 1):
            cell = i % self.capacity
            if self.barrel[cell] is None:
                self.barrel[cell] = bullet
                return True
        return False

    def add_bullets_from_list(self, list):
        counter = 0
        # j = indicator of bullets in list
        for j in list:
            if self.add_bullet(j):
                counter += 1
        return counter > 0

    def shoot(self):
        bullet = self.barrel[self.indicator]
        if bullet is None:
            return None

    def unload(self, all_items=False):
        if all_items == False:
            bullet = self.barrel[self.indicator - 1]
            self.barrel[self.indicator - 1] = None
            return bullet
        else:
            not_all_items = [x for x in self.barrel if x is not None]
            self.barrel = [None] * self.capacity
            return not_all_items

    def bullet_count(self):
        return len([1 for i in self.barrel if i is not None])

    def scroll(self):
        self.indicator = random.randint(0, self.capacity)

arg = Revolver(2)

arg.add_bullets_from_list([2, 3, 4, 5, 6])
print(arg.barrel)

n = arg.add_bullet(1)
print(arg.barrel)

k = arg.bullet_count()
print(k)

b = arg.shoot()
print(b)

arg.scroll()
print(arg.indicator)

unloadd = arg.unload()
print(unloadd)

print(arg.barrel)

