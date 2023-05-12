import Temp_calculator
import pytest


def test_0():
	cut = Temp_calculator.TempCalc(138,23)
	cut.fahrenheit = 108
	cut.fahrenheit = 96
	cut.fahrenheit_value()
	cut.fahrenheit = -10
	cut.fahrenheit = 99
	cut.fahrenheit_value()
	cut.fahrenheit = -26
	cut.fahrenheit = 96


def test_1():
	cut = Temp_calculator.TempCalc(90,-18)
	cut.fahrenheit_value()
	cut.celsius = 17
	cut.celsius_value()
	cut.celsius = 47
	cut.celsius_value()
	cut.fahrenheit = 64
	cut.celsius = 21
	cut.fahrenheit_value()


def test_2():
	cut = Temp_calculator.TempCalc(138,-25)
	cut.fahrenheit = 60


def test_3():
	cut = Temp_calculator.TempCalc(127,43)
	cut.celsius = -1
	cut.celsius_value()
	cut.fahrenheit = -40
	cut.fahrenheit_value()


def test_4():
	cut = Temp_calculator.TempCalc(68,-17)
	cut.celsius_value()
	cut.celsius = -21
	cut.celsius = 44
	cut.celsius = -24
	cut.fahrenheit = 41
	cut.celsius = 5
	cut.celsius = -39
	cut.fahrenheit = 54


def test_5():
	cut = Temp_calculator.TempCalc(76,8)
	cut.celsius_value()
	cut.celsius = 0
	cut.celsius = -11
	cut.celsius = 32
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()


def test_6():
	cut = Temp_calculator.TempCalc(131,-8)
	cut.fahrenheit = 15
	cut.fahrenheit_value()
	cut.celsius = -20
	cut.fahrenheit = 100
	cut.celsius = -5
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.celsius = -30
	cut.fahrenheit = 124


def test_7():
	cut = Temp_calculator.TempCalc(9,19)
	cut.celsius = 0
	cut.fahrenheit = 112
	cut.fahrenheit = 105
	cut.celsius = 48
