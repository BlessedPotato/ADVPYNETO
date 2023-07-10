from accountant.client import *
from accountant.db.salary import *
from datetime import *

if __name__ == '__main__':

    people.get_employee()
    salary.calculate_salary()
    print(f'Current date is: {date.today()}')