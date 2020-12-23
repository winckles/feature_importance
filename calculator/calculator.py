class Calculator:
    """
        A calculator class
        ...
        Attributes
        ----------
        memory : float
            The starting number for the operation
        Methods
        -------
        check_memory()
            checks the number in memory
        reset_memory()
            sets the number in memory to 0
        add(number)
            adds the number in memory with given number
        subtract(number)
            subtracts the number in memory with given number
        multiply(number)
            multiplies the number in memory by given number
        divide(number)
            divides the number in memory by given number
        take_root(number)
            take nth root of the number in memory
        """

    def __init__(self, memory: float = 0):
        """
        Calculator object accepts float or int as initial memory value
        Otherwise a TypeError is raised
        """
        if not isinstance(memory, (float, int)):
            raise TypeError
        self.__memory = memory

    @property
    def memory(self) -> float:
        return self.__memory

    def check_memory(self) -> str:
        """ Check the number in memory """
        return f"The number in memory is {self.__memory}"

    def reset_memory(self) -> str:
        """ Checks memory and sets it back to 0 """
        if self.__memory is not 0:
            self.__memory = 0
        return f"The number in memory is now {self.__memory}"

    def add(self, number=float) -> float:
        """ Returns the number in memory added by the provided number """
        self.__memory += number
        return self.__memory

    def subtract(self, number=float) -> float:
        """ Returns the number in memory subtracted by the provided number """
        self.__memory -= number
        return self.__memory

    def multiply(self, number=float) -> float:
        """ Returns the number in memory multiplied by the provided number """
        self.__memory *= number
        return self.__memory

    def divide(self, number=float) -> float:
        """
        Returns the number in memory divided by the provided number
        The provided number can't be 0
        """
        if number == 0:
            raise ZeroDivisionError
        self.__memory /= number
        return self.__memory

    def take_root(self, number=float) -> float:
        """
        Returns the nth root of the number in memory
        The provided number can't be 0
        """
        if number == 0:
            raise ZeroDivisionError
        self.__memory ** (1 / float(number))
        return self.__memory
