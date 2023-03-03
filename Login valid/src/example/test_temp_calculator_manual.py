import Temp_calculator
import pytest


def test_temp_constructor():
    temp_calc = Temp_calculator.Login("ahmed2@gmail.com", "fightclub")
    assert temp_calc.email == "email@hotmail.com"
    assert temp_calc.password == "password"


def test_invalid_eamil():
    # Testing Constructors
    with pytest.raises(ValueError) as context:
        temp_calc = Temp_calculator.Login("21344", "lalaland")

    with pytest.raises(ValueError) as context:
        temp_calc = Temp_calculator.Login("1245hsj@gmail.", "philfoden")

    # Testing setters
    temp_calc = Temp_calculator.Login("fordie@hotmail.org", "babayega")
    with pytest.raises(ValueError) as context:
        temp_calc.email = "no email"

    with pytest.raises(ValueError) as context:
        temp_calc.email = "hireathotmail.com"


def test_invalid_pasword():
    # Testing Constructors
    with pytest.raises(ValueError) as context:
        temp_calc = Temp_calculator.Login("ghaly22@gmail.com", "10")

    with pytest.raises(ValueError) as context:
        temp_calc = Temp_calculator.Login("lol@HOTMAIL.COM", "fefe")

    # Testing setters
    temp_calc = Temp_calculator.Login("randy@yahoo.com", "belly")
    with pytest.raises(ValueError) as context:
        temp_calc.password = "bold"

    with pytest.raises(ValueError) as context:
        temp_calc.password = "e4df"





