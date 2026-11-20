from dataclasses import dataclass

@dataclass
class Employee:

    employee_id: int
    employee_name: str
    department: str

employee=Employee(101,"Ravi","Dev") 

print(employee)
print(employee.employee_id)