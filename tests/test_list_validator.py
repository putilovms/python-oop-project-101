from validator import Validator
import pytest


@pytest.fixture
def schema():
    v = Validator()
    return v.list()


def test_empty_list(schema):
    assert schema.is_valid(None)


def test_list_required(schema):
    schema.required()
    assert not schema.is_valid(None)
    assert schema.is_valid([])
    assert schema.is_valid(['hexlet'])


def test_list_sizeof(schema):
    schema.sizeof(2)
    assert not schema.is_valid(['hexlet'])
    assert schema.is_valid(['hexlet', 'code-basics'])
