import bmi_calculator
import pytest


def test_0():
	cut = bmi_calculator.BMICalc(224,393,27)
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.age = 40
	cut.age = 25
	cut.weight = 954
	cut.bmi_value()
	cut.height = 505
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.age = 142
	cut.age = 85
	cut.classify_bmi_teens_and_children()
	cut.height = 935
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.weight = 785
	cut.classify_bmi_adults()


def test_1():
	cut = bmi_calculator.BMICalc(756,625,0)
	cut.height = 995
	cut.classify_bmi_adults()
	cut.height = 435
	cut.age = 86
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.age = 18
	cut.weight = 482
	cut.weight = 448


def test_2():
	cut = bmi_calculator.BMICalc(490,687,11)
	cut.classify_bmi_adults()
	cut.height = 256
	cut.age = 145
	cut.classify_bmi_adults()
	cut.height = 214


def test_3():
	cut = bmi_calculator.BMICalc(143,476,69)
	cut.age = 5
	cut.height = 409
	cut.age = 23
	cut.age = 45
	cut.age = 135
	cut.classify_bmi_teens_and_children()
	cut.height = 840
	cut.height = 495
	cut.weight = 25
	cut.height = 403
	cut.weight = 257
	cut.bmi_value()
	cut.age = 30


def test_4():
	cut = bmi_calculator.BMICalc(204,832,38)
	cut.height = 668
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.age = 83
	cut.bmi_value()
	cut.classify_bmi_adults()


def test_5():
	cut = bmi_calculator.BMICalc(493,670,131)
	cut.classify_bmi_adults()


def test_6():
	cut = bmi_calculator.BMICalc(724,170,95)
	cut.weight = 327
	cut.weight = 185
	cut.age = 18
	cut.height = 199
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.age = 77
	cut.age = 19
	cut.classify_bmi_adults()
	cut.height = 578
	cut.height = 883
	cut.age = 102
	cut.classify_bmi_adults()
	cut.weight = 204
	cut.age = 32
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.height = 95


def test_7():
	cut = bmi_calculator.BMICalc(624,746,37)
	cut.classify_bmi_teens_and_children()
	cut.weight = 542
	cut.weight = 746
	cut.bmi_value()
	cut.bmi_value()
	cut.age = 109
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.height = 406
	cut.classify_bmi_teens_and_children()
	cut.age = 57
	cut.classify_bmi_adults()


def test_8():
	cut = bmi_calculator.BMICalc(751,721,48)
	cut.age = 145
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.weight = 884
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()


def test_9():
	cut = bmi_calculator.BMICalc(751,721,48)
	cut.age = 145
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.weight = 884
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()


def test_10():
	cut = bmi_calculator.BMICalc(248,989,72)
	cut.age = 31
	cut.classify_bmi_adults()
	cut.weight = 674
	cut.height = 303


def test_11():
	cut = bmi_calculator.BMICalc(629,955,90)
	cut.bmi_value()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.height = 243
	cut.bmi_value()
	cut.age = 113
	cut.bmi_value()
	cut.classify_bmi_adults()
