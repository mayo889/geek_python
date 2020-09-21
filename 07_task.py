import re


class ComplexNumber:
    def __init__(self, data):
        self.a = int(re.findall(r"(\S+)\b[+-]", data)[0])
        self.b = int(re.findall(r"(\b[+-]\d+)i", data)[0])

    def __str__(self):
        return f"{self.a}+{self.b}i" if self.b >= 0 else f"{self.a}{self.b}i"

    def __add__(self, other):
        a, b = self.a + other.a, self.b + other.b
        return ComplexNumber(f"{a}+{b}i") if b >= 0 else ComplexNumber(f"{a}{b}i")

    def __mul__(self, other):
        a, b = self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b
        return ComplexNumber(f"{a}+{b}i") if b >= 0 else ComplexNumber(f"{a}{b}i")


# complex_1 = ComplexNumber(input("Введите первое комплексное число в виде a+bi: "))
# complex_2 = ComplexNumber(input("Введите второе комплексное число в виде a+bi: "))
complex_1 = ComplexNumber('11-22i')
complex_2 = ComplexNumber('-24+34i')
print(complex_1)
print(complex_2)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
