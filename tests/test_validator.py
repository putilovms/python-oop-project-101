from validator import Validator


def test_new_schema():
    v = Validator()
    schema = v.string()
    schema2 = v.string()
    assert schema is not schema2


def test_empty_string_is_valid():
    v = Validator()
    schema = v.string()
    assert schema.is_valid('') == True
    assert schema.is_valid(None) == True
    assert schema.is_valid('what does the fox say') == True


def test_string_required():
    v = Validator()
    schema = v.string()
    schema2 = v.string()
    schema.required()
    assert schema.is_valid('') == False
    assert schema.is_valid(None) == False
    assert schema2.is_valid('') == True
    assert schema.is_valid('hexlet') == True


def test_string_contains():
    v = Validator()
    schema = v.string()
    assert schema.contains('what').is_valid('what does the fox say') == True
    assert schema.contains('whatthe').is_valid('what does the fox say') == False

def test_string_length():
    v = Validator()
    assert v.string().min_len(10).min_len(4).is_valid('Hexlet') == True
