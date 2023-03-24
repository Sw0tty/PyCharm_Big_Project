class Room:
    def get_room(self):
        print('room')


class Room1(Room):
    def get_room(self):
        print('room1')


class Room2(Room):
    def get_room(self):
        print('room2')


class Flat(Room1, Room2):
    pass


print(Flat.mro())  # метод класса, который показывает порядок наследования

f = Flat()
f.get_room()

print()

class Room11:
    def get_room(self):
        print('room1')


class Room2:
    def get_room(self):
        print('room2')

    def get_room2(self):
        print('room2 for flat')


class Kitchen:
    def get_kitchen(self):
        print('kitchen')


class Flat(Kitchen, Room11, Room2):
    pass


my_flat = Flat()
my_flat.get_kitchen()
my_flat.get_room()
my_flat.get_room2()
print(isinstance(my_flat, Flat))
print(isinstance(my_flat, Room11))
print(isinstance(my_flat, Room2))
