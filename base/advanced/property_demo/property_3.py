"""
To ensure backward compatibility in case setter logics need to be changed, Python property can be used.
"""


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature  # Calls the setter

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError('Temp below -273 is not possible')
        print('setting value')
        self._temperature = value

    temperature = property(get_temperature, set_temperature)  # This converts methods as property object
    # i.e. attaches some code to member attribute accesses (temperature)


if __name__ == '__main__':
    c = Celsius()  # Calls the setter implicitly

    # Any code to retrieve value of temp calls get_temperature instead of __dict__ lookup

    print(c.temperature)
    c.temperature = 27
    print(c.temperature)
    print(c.to_fahrenheit())

    # Finally note that, the actual temperature value is stored in the private variable _temperature.
    # The attribute temperature is a property object which provides interface to this private variable.
