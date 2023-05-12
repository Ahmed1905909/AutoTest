import Temp_calculator
import pytest


def test_temp_constructor():
    temp_calc = class_test.TempCalc(86, 30)
    assert temp_calc.fahrenheit == 86
    assert temp_calc.celsius == 30


def test_invalid_fahrenheit():
    # Testing Constructors
    with pytest.raises(ValueError) as context:
        temp_calc = class_test.TempCalc(-150, 41)

    with pytest.raises(ValueError) as context:
        temp_calc = class_test.TempCalc(190, 41)

    # Testing setters
    temp_calc = class_test.TempCalc(190, 22)
    with pytest.raises(ValueError) as context:
        temp_calc.fahrenheit = -60

    with pytest.raises(ValueError) as context:
        temp_calc.fahrenheit = 180


def test_invalid_celsius():
    # Testing Constructors
    with pytest.raises(ValueError) as context:
        temp_calc = class_test.TempCalc(60, -70)

    with pytest.raises(ValueError) as context:
        temp_calc = class_test.TempCalc(90, 80)

    # Testing setters
    temp_calc = class_test.TempCalc(40, 190)
    with pytest.raises(ValueError) as context:
        temp_calc.celsius = -60

    with pytest.raises(ValueError) as context:
        temp_calc.celsius = 180





