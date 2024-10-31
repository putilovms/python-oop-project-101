import math


class CommonValidator():
    def __init__(self):
        self.required_flag = False

    def required(self):
        self.required_flag = True
        return self


class StringValidator(CommonValidator):
    def __init__(self):
        super().__init__()
        self.contains_string = None
        self.min_lenght = None

    def contains(self, string):
        self.contains_string = string
        return self

    def is_valid(self, string):
        if self.required_flag and not string:
            return False
        if string is not None and not isinstance(string, str):
            return False
        if self.contains_string:
            return self.contains_string in string
        if self.min_lenght is not None:
            return len(string) >= self.min_lenght
        return True

    def min_len(self, min_lenght):
        self.min_lenght = min_lenght
        return self


class NumberValidator(CommonValidator):
    def __init__(self):
        super().__init__()
        self.positive_flag = False
        self.range_value = {'min': -math.inf, 'max': math.inf}

    def positive(self):
        self.positive_flag = True
        return self

    def range(self, min, max):
        self.range_value = {'min': min, 'max': max}

    def is_valid(self, number):
        if self.required_flag and not number:
            return False
        if number is not None and not isinstance(number, int):
            return False
        if self.positive_flag and number < 0:
            return False
        if number is not None:
            in_range = number > self.range_value['min'] \
                and number <= self.range_value['max']
            if not in_range:
                return False
        return True


class Validator():
    def string(self):
        return StringValidator()

    def number(self):
        return NumberValidator()
