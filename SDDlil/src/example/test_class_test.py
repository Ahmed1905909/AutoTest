import class_test
import pytest


def test_0():
	cut = class_test.Testexample(915,794,119)
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.weight = 984
	cut.age = 50
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.weight = 723
	cut.weight = 444
	cut.height = 901


def test_1():
	cut = class_test.Testexample(324,79,105)
	cut.classify_bmi_teens_and_children()
	cut.weight = 213
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()


def test_2():
	cut = class_test.Testexample(892,78,125)
	cut.bmi_value()
	cut.height = 277
	cut.weight = 336
	cut.classify_bmi_adults()
	cut.height = 543
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.height = 833
	cut.bmi_value()
	cut.age = 114
	cut.classify_bmi_adults()
	cut.weight = 212
	cut.age = 147
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()


def test_3():
	cut = class_test.Testexample(319,321,56)
	cut.classify_bmi_adults()
	cut.weight = 534
	cut.age = 17
	cut.age = 120
	cut.classify_bmi_teens_and_children()
	cut.height = 474
	cut.height = 289
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.height = 569
	cut.age = 106
	cut.classify_bmi_adults()
	cut.weight = 289
	cut.age = 81
	cut.bmi_value()
	cut.weight = 450
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()


def test_4():
	cut = class_test.Testexample(615,967,3)
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()


def test_5():
	cut = class_test.Testexample(618,17,63)
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.age = 8
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.height = 426
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.weight = 734
	cut.weight = 345
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.age = 143


def test_6():
	cut = class_test.Testexample(954,24,116)
	cut.weight = 746
	cut.bmi_value()
	cut.classify_bmi_adults()


def test_7():
	cut = class_test.Testexample(954,24,116)
	cut.weight = 746
	cut.bmi_value()
	cut.classify_bmi_adults()


def test_8():
	cut = class_test.Testexample(190,360,81)
	cut.height = 323
	cut.classify_bmi_adults()


def test_9():
	cut = class_test.Testexample(988,267,88)
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.weight = 273


def test_10():
	cut = class_test.Testexample(427,344,68)
	cut.age = 17
	cut.classify_bmi_teens_and_children()
	cut.weight = 640
	cut.weight = 861
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.weight = 712
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.weight = 853
	cut.height = 422
	cut.height = 665
	cut.bmi_value()
	cut.bmi_value()
	cut.age = 127
	cut.height = 443
	cut.classify_bmi_adults()
	cut.height = 940


def test_11():
	cut = class_test.Testexample(970,330,-1)
