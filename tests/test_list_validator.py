from validator import Validator
import pytest


@pytest.fixture
def schema():
    v = Validator()
    return v.list()


def test_empty_list(schema):
    assert schema.is_valid(None) == True


def test_list_required(schema):
    schema.required()
    assert schema.is_valid(None) == False
    assert schema.is_valid([]) == True
    assert schema.is_valid(['hexlet']) == True


def test_list_sizeof(schema):
    schema.sizeof(2)
    assert schema.is_valid(['hexlet']) == False
    assert schema.is_valid(['hexlet', 'code-basics']) == True
