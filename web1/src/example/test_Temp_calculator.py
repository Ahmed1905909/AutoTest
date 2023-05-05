import Temp_calculator
import pytest


def test_0():
	cut = Temp_calculator.TempCalc(72,43)
	cut.celsius = -21
	cut.fahrenheit_value()
	cut.fahrenheit = 3
	cut.fahrenheit_value()
	cut.celsius = 60
	cut.fahrenheit = 91
	cut.celsius = 59
	cut.fahrenheit_value()
	cut.fahrenheit = 62


def test_1():
	cut = Temp_calculator.TempCalc(72,43)
	cut.celsius = -21
	cut.fahrenheit_value()
	cut.fahrenheit = 3
	cut.fahrenheit_value()
	cut.celsius = 60
	cut.fahrenheit = 86
	cut.celsius = 59
	cut.fahrenheit_value()
	cut.fahrenheit = 62


def test_2():
	cut = Temp_calculator.TempCalc(21,42)
	cut.fahrenheit = 120
	cut.fahrenheit = 3
	cut.celsius = 35


def test_3():
	cut = Temp_calculator.TempCalc(21,42)
	cut.fahrenheit = 120
	cut.fahrenheit = 3
	cut.celsius = 35


def test_4():
	cut = Temp_calculator.TempCalc(-8,-9)
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 85
	cut.fahrenheit_value()


def test_5():
	cut = Temp_calculator.TempCalc(13,18)
	cut.celsius_value()
	cut.fahrenheit = 20
	cut.fahrenheit = -27
	cut.celsius_value()
	cut.fahrenheit_value()


def test_6():
	cut = Temp_calculator.TempCalc(13,18)
	cut.celsius_value()
	cut.fahrenheit = 20
	cut.fahrenheit = -27
	cut.celsius_value()
	cut.fahrenheit_value()


def test_7():
	cut = Temp_calculator.TempCalc(63,30)
	cut.fahrenheit_value()


def test_8():
	cut = Temp_calculator.TempCalc(-27,-15)
	cut.fahrenheit = 116
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit = 131
	cut.fahrenheit_value()
	cut.celsius_value()


def test_9():
	cut = Temp_calculator.TempCalc(-27,-15)
	cut.fahrenheit = 116
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit = 131
	cut.fahrenheit_value()
	cut.celsius_value()


def test_10():
	cut = Temp_calculator.TempCalc(72,43)
	cut.celsius = -21
	cut.fahrenheit_value()
	cut.fahrenheit = 3
	cut.fahrenheit_value()
	cut.celsius = 60
	cut.fahrenheit = 91
	cut.celsius = 59
	cut.fahrenheit_value()
	cut.fahrenheit = 62


def test_11():
	cut = Temp_calculator.TempCalc(72,43)
	cut.celsius = -21
	cut.fahrenheit_value()
	cut.fahrenheit = 3
	cut.fahrenheit_value()
	cut.celsius = 60
	cut.fahrenheit = 91
	cut.celsius = 59
	cut.fahrenheit_value()
	cut.fahrenheit = 62


def test_12():
	cut = Temp_calculator.TempCalc(21,42)
	cut.fahrenheit = 120
	cut.fahrenheit = 3
	cut.celsius = 35


def test_13():
	cut = Temp_calculator.TempCalc(21,42)
	cut.fahrenheit = 120
	cut.fahrenheit = 3
	cut.celsius = 35


def test_14():
	cut = Temp_calculator.TempCalc(-8,-9)
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 85
	cut.fahrenheit_value()


def test_15():
	cut = Temp_calculator.TempCalc(-8,-9)
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 85
	cut.fahrenheit_value()


def test_16():
	cut = Temp_calculator.TempCalc(13,18)
	cut.celsius_value()
	cut.fahrenheit = 20
	cut.fahrenheit = -27
	cut.celsius_value()
	cut.fahrenheit_value()


