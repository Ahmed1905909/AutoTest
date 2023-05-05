import class_test
import pytest


def test_0():
	cut = class_test.Testexample(783,497,36)
	cut.weight = 632
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.age = 18
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.age = 14
	cut.age = 8
	cut.weight = 363
	cut.classify_bmi_adults()


def test_1():
	cut = class_test.Testexample(684,755,8)
	cut.classify_bmi_teens_and_children()
	cut.weight = 145
	cut.age = 140
	cut.classify_bmi_adults()
	cut.age = 29
	cut.weight = 578
	cut.bmi_value()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.height = 567
	cut.bmi_value()
	cut.weight = 599
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.height = 812
	cut.bmi_value()


def test_2():
	cut = class_test.Testexample(461,41,77)
	cut.age = 16
	cut.height = 813
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.height = 173
	cut.classify_bmi_adults()
	cut.height = 255
	cut.bmi_value()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.height = 864
	cut.age = 145
	cut.age = 128


def test_3():
	cut = class_test.Testexample(379,820,79)
	cut.height = 197
	cut.age = 87
	cut.height = 842
	cut.classify_bmi_teens_and_children()
	cut.age = 135
	cut.bmi_value()
	cut.age = 16
	cut.height = 256
	cut.weight = 2
	cut.weight = 168
	cut.classify_bmi_adults()
	cut.weight = 498
	cut.bmi_value()
	cut.height = 550
	cut.classify_bmi_teens_and_children()
	cut.height = 416
	cut.classify_bmi_adults()


def test_4():
	cut = class_test.Testexample(915,499,45)


def test_5():
	cut = class_test.Testexample(552,897,56)
	cut.weight = 507
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.age = 18
	cut.height = 695
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.weight = 617
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.weight = 322
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.age = 128
	cut.age = 122
	cut.age = 41


def test_6():
	cut = class_test.Testexample(317,650,41)
	cut.height = 240
	cut.height = 476
	cut.classify_bmi_adults()
	cut.height = 302
	cut.classify_bmi_adults()
	cut.weight = 1
	cut.weight = 510
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.age = 14
	cut.age = 143
	cut.classify_bmi_teens_and_children()
	cut.height = 622
	cut.classify_bmi_teens_and_children()


def test_7():
	cut = class_test.Testexample(10,958,132)
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.height = 534
	cut.classify_bmi_adults()
	cut.age = 129
	cut.age = 116
	cut.height = 546
	cut.height = 946


def test_8():
	cut = class_test.Testexample(697,686,106)
	cut.classify_bmi_adults()
	cut.weight = 749
	cut.height = 215
	cut.weight = 732
	cut.bmi_value()
	cut.height = 599
	cut.classify_bmi_adults()
	cut.age = 27
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()


def test_9():
	cut = class_test.Testexample(928,601,111)
	cut.weight = 441
	cut.bmi_value()
	cut.weight = 322
	cut.height = 247
	cut.weight = 169
	cut.weight = 212
	cut.weight = 190
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.age = 92
	cut.bmi_value()


def test_10():
	cut = class_test.Testexample(385,744,119)
	cut.bmi_value()
	cut.age = 142
	cut.bmi_value()
	cut.height = 43
	cut.classify_bmi_adults()
	cut.height = 555
	cut.classify_bmi_teens_and_children()


def test_11():
	cut = class_test.Testexample(321,811,118)
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.bmi_value()
	cut.height = 396
	cut.age = 110
	cut.age = 6
	cut.classify_bmi_teens_and_children()


def test_12():
	cut = class_test.Testexample(321,811,118)
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.bmi_value()
	cut.height = 396
	cut.age = 110
	cut.age = 6
	cut.classify_bmi_teens_and_children()


def test_13():
	cut = class_test.Testexample(109,510,134)
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.bmi_value()
	cut.bmi_value()
	cut.bmi_value()
	cut.height = 931
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.age = 0
	cut.weight = 38
	cut.age = 145
	cut.weight = 187
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.bmi_value()


def test_14():
	cut = class_test.Testexample(124,70,79)
	cut.age = 3
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()


def test_15():
	cut = class_test.Testexample(544,989,5)
	cut.height = 500
	cut.classify_bmi_teens_and_children()
	cut.height = 233
	cut.height = 476
	cut.classify_bmi_teens_and_children()
	cut.height = 7
	cut.classify_bmi_teens_and_children()
	cut.height = 134
	cut.bmi_value()
	cut.weight = 608
	cut.classify_bmi_adults()
	cut.age = 148
	cut.bmi_value()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.height = 670
	cut.age = 70
	cut.age = 86
	cut.age = 59
	cut.weight = 219
