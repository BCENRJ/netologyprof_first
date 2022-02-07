from main import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    # Get Current Date v1
    print(f'Текущая дата: {d.today()}')
    # v2
    print(f'Текущая дата: {d.today().strftime("%B %d, %Y")}')