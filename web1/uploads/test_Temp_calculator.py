import Temp_calculator
import pytest


def test_0():
	cut = Temp_calculator.TempCalc(74,27)
	cut.celsius_value()
	cut.fahrenheit = 37
	cut.celsius = -40
	cut.celsius = -20
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.fahrenheit = 88
	cut.celsius = 53


def test_1():
	cut = Temp_calculator.TempCalc(-6,-18)
	cut.celsius = -30
	cut.fahrenheit = 83
	cut.fahrenheit_value()
