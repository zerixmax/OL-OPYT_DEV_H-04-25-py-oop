


class Employee():
    def __init__(self,
                 employee_id: str,
                 job_description: str,
                 first_name: str,
                 last_name: str,
                 vat_id: str,
                 email: str,
                 phone: str,
                 date_of_birth: str = ''):
        self.employee_id = employee_id
        self.job_description = job_description
        self.first_name = first_name
        self.last_name = last_name
        self.vat_id = vat_id
        self.email = email
        self.phone = phone
        self.date_of_birth = date_of_birth


class Customer():
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 vat_id: str,
                 email: str,
                 phone: str,
                 date_of_birth: str = '',
                 is_important: bool = False):
        self.first_name = first_name
        self.last_name = last_name
        self.vat_id = vat_id
        self.email = email
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.is_important = is_important



