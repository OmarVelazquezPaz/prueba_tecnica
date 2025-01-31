import os

class InvalidNumber(Exception):
    """Custom Error for an invalid number."""

class MissingNumber:
    def __init__(self):
        self._numbers_lst = [x for x in range(1,101)]
        self._sum_numbers = sum(x for x in range(1,101))
        
    
    def _validate_number(self,number):
        if number >= 0 and number <= 100:
            return number
        else:
            raise InvalidNumber("Number out of range")
    
    def extact(self,remove):
        remove = self._validate_number(remove)
        for i in range(len(self._numbers_lst)):
            if self._numbers_lst[i] == remove:
                self._numbers_lst.pop(i)
                break
        print(self._numbers_lst)
    

    
    def calculate_missing_number(self):
        return self._sum_numbers - sum(self._numbers_lst)


def main():
    print("Enter a number between 1 and 100, included: ")
    remove_number = input(">> ")
    try:
        remove_number = int(remove_number)
    except ValueError as e:
        print("Not a number! ",e)
    else:
        number = MissingNumber()
        print(number.extact(remove_number))
        print("Missing Number: ",number.calculate_missing_number())

if __name__ == '__main__':
    os.system('clear')
    main()