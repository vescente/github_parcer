class PositiveIntegerField:

    def __init__(self, val=0):
        self._val = val

    def __get__(self, instance, owner):
        print(f"Getting value: {self._val}")
        return self._val

    def __set__(self, instance, value):
        print(f"Setting value: {value}")
        self._val = value if value > 0 else ValueError(
            "Value must be positive")

    # def __delete__(self, instance):
    #     pass


class Person:

    # Using the descriptor
    age = PositiveIntegerField()

    def __init__(self, age):
        self.age = age


class Salary:
    # Using the descriptor
    value = PositiveIntegerField()

    def __init__(self, value):
        self.value = value

    # @property
    # def value(self):
    #     return self._value

    # @value.setter
    # def value(self, new_value):
    #     if new_value < 0:
    #         raise ValueError("Salary cannot be negative")
    #     self._value = new_value


person = Person(10)
person.age = 20
print(person.age)  # Output: 20
salary = Salary(10000)
salary.value = -20000
print(salary.value)  # Output: 2000
