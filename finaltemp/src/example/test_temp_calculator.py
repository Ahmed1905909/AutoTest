import Temp_calculator
import pytest


def test_0():
	cut = Temp_calculator.TempCalc(96,-24)
	cut.fahrenheit_value()
	cut.fahrenheit = 34
	cut.fahrenheit = 77
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.fahrenheit = 12


def test_1():
	cut = Temp_calculator.TempCalc(110,-23)
	cut.celsius = -13
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit = 116
	cut.celsius = -29
	cut.celsius = 44
	cut.fahrenheit = 23
	cut.celsius_value()
	cut.fahrenheit = 113
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit = 51
	cut.fahrenheit = 104


def test_2():
	cut = Temp_calculator.TempCalc(-7,-35)
	cut.celsius = -26
	cut.fahrenheit = 132
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius = 37
	cut.fahrenheit = 42
	cut.celsius_value()
	cut.celsius = -16
	cut.celsius_value()
	cut.fahrenheit = 91


def test_3():
	cut = Temp_calculator.TempCalc(98,9)
	cut.celsius = 0
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit = 77
	cut.celsius = -29
	cut.fahrenheit_value()
	cut.celsius = 8


def test_4():
	cut = Temp_calculator.TempCalc(-39,1)
	cut.celsius = 60
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius = 42
	cut.celsius = 55
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius = 48
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit_value()


def test_5():
	cut = Temp_calculator.TempCalc(-15,-26)
	cut.celsius_value()
	cut.celsius = 24
	cut.celsius = 58
	cut.celsius_value()


def test_6():
	cut = Temp_calculator.TempCalc(54,60)
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 57
	cut.celsius = -8
	cut.fahrenheit = 136
	cut.celsius_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.celsius = 13
	cut.celsius_value()
	cut.fahrenheit = 64
	cut.fahrenheit = 55
	cut.celsius_value()
	cut.celsius = -38
	cut.celsius = -25
	cut.celsius_value()
	cut.celsius = 20


def test_7():
	cut = Temp_calculator.TempCalc(98,23)
	cut.fahrenheit_value()
	cut.celsius = -17
	cut.celsius_value()
	cut.fahrenheit = 123
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.celsius = 59
	cut.celsius_value()


def test_8():
	cut = Temp_calculator.TempCalc(-27,29)
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit = 6
	cut.celsius_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 69


def test_9():
	cut = Temp_calculator.TempCalc(27,-32)
	cut.fahrenheit = 19
	cut.fahrenheit = -36
	cut.celsius_value()
	cut.fahrenheit = 88
	cut.fahrenheit = 17
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.fahrenheit = 88
	cut.fahrenheit_value()
	cut.celsius = -27
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.fahrenheit_value()


def test_10():
	cut = Temp_calculator.TempCalc(39,40)
	cut.fahrenheit_value()
	cut.celsius = -18
	cut.fahrenheit = -10
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius = -36
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.fahrenheit = 36
	cut.fahrenheit = 78
	cut.celsius_value()
	cut.celsius_value()
	cut.celsius = 57
	cut.fahrenheit_value()


def test_11():
	cut = Temp_calculator.TempCalc(117,29)
	cut.fahrenheit = 41
	cut.celsius = 28
	cut.fahrenheit = 134
	cut.fahrenheit_value()
	cut.fahrenheit_value()


def test_12():
	cut = Temp_calculator.TempCalc(25,-2)
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 16
	cut.fahrenheit_value()
	cut.fahrenheit = 23
	cut.celsius = 8
	cut.fahrenheit = -1
	cut.celsius = -1
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.fahrenheit = 92


def test_13():
	cut = Temp_calculator.TempCalc(60,55)
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.fahrenheit = 58


def test_14():
	cut = Temp_calculator.TempCalc(82,-11)
	cut.fahrenheit = 71
	cut.fahrenheit = 19
	cut.fahrenheit_value()
	cut.celsius = -40
	cut.fahrenheit = 47
	cut.celsius = 25
	cut.celsius_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 115
	cut.fahrenheit_value()
	cut.fahrenheit = 99
	cut.fahrenheit = 12
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit = 63
