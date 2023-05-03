import class_test
import pytest


def test_0():
	cut = bmi_calculator.BMICalc(295,590,7)
	cut.weight = 114
	cut.age = 126
	cut.bmi_value()
	cut.height = 17
	cut.weight = 271
	cut.height = 76
	cut.bmi_value()
	cut.age = 143
	cut.classify_bmi_adults()
	cut.height = 743
	cut.classify_bmi_teens_and_children()


def test_1():
	cut = bmi_calculator.BMICalc(739,821,18)
	cut.age = 131
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.weight = 451
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.age = 41
	cut.weight = 480


def test_2():
	cut = bmi_calculator.BMICalc(932,721,126)
	cut.classify_bmi_adults()
	cut.height = 45
	cut.age = 33
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.height = 834
	cut.weight = 206
	cut.height = 688
	cut.weight = 770
	cut.height = 391
	cut.classify_bmi_adults()
	cut.weight = 844
	cut.weight = 893
	cut.bmi_value()
	cut.bmi_value()
	cut.weight = 957


def test_3():
	cut = bmi_calculator.BMICalc(628,676,141)
	cut.classify_bmi_teens_and_children()
	cut.age = 127
	cut.classify_bmi_adults()
	cut.age = 63
	cut.bmi_value()
	cut.age = 95
	cut.age = 144
	cut.weight = 530
	cut.classify_bmi_teens_and_children()


def test_4():
	cut = bmi_calculator.BMICalc(502,946,96)
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.weight = 598
	cut.classify_bmi_teens_and_children()
	cut.height = 746
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.weight = 562
	cut.classify_bmi_teens_and_children()
	cut.age = 14
	cut.height = 430
	cut.weight = 278
	cut.weight = 370
	cut.weight = 574
	cut.age = 48


def test_5():
	cut = bmi_calculator.BMICalc(846,331,94)
	cut.age = 74
	cut.weight = 422


def test_6():
	cut = bmi_calculator.BMICalc(804,892,60)
	cut.classify_bmi_adults()


def test_7():
	cut = bmi_calculator.BMICalc(309,798,101)
	cut.age = 150
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.weight = 681
	cut.height = 756
	cut.bmi_value()
	cut.bmi_value()
	cut.height = 416
	cut.age = 106


def test_8():
	cut = bmi_calculator.BMICalc(21,801,88)
	cut.height = 276
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.height = 637
	cut.weight = 350
	cut.classify_bmi_adults()


def test_9():
	cut = bmi_calculator.BMICalc(818,511,60)
	cut.classify_bmi_teens_and_children()
	cut.weight = 599
	cut.weight = 49
	cut.classify_bmi_adults()
	cut.weight = 996
	cut.weight = 706
	cut.age = 140
	cut.classify_bmi_adults()
	cut.age = 130
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.weight = 785
	cut.age = 113
	cut.bmi_value()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.height = 817


def test_10():
	cut = bmi_calculator.BMICalc(404,361,59)
	cut.age = 114
	cut.bmi_value()
	cut.age = 46
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.age = 103
	cut.age = 22
	cut.age = 83


def test_11():
	cut = bmi_calculator.BMICalc(836,68,68)
	cut.height = 819
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.height = 761
	cut.weight = 753
	cut.weight = 312
	cut.age = 51
	cut.height = 322
	cut.classify_bmi_adults()
	cut.weight = 127
	cut.bmi_value()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.height = 327
	cut.bmi_value()
	cut.weight = 381


def test_12():
	cut = bmi_calculator.BMICalc(333,471,116)
	cut.age = 68
	cut.classify_bmi_adults()


def test_13():
	cut = bmi_calculator.BMICalc(333,471,116)
	cut.age = 68
	cut.classify_bmi_adults()


def test_14():
	cut = bmi_calculator.BMICalc(206,97,35)
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.weight = 681
	cut.bmi_value()
	cut.age = 16
	cut.age = 74
	cut.age = 9
	cut.classify_bmi_adults()


def test_15():
	cut = bmi_calculator.BMICalc(206,97,35)
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.weight = 681
	cut.bmi_value()
	cut.age = 16
	cut.age = 74
	cut.age = 9
	cut.classify_bmi_adults()


def test_16():
	cut = bmi_calculator.BMICalc(124,686,81)
	cut.bmi_value()
	cut.height = 465
	cut.classify_bmi_teens_and_children()
