from validator import Validator


def test_own_validators():
    v = Validator()

    v.add_validator('string', 'startWith',
                    lambda value, start: value.startswith(start))
    schema = v.string().test('startWith', 'H')
    assert not schema.is_valid('exlet')
    assert schema.is_valid('Hexlet')

    v.add_validator('number', 'min', lambda value, min: value >= min)
    schema = v.number().test('min', 5)
    assert not schema.is_valid(4)
    assert schema.is_valid(6)
