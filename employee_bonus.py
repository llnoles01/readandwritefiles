import csv

with open("EmployeePay.csv","r") as emp_pay:
    read_file = csv.reader(emp_pay)

    for row in read_file:
        
        emp_id = row [0]
        first_name = row [1]
        last_name = row [2]
        salary = row [3]
        bonus = row [4]

        print(f" Employee ID: {emp_id}")
        print(f"First name: {first_name}")
        print(f"Last name: {last_name}")
        print(f"Salary: {salary}")
        print(f"Bonus: {bonus}")
