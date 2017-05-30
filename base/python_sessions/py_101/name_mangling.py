class Cup:
    def __init__(self, color):
        self._color = color    # protected variable
        self.__content = None  # private variable

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

c = Cup('red')
print(c.__content) # Invalid since double underscore and single underscore is understood as _<class><member>
print(c._Cup__content) # Valid


