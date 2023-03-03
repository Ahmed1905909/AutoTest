import re


class Login:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError('Invalid email.')
        else:
            self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password) < 6:
            raise ValueError('Invalid password.')
        else:
            self.__password = password

