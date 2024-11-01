from validator import Validator
import pytest


@pytest.fixture
def schema():
    v = Validator()
    return v.number()


def test_empty_number(schema):
    assert schema.is_valid(None)


def test_number_required(schema):
    schema.required()
    assert not schema.is_valid(None)
    assert not schema.is_valid(0)


def test_number_int(schema):
    assert schema.is_valid(7)
    assert not schema.is_valid('7')


def test_number_positive(schema):
    assert schema.positive().is_valid(10)
    assert schema.positive().is_valid(0)
    assert not schema.positive().is_valid(-10)


def test_number_range(schema):
    schema.range(-5, 5)
    assert schema.is_valid(5)
    assert not schema.is_valid(-5)
