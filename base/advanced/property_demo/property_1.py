"""
Class which stores temperature in degree celsius
"""


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


if __name__ == '__main__':
    man = Celsius()
    # man.temperature = 37  # Set temp
    # print(man.temperature)  # Get temp
    # print(man.to_fahrenheit())

    # Whenever we assign or retrieve any object attribute like temperature, as show above,
    # Python searches it in the object's __dict__ dictionary.
    print(man.__dict__)
    # Thus man.temperature internally becomes man.__dict__['temperature']
