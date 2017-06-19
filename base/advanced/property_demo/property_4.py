"""
The previous implementation can be implemented as a decorator in python
"""


class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.__temperature * 18) + 32

    @property
    def temperature(self):
        print('Getter')
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError('Not allowed dude!')

        print('Setter')
        self.__temperature = value


if __name__ == '__main__':
    c = Celsius(0)
    print(c.temperature)
    x = Celsius(37)
    print(x.temperature)
    y = Celsius(-300)
    print(y.temperature)