def test_17():
	cut = Temp_calculator.TempCalc(13,18)
	cut.celsius_value()
	cut.fahrenheit = 20
	cut.fahrenheit = -27
	cut.celsius_value()
	cut.fahrenheit_value()


def test_18():
	cut = Temp_calculator.TempCalc(63,30)
	cut.fahrenheit_value()


def test_19():
	cut = Temp_calculator.TempCalc(63,30)
	cut.fahrenheit_value()


def test_20():
	cut = Temp_calculator.TempCalc(-27,-15)
	cut.fahrenheit = 116
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit = 131
	cut.fahrenheit_value()
	cut.celsius_value()


def test_21():
	cut = Temp_calculator.TempCalc(-27,-15)
	cut.fahrenheit = 116
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit = 131
	cut.fahrenheit_value()
	cut.celsius_value()


def test_22():
	cut = Temp_calculator.TempCalc(72,43)
	cut.celsius = -21
	cut.fahrenheit_value()
	cut.fahrenheit = 3
	cut.fahrenheit_value()
	cut.celsius = 60
	cut.fahrenheit = 91
	cut.celsius = 59
	cut.fahrenheit_value()
	cut.fahrenheit = 62


def test_23():
	cut = Temp_calculator.TempCalc(72,43)
	cut.celsius = -21
	cut.fahrenheit_value()
	cut.fahrenheit = 3
	cut.fahrenheit_value()
	cut.celsius = 60
	cut.fahrenheit = 91
	cut.celsius = 59
	cut.fahrenheit_value()
	cut.fahrenheit = 62


def test_24():
	cut = Temp_calculator.TempCalc(72,43)
	cut.celsius = -21
	cut.fahrenheit_value()
	cut.fahrenheit = 3
	cut.fahrenheit_value()
	cut.celsius = 60
	cut.fahrenheit = 91
	cut.celsius = 59
	cut.fahrenheit_value()
	cut.fahrenheit = 62


def test_25():
	cut = Temp_calculator.TempCalc(21,42)
	cut.fahrenheit = 120
	cut.fahrenheit = 3
	cut.celsius = 35


def test_26():
	cut = Temp_calculator.TempCalc(-8,-9)
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 85
	cut.fahrenheit_value()


def test_27():
	cut = Temp_calculator.TempCalc(21,42)
	cut.fahrenheit = 120
	cut.fahrenheit = 3
	cut.celsius = 35


def test_28():
	cut = Temp_calculator.TempCalc(21,42)
	cut.fahrenheit = 120
	cut.fahrenheit = 3
	cut.celsius = 35


def test_29():
	cut = Temp_calculator.TempCalc(63,30)
	cut.fahrenheit_value()


def test_30():
	cut = Temp_calculator.TempCalc(-8,-9)
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 85
	cut.fahrenheit_value()


def test_31():
	cut = Temp_calculator.TempCalc(-27,-15)
	cut.fahrenheit = 116
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit = 131
	cut.fahrenheit_value()
	cut.celsius_value()


def test_32():
	cut = Temp_calculator.TempCalc(-8,-9)
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 85
	cut.fahrenheit_value()


def test_33():
	cut = Temp_calculator.TempCalc(13,18)
	cut.celsius_value()
	cut.fahrenheit = 20
	cut.fahrenheit = -27
	cut.celsius_value()
	cut.fahrenheit_value()


def test_34():
	cut = Temp_calculator.TempCalc(13,18)
	cut.celsius_value()
	cut.fahrenheit = 20
	cut.fahrenheit = -27
	cut.celsius_value()
	cut.fahrenheit_value()


def test_35():
	cut = Temp_calculator.TempCalc(-39,47)
	cut.celsius = 58
	cut.fahrenheit = 35
	cut.fahrenheit = 128
	cut.fahrenheit = 92
	cut.fahrenheit_value()
	cut.fahrenheit = -40
	cut.fahrenheit_value()
	cut.celsius = 28
	cut.fahrenheit_value()
