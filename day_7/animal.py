class Animal:
    name = 'Homer'
    noise = "Grunt"
    size = "Large"
    color = "Brown"

    def get_color(self):
        return self.color

    def make_noise(self):
        return self.noise


class Dog(Animal):
    name = 'Gib'
    size = 'small'
    color = "black"


gib = Dog()
print(gib.color)
