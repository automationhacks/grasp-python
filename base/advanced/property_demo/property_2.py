"""
In case client asks us to implement a constraint in property_1 example that,
temperature cannot be less than -273.15 (absolute 0)

Solution: Hide attribute temperature (make it private) and define getter and setter interfaces to manipulate it

Impl: 1. temperature is made as _temperature
      2. get_temperature and set_temperature methods are implemented
"""


class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError('Temp below -273 is not possible')
        self._temperature = value


if __name__ == '__main__':
    # man = Celsius(-277)  # will return a value error
    man = Celsius(37)
    print(man.get_temperature())
    man.set_temperature(-300)
    print(man.get_temperature())

"""
The big problem with the above update is that, all the clients who implemented our previous class in their program have,
 to modify their code from obj.temperature to obj.get_temperature() and all assignments like obj.temperature = val to ,
 obj.set_temperature(val).
This refactoring can cause headaches to the clients with hundreds of thousands of lines of codes.
All in all, our new update was not backward compatible. This is where property comes to rescue.
"""
