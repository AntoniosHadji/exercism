import re
import string


class Phone:
    def __init__(self, phone_number):
        pattern = re.compile(r"[\s" + string.punctuation + r"]")
        phone_number = pattern.sub("", phone_number)

        length = len(phone_number)
        if length > 11:
            raise ValueError("Too many numbers.")
        if length == 11:
            if phone_number[0] != "1":
                raise ValueError("Only US country codes supported")
            phone_number = phone_number[1:]

        if phone_number[0] in ["0", "1"]:
            raise ValueError("Area code can not begin with zero or one.")
        if phone_number[3] in ["0", "1"]:
            raise ValueError("Exchange code can not begin with zero or one.")

        self.area_code = phone_number[:3]
        self.number = phone_number

    def pretty(self):
        return "({}) {}-{}".format(self.area_code, self.number[3:6], self.number[6:])
