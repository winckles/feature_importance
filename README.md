## Calculator

Calculator is a Python package that provides formulas for basic mathmetic computations such as:

| Formula    | Description | 
|------------|-------------|
|`check_memory` | Check the number in memory |
|`reset_memory`| Checks memory and sets it back to 0|
| `add`      | Returns the number in memory added by the provided number|
| `subtract` | Returns the number in memory subtracted by the provided number            |
| `divide`   |  Returns the number in memory multiplied by the provided number           |
| `multiply` |  Returns the number in memory divided by the provided number. The provided number can't be 0           |
| `take_root`     |  Returns the nth root of the number in memory. The provided number can't be 0           |


Table of content
* [Installation](#installation)
* [Getting Started](#getting-started)
* [Technologies Used](#technologies)
* [Contributing](#contributing)
* [License](#license)


### Installation

To run this calculator package please take a look at the following instructions

1. Install the package
```
pip install git+https://github.com/winckles/calculator_package.git`
```
2. Import the class
```
from calculator_package import Calculator
```
3. Create an object and use the functions
```
calculator = Calculator()
calculator.add(5)
```

### Getting Started
This calculator package lets you perform basic arithmetic functions, and the calculator stores the result in its memory. More explanation on arithmetic can be found [here](https://courses.lumenlearning.com/boundless-algebra/chapter/introduction-to-arithmetic-operations/#:~:text=Key%20Points-,The%20basic%20arithmetic%20operations%20for%20real%20numbers%20are%20addition%2C%20subtraction,%2C%20associative%2C%20and%20distributive%20properties)

### Technologies
* Python 3.9
* Pytest 6.2.1
* Setuptools 51.1.0


### Contributing
Please let me know if you encounter a bug by filing an issue, all contributions are appreciated!

If you plan to contribute new features please send a PR.

### License
Calculator has a MIT-style license, as found in the [LICENSE](LICENSE) file.
