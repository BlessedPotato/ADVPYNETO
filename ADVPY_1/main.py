from accountant import salary
from accountant import people
from datetime import date


if __name__ == '__main__':

    people.get_employee()
    salary.calculate_salary()
    print(f'Current date is: {date.today()}')
