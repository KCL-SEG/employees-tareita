"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from unicodedata import name


class Employee:
    def __init__(self, name, salary, hours, bonus, commission, contract_count):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.bonus = bonus
        self.commission = commission
        self.contract_count = contract_count
		
    def get_pay_per_hour(self):
        if self.hours != 0:
            return (self.hours * self.salary)
        else:
            return self.salary    

    def get_comission_pay(self):
        if self.commission != 0:
            return (self.commission * self.contract_count)
        elif self.bonus != 0:
            return self.bonus
        else:
            return 0    

    def get_pay(self):
        return self.get_pay_per_hour() + self.get_comission_pay()

    def check_comission(self):
        comission_string = f' and receives a commission for {self.contract_count} contract(s) at {self.commission}/contract'
        bonus_string = f' and receives a bonus commission of {self.bonus}'
        if self.commission != 0:
            return comission_string
        elif self.bonus != 0:
            return bonus_string
        else:
            return ''

    def __str__(self):
        comission_type = self.check_comission()
        name_string = f'{self.name} works on a '
        salary_string = ''
        total_pay_string = f' Their total pay is {self.get_pay()}.'

        if self.hours:
            salary_string = f'contract of {self.hours} hours at {self.salary}/hour{comission_type}. '
        else:
            salary_string = f'monthly salary of {self.salary}{comission_type}. '
        

        return name_string + salary_string + total_pay_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 0, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 600, 0, 0)

# print(str(ariel))
# print(ariel.get_comission_pay())
# print(ariel.get_pay_per_hour())
# print(ariel.get_pay())