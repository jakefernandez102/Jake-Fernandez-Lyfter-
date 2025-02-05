class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Bus:
    def __init__(self, capacity, passengers=None):
        self.capacity = capacity
        self.passengers = passengers if passengers is not None else []

    def add_passenger(self, person):
        if(len(self.passengers) < self.capacity):
            self.passengers.append(person)
            return True
        else:
            print("No hay espacio")
            return False

    def remove_passegenger(self, passenger):
        return self.passengers.remove(passenger)

    def get_passengers(self):
        passengers = []
        for passenger in self.passengers:
            passengers.append(passenger.name)
        return passengers


person1 = Person("Juan", 20)
person2 = Person("Pedro", 30)
person3 = Person("Maria", 40)

bus = Bus(2,[])
bus.add_passenger(person1)
print(bus.get_passengers())

bus.add_passenger(person2)
print(bus.get_passengers())

bus.add_passenger(person3)
print(bus.get_passengers())

print(bus.remove_passegenger(person1))
print(bus.get_passengers())
