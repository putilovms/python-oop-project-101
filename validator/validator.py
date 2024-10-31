import math


class RequiredMixin():
    required_flag = False

    def required(self):
        self.required_flag = True
        return self


class StringValidator(RequiredMixin):
    def __init__(self):
        self.contains_string = None
        self.min_lenght = None

    def contains(self, string):
        self.contains_string = string
        return self

    def min_len(self, min_lenght):
        self.min_lenght = min_lenght
        return self

    def is_valid(self, value):
        if self.required_flag and not value:
            return False
        if value is not None and not isinstance(value, str):
            return False
        if self.contains_string:
            if self.contains_string not in value:
                return False
        if self.min_lenght is not None:
            if len(value) < self.min_lenght:
                return False
        return True


class NumberValidator(RequiredMixin):
    def __init__(self):
        self.positive_flag = False
        self.range_value = {'min': -math.inf, 'max': math.inf}

    def positive(self):
        self.positive_flag = True
        return self

    def range(self, min_value, max_value):
        self.range_value = {'min': min_value, 'max': max_value}
        return self

    def is_valid(self, value):
        if self.required_flag and value is None:
            return False
        if value is not None and not isinstance(value, int):
            return False
        if value is not None and self.positive_flag and value < 0:
            return False
        if value is not None:
            min_value = self.range_value['min']
            max_value = self.range_value['max']
            in_range = value > min_value and value <= max_value
            if not in_range:
                return False
        return True


class ListValidator(RequiredMixin):
    def __init__(self):
        self.sizeof_value = None

    def sizeof(self, value):
        self.sizeof_value = value
        return self

    def is_valid(self, value):
        if self.required_flag and value is None:
            return False
        if value is not None and not isinstance(value, list):
            return False
        sizeof = self.sizeof_value
        if sizeof is not None and len(value) < sizeof:
            return False
        return True


class DictValidator():
    def shape(self, checks):
        self.checks = checks

    def is_valid(self, values):
        for key, value in values.items():
            if not self.checks[key].is_valid(value):
                return False
        return True


class Validator():
    def string(self):
        return StringValidator()

    def number(self):
        return NumberValidator()

    def list(self):
        return ListValidator()

    def dict(self):
        return DictValidator()
