import Temp_calculator
import pytest


def test_0():
	cut = class_test.TempCalc(99,38)
	cut.celsius = 49
	cut.fahrenheit = 21
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.fahrenheit = 105
	cut.celsius_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius = 39


def test_1():
	cut = class_test.TempCalc(1,-35)
	cut.fahrenheit = 64
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius = -5
	cut.celsius_value()
	cut.fahrenheit = 11


def test_2():
	cut = class_test.TempCalc(27,8)
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius = -24
	cut.fahrenheit = 96
	cut.fahrenheit_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.celsius_value()
	cut.fahrenheit = 97


def test_3():
	cut = class_test.TempCalc(24,-16)
	cut.celsius = 40
	cut.fahrenheit = 47
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.fahrenheit_value()


def test_4():
	cut = class_test.TempCalc(17,3)
	cut.fahrenheit_value()
	cut.fahrenheit_value()
	cut.celsius = -12
	cut.fahrenheit = 62
	cut.fahrenheit_value()
	cut.fahrenheit_value()


def test_5():
	cut = class_test.TempCalc(-33,14)


def test_6():
	cut = class_test.TempCalc(-10,-13)


def test_7():
	cut = class_test.TempCalc(65,-29)
	cut.fahrenheit_value()
	cut.fahrenheit = 18
	cut.celsius_value()
	cut.fahrenheit = -26
	cut.celsius = -11
	cut.fahrenheit = 63
	cut.fahrenheit = 38
	cut.celsius = -24
	cut.celsius_value()


def test_8():
	cut = class_test.TempCalc(50,-19)
	cut.fahrenheit = 99
	cut.fahrenheit_value()


def test_9():
	cut = class_test.TempCalc(135,13)
	cut.fahrenheit_value()
	cut.fahrenheit = 32
	cut.fahrenheit = -26
	cut.fahrenheit = -15
	cut.celsius = 47
