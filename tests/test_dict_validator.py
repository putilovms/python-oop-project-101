from validator import Validator


def test_dict_is_valid():
    v = Validator()
    schema = v.dict()

    schema.shape({
        'name': v.string().required(),
        'age': v.number().positive(),
    })

    assert schema.is_valid({'name': 'kolya', 'age': 100}) == True
    assert schema.is_valid({'name': 'maya', 'age': None}) == True
    assert schema.is_valid({'name': '', 'age': None}) == False
    assert schema.is_valid({'name': 'ada', 'age': -5}) == False
