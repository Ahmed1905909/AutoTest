import random
import string
import re

# Class that represents a solution. Contains a test suite and a fitness score
class Solution:
    test_suite = []
    fitness = -1

    def __init__(self):
        self.test_suite = []
        self.fitness = -1

    # Gets the average length of a test case
    def average_length(self):
        actions = 0.0

        for test in self.test_suite:
            actions += len(test)

        return actions / len(self.test_suite)


# Generates a test suite, containing between 1 and "max" test cases
# Each test case will contain 1 - "max" actions.
def generate_test_suite(metadata, max_test_cases, max_actions):
    num_test_cases = random.randint(1, max_test_cases)
    test_suite = []
    for i in range(num_test_cases):
        test_suite.append(generate_test_case(metadata, max_actions))
    return test_suite


# Generate a test case of length 1 - max number of actions
# A test case initializes the CUT, then performs actions on it
def generate_test_case(metadata, max_actions):
    test_case = []
    # Initialize the CUT
    test_case.append(generate_constructor(metadata))

    # Generate actions
    num_actions = random.randint(0, max_actions)
    for j in range(num_actions):
        test_case.append(generate_action(metadata))

    return test_case


def generate_constructor(metadata):
    # If there are no constructors, or if it has no parameters, create an empty
    # parameter list
    if "constructor" not in metadata.keys() or "parameters" not in \
            metadata["constructor"].keys() or \
            len(metadata["constructor"]["parameters"]) == 0:
        parameter_data = []
    else:
        parameter_data = metadata["constructor"]["parameters"]

    parameters = []

    for parameter in range(len(parameter_data)):
        if parameter_data[parameter]["type"] == "string":
            if "min" in parameter_data[parameter]:
                min_length = parameter_data[parameter]["min"]
            else:
                min_length = 5

            if "max" in parameter_data[parameter]:
                max_length = parameter_data[parameter]["max"]
            else:
                max_length = 10

            email = '"' + "".join([random.choice(string.ascii_letters + string.digits) for i in range(10)]) + "@gmail.com" + '"'
            parameters.append(email)

        elif parameter_data[parameter]["type"] == "password":
            if "min" in parameter_data[parameter]:
                min_length = parameter_data[parameter]["min"]
            else:
                min_length = 8

            if "max" in parameter_data[parameter]:
                max_length = parameter_data[parameter]["max"]
            else:
                max_length = 16

            password_chars = string.ascii_letters + string.digits + string.punctuation

            random_password = '"' + "".join(random.choices(password_chars, k=random.randint(min_length, max_length))) + '"'
            parameters.append(random_password)

        else:
            raise ValueError("Constructor parameter type not supported")

    return [-1, parameters]

# Generate a random action on the CUT
# Selects a random action, then generates random input for that action

def generate_action(metadata):
    which_action = random.randint(0, len(metadata["actions"]) - 1)

    if "parameters" in metadata["actions"][which_action].keys():
        parameter_data = metadata["actions"][which_action]["parameters"]
    else:
        parameter_data = []

    parameters = []

    for parameter in range(len(parameter_data)):
        if "type" in parameter_data[parameter]:
            if parameter_data[parameter]["type"] == "email":
                # Generate a random email address with double quotes
                email = "\"" + "".join([random.choice(string.ascii_letters + string.digits) for i in range(10)]) + "@gmail.com\""
                parameters.append(email)
            elif parameter_data[parameter]["type"] == "string":
                if "min" in parameter_data[parameter]:
                    min_length = parameter_data[parameter]["min"]
                else:
                    min_length = 1

                if "max" in parameter_data[parameter]:
                    max_length = parameter_data[parameter]["max"]
                else:
                    max_length = 1

                random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(min_length, max_length)))
                # Add double quotes to the generated string
                parameters.append('"' + random_string + '"')
            elif parameter_data[parameter]["type"] == "int":
                if "min" in parameter_data[parameter]:
                    min_value = parameter_data[parameter]["min"]
                else:
                    min_value = 0

                if "max" in parameter_data[parameter]:
                    max_value = parameter_data[parameter]["max"]
                else:
                    max_value = 0

                random_int = random.randint(min_value, max_value)
                parameters.append(random_int)
            elif parameter_data[parameter]["type"] == "password":
                if "min" in parameter_data[parameter]:
                    min_length = parameter_data[parameter]["min"]
                else:
                    min_length = 8

                if "max" in parameter_data[parameter]:
                    max_length = parameter_data[parameter]["max"]
                else:
                    max_length = 16

                password_chars = string.ascii_letters + string.digits + string.punctuation

                # Generate a random password with double quotes
                random_password = "\"" + "".join(random.choices(password_chars, k=random.randint(min_length, max_length))) + "\""
                parameters.append(random_password)
            else:
                raise ValueError("Action parameter type not supported")

    return [which_action, parameters]
