from validator import Validator


def test_test():
    validator = Validator()
    assert validator.test() is None
