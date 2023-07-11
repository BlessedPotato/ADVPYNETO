from accountant import *
from accountant.db import *
from datetime import *

if __name__ == '__main__':

    people.get_employees()
    salary.calculate_salary()
    print(f'Current date is: {date.today()}')