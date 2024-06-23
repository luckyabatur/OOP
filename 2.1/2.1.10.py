from string import ascii_letters, digits
import random


class EmailValidator:
    allowed = ascii_letters + digits + '_.'

    def __new__(cls):
        return None

    @classmethod
    def get_random_email(cls):
        email = random.sample(cls.allowed, random.randrange(1, 99))
        return f'{"".join(email)}@gmail.com'

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if (all(letter in cls.allowed + '@' for letter in email) and
                email.count('@') == 1 and len(email[:email.index('@')]) <= 100 and
                len(email[email.index('@'):]) <= 50 and
                email[email.index('@'):].count('.') >= 1 and
                '..' not in email):
            return True
        return False

    @staticmethod
    def __is_email_str(email):
        if isinstance(email, str):
            return True
        return False
