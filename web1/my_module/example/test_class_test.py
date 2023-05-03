import class_test
import pytest


def test_0():
	cut = class_test.Testexample(355,200,142)
	cut.height = 536
	cut.age = 66
	cut.age = 142
	cut.classify_bmi_adults()
	cut.bmi_value()


def test_1():
	cut = class_test.Testexample(149,586,12)
	cut.classify_bmi_adults()
	cut.age = 37
	cut.age = 67
	cut.weight = 643
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.height = 467
	cut.classify_bmi_adults()
	cut.age = 80


def test_2():
	cut = class_test.Testexample(61,969,107)
	cut.height = 947
	cut.classify_bmi_adults()
	cut.age = 122
	cut.classify_bmi_teens_and_children()
	cut.age = 49
	cut.classify_bmi_teens_and_children()
	cut.weight = 610
	cut.height = 893
	cut.age = 50
	cut.bmi_value()
	cut.height = 396
	cut.weight = 446
	cut.age = 1
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.weight = 843
	cut.classify_bmi_teens_and_children()
	cut.height = 930


def test_3():
	cut = class_test.Testexample(865,52,76)


def test_4():
	cut = class_test.Testexample(800,500,138)
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()


def test_5():
	cut = class_test.Testexample(14,312,37)
	cut.age = 20


def test_6():
	cut = class_test.Testexample(690,840,142)
	cut.bmi_value()
	cut.height = 150
	cut.classify_bmi_adults()
	cut.age = 146
	cut.bmi_value()
	cut.weight = 675
	cut.weight = 16
	cut.bmi_value()
	cut.weight = 868
	cut.classify_bmi_teens_and_children()
	cut.weight = 848
	cut.age = 43
	cut.height = 216
	cut.age = 80
	cut.classify_bmi_adults()
	cut.bmi_value()


def test_7():
	cut = class_test.Testexample(42,952,21)
	cut.bmi_value()
	cut.weight = 229
	cut.age = 124
	cut.age = 70
	cut.classify_bmi_teens_and_children()
	cut.height = 321
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.age = 63
	cut.age = 15
	cut.bmi_value()
	cut.bmi_value()
	cut.weight = 650
	cut.age = 40
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.weight = 349
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()


def test_8():
	cut = class_test.Testexample(550,487,38)
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()


def test_9():
	cut = class_test.Testexample(877,415,128)
	cut.classify_bmi_teens_and_children()
	cut.weight = 494
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.weight = 234
	cut.classify_bmi_teens_and_children()
	cut.height = 949
	cut.age = 10
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.age = 22
	cut.age = 73


def test_10():
	cut = class_test.Testexample(715,907,144)


def test_11():
	cut = class_test.Testexample(639,651,37)


def test_12():
	cut = class_test.Testexample(111,930,142)
