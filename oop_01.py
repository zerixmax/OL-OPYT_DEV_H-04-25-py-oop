from datetime import datetime


class Person():
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 vat_id: str,
                 email: str,
                 phone: str,
                 date_of_birth: str = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.vat_id = vat_id
        self.email = email
        self.phone = phone
        self._date_of_birth = date_of_birth

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_dob(self) -> datetime:
        return datetime.strptime(self._date_of_birth, '%Y-%m-%d')



class Employee(Person):
    def __init__(self,
                 employee_id: str,
                 job_description: str,
                 first_name: str,
                 last_name: str,
                 vat_id: str,
                 email: str,
                 phone: str,
                 date_of_birth: str = ''):
        super().__init__(first_name, last_name, vat_id, email, phone, date_of_birth)
        self.employee_id = employee_id
        self.job_description = job_description


class Customer(Person):
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 vat_id: str,
                 email: str,
                 phone: str,
                 date_of_birth: str = '',
                 is_important: bool = False):
        super().__init__(first_name, last_name, vat_id, email, phone, date_of_birth)
        self.is_important = is_important




employee = Employee('007',
                    'CEO',
                    'Pero',
                    'Peric',
                    '123456',
                    'pero.peric@email.hr',
                    '09_ 1234 567',
                    '1998-01-28')

customer = Customer('Joza',
                    'Jozic',
                    '987654',
                    'joza.jozic@email.hr',
                    '09_ 9876 543',
                    '1998-02-28',
                    True)


print(employee)
print(employee.last_name)
print(employee.get_dob())

print()
print(customer)
print(customer.get_dob())
