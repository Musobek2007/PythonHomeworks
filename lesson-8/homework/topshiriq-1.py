class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(f'{self.name}is eating.')
    def walk(self):
        print(f'{self.name}is walking.')
    def sleep(self):
        print(f'{self.name}is sleeping.')
    def make_sound(self):
        print(f'{self.name}is running.')
class Cow(Animal):
    def __init__(self,name,age,milk):
        super().__init__(name,age)
        self.milk=milk
    def make_sound(self):
        print(f'{self.name} says Moo!')
    def produce(self):
        print('f{self.name} produces {self.milk} liters of milk per day.')
class Chicken(Animal):
    def __init__(self,name,age,egg_count):
        super().__init__(name,age)
        self.egg_count=egg_count  # eggs per week
    def make_sound(self):
        print(f"{self.name} says Cluck!")
    def produce(self):
        print(f"{self.name} lays {self.egg_count} eggs per week.")
class Sheep(Animal):
    def __init__(self,name,age,wool_quantity):
        super().__init__(name, age)
        self.wool_quantity=wool_quantity  # kg per shearing
    def make_sound(self):
        print(f"{self.name} says Baa!")
    def produce(self):
        print(f"{self.name} provides {self.wool_quantity} kg of wool per shearing.")
def main():
    cow = Cow("Bessie", 5, 20)
    chicken = Chicken("Clucky", 2, 30)
    sheep = Sheep("Woolly", 4, 5)

    farm_animals = [cow, chicken, sheep]

    for animal in farm_animals:
        print(f"\n--- {animal.name} ---")
        animal.eat()
        animal.sleep()
        animal.make_sound()
        animal.produce()


if __name__ == "__main__":
    main()   