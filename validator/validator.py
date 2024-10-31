class StringValidator():
    def __init__(self):
        self.required_flag = False
        self.contains_string = None
        self.min_lenght = None

    def required(self):
        self.required_flag = True
        return self

    def contains(self, string):
        self.contains_string = string
        return self

    def is_valid(self, string):
        if self.required_flag and not string:
            return False
        if self.contains_string:
            return self.contains_string in string
        if self.min_lenght is not None:
            return len(string) >= self.min_lenght
        return True

    def min_len(self, min_lenght):
        self.min_lenght = min_lenght
        return self


class Validator():
    def string(self):
        return StringValidator()
