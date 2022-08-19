import re


class ValidCarNumber:

    def __init__(self, number):
        self.number = number

    def is_valid(self, number):
        is_valid = re.search(r"0[1-9]KG([0-9]{3})(([A-Z]{3})|([A-Z]{2}))", number)
        try:
            if number[is_valid.start():is_valid.end()] == number:
                return "номер машины валидный!"
        except:
            return "номер машины инвалидный!!!"


print(ValidCarNumber(None).is_valid(number=input('введите номер машины: ')))