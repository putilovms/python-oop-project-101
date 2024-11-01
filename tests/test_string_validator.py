from validator import Validator
import pytest


@pytest.fixture
def schema():
    v = Validator()
    return v.string()


def test_new_schema():
    v = Validator()
    schema = v.string()
    schema2 = v.string()
    assert schema is not schema2


def test_empty_string(schema):
    assert schema.is_valid('')
    assert schema.is_valid(None)


def test_string_str(schema):
    assert schema.is_valid('what does the fox say')
    assert not schema.is_valid(10)


def test_string_required():
    v = Validator()
    schema = v.string()
    schema2 = v.string()
    schema.required()
    assert not schema.is_valid('')
    assert not schema.is_valid(None)
    assert schema.is_valid('hexlet')
    assert schema2.is_valid('')


def test_string_contains(schema):
    assert schema.contains('').is_valid('what does the fox say')
    assert schema.contains('what').is_valid('what does the fox say')
    assert not schema.contains('whatthe').is_valid('what does the fox say')


def test_string_length():
    v = Validator()
    assert not v.string().min_len(10).is_valid('Hexlet')
    assert v.string().min_len(10).min_len(4).is_valid('Hexlet')
