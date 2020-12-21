class Calculator:
  def __init__(self, number_1: int, number_2: int):
        self.__number_1 = number_1
        self.__number_2 = number_2
        self.__memory = 0

    @property
    def number_1(self) -> int:
        return self.__number_1

    @property
    def numer_2(self) -> int:
        return self.__number_2

    @property
    def memory(self) -> int:
        return self.__memory


    def check_memory(self) -> str:
        """ Check the number in memory """
        return f"The number in memory is {self.__memory}%"


    def reset_memory(self):
        """ Resets the memory back to 0 """
        self.check_memory()
        if self.__memory is not 0:
            self.__memory = 0


    def add(self, number_1, number_2) -> int:
        """ Returns number_1 + number_2 """
        return number_1 + number_2

    
    def subtract(self, number_1, number_2) -> int:
        """ Returns number_1 - number_2 """
        return number_1 - number_2


    def multiply(self, number_1, number_2) -> int:
        """ Returns number_1 * number_2 """
        return number_1 * number_2


    def divide(self, number_1, number_2) -> int:
        """ Returns number_1 / number_2 """
        return number_1 / number_2
    
