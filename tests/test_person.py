from secret_santa.person import PersonType, Household


def test_recipient_type():
    print(PersonType.PARENT)
    print(PersonType.GRANDPARENT)
    print(PersonType.ALL)
    print(PersonType.GRANDCHILD | PersonType.CHILD)
    print(PersonType.GRANDPARENT & PersonType.PARENT)
    print(PersonType.ALL & ~PersonType.PARENT)
    print(~PersonType.CHILD)
    assert True


def test_from_name():
    # unexpected way to reference an enum using a string
    household = Household['BOB_AND_NAN']
    print('\n')
    print('retrieved household: \n')
    print(household)
    assert True
