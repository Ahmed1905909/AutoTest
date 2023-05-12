class TempCalc:

    def __init__(self, fahrenheit, celsius):
        self.fahrenheit = fahrenheit
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.__fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        if fahrenheit <= -40 or fahrenheit >= 140:
            raise ValueError('Invalid fahrenheit.')
        else:
            self.__fahrenheit = fahrenheit

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, celsius):
        if celsius <= -40 or celsius >= 60:
            raise ValueError('Invalid celsius.')
        else:
            self.__celsius = celsius

    def fahrenheit_value(self):
        # convert to fahrenheit.
        fahrenheit_value = (self.celsius * 9 / 5) + 32
        return fahrenheit_value

    def celsius_value(self):
        # convert to celsius
        celsius_value = (self.fahrenheit - 32) * 5 / 9
        return celsius_value



