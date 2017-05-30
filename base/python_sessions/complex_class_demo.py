class ComplexNumbers:

    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_complex_num(self):
        return '%s+%sj' % (self.real, self.imag)

c1 = ComplexNumbers(1, 3)  # First Object
print(c1.get_complex_num())

c2 = ComplexNumbers(5)  # Second Object
c2.attr = 11  # Create new attribute for c2

print(c2.real, c2.imag, c2.attr)
# print(c1.attr)
