from datetime import date

from application.salary import calculate_salary

from application.db.people import get_employees


def get_current_date():
    current_date = date.today()
    print(current_date)


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    get_current_date()
