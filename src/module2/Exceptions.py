class InvalidSalaryError(Exception):
    pass


def calculate(salary):
    if salary <= 0:
        raise InvalidSalaryError("salary must be greater than zero")
    print("Employee salary", salary)


try:
 calculate(-5000)

except InvalidSalaryError as error:
 print("Error:", error)

 