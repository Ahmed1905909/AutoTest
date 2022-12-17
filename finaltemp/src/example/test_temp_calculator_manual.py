import Temp_calculator
import pytest


def test_temp_constructor():
    temp_calc = Temp_calculator.TempCalc(86, 30)
    assert temp_calc.fahrenheit == 86
    assert temp_calc.celsius == 30


def test_invalid_fahrenheit():
    # Testing Constructors
    with pytest.raises(ValueError) as context:
        temp_calc = Temp_calculator.TempCalc(-150, 41)

    with pytest.raises(ValueError) as context:
        temp_calc = Temp_calculator.TempCalc(190, 41)

    # Testing setters
    temp_calc = Temp_calculator.TempCalc(190, 22)
    with pytest.raises(ValueError) as context:
        temp_calc.fahrenheit = -60

    with pytest.raises(ValueError) as context:
        temp_calc.fahrenheit = 180


def test_invalid_celsius():
    # Testing Constructors
    with pytest.raises(ValueError) as context:
        temp_calc = Temp_calculator.TempCalc(60, -70)

    with pytest.raises(ValueError) as context:
        temp_calc = Temp_calculator.TempCalc(90, 80)

    # Testing setters
    temp_calc = Temp_calculator.TempCalc(40, 190)
    with pytest.raises(ValueError) as context:
        temp_calc.celsius = -60

    with pytest.raises(ValueError) as context:
        temp_calc.celsius = 180





