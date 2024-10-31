from validator import Validator
import pytest


@pytest.fixture
def schema():
    v = Validator()
    return v.number()


def test_empty_number(schema):
    assert schema.is_valid(None) == True


def test_number_required(schema):
    schema.required()
    assert schema.is_valid(None) == False


def test_number_int(schema):
    assert schema.is_valid(7) == True
    assert schema.is_valid('7') == False


def test_number_positive(schema):
    assert schema.positive().is_valid(10) == True
    assert schema.positive().is_valid(0) == True
    assert schema.positive().is_valid(-10) == False


def test_number_range(schema):
    schema.range(-5, 5)
    assert schema.is_valid(5) == True
    assert schema.is_valid(-5) == False
    
