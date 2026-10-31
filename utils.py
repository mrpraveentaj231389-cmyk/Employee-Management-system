import csv
import logging
import requests
import json

#----------LOGGING----------

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(ascitime)s - %(levelname)s  - %(message)"
)

#----------OOP----------

class Employee:
    
    def __init__(self, emp_id, name, age, deaprtment, salary, skills):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.deapartment = deaprtment
        self.salary = salary
        self.skill = skills

    def display(self):

        print("\nEmployee Details")
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Department: {self.deapartment}")
        print(f"salary: {self.salary}")
        print(f"skills: {','.join(self.skills)}")

    def to_dict(self):
        return{
            "id":self.emp_id,
            "name":self.name,
            "age": self.age,
            "department":self.deapartment,
            "salary":self.salary,
            "skills": self.skills
            
            
            }

employees = []

#----------FUNCTIONS----------

def add_employee():
    try:
        emp_id = int(input("Enter ID:"))
        name = input("Enter Name:")
        age = int(input("Enter age:"))
        department = input("Enter Department:")
        salary = float(input("Enter salary:"))
        skills = input("Enter Skills:").split(",")

        skills = [skill.strip() for skill in skills]

        emp = Employee(
            emp_id,
            name,
            age, 
            department, 
            salary,
            skills,

        )

        employees.append(emp)

        with open("employee.txt", "a") as file:
            file.write(
                f"{emp_id}, {name}, {age}, {department}, {salary}, {skills}\n"

            )

        logging.info("Employee Added")

        print("Employee Added Successfully")

    except ValueError:
        print("Invalid input")

def view_employees():
    if not employees:
        print("No employees Found")
        return

    for emp in employees:
        emp.display()

def search_employee():

    try:
        search_id = int(input("Enter Employee ID: "))

        for emp in employees:
            if emp.emp_id == search_id:
                emp.display()
                logging.Info("Employee Searched")
                return

        print("Employee Not Found")

    except ValueError:
        print("Invalid ID")


def department_summary():

    dept_count = {}

    for emp in employees:

        if emp.department in dept_count:
            dept_count[emp.department] += 1
        else:
            dept_count[emp.department] = 1

    print("\nDepartment Summary")


    for dept, count in dept_count.items():
        print(dept, ":", count)


def Unique_skills():

    skills_set = set()

    for emp in employees:
        skills_set.update(emp.skills)

    print("\nUnique_skills")

    for skill in skills_set:
        print(skill)


def save_json():
    try:

        data = [emp.to_dict() for emp in employees]

        with open("backup.json", "w") as file:
            json.dump(data, file, indent=4)

        logging.info("JSON Backup Created")

        print("Backup saved")

    except Exception as e:
        print("Error:", e)


def load_csv():

    try:

        with open("employees.csv", "r" ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                emp = Employee(
                    int(row["id"]),
                    row["name"],
                    int(row["age"]),
                    row["deaprtment"],
                    float(row["salary"]),
                    row["skills"].split(";")
                )

                employees.append(emp)

        print("CSV Loaded Successfully")

    except FileNotFoundError:
        print("employees.csv File Not found")

def get_quote():

    try:

        response = requests.get(

            "http://api.quotale.io/random",
            timeout=5
        )

        data = response.json()

        print("\nMotivation Quote")
        print(data["content"])
        print("-",data["author"] )

    except Exception:
        print("API Request Failed")

#----------MENU----------

while True:

    print("\n===== Employee Management System =====")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Department Sumaary")
    print("5. Show Unique skills")
    print("6. Save JSON Backup")
    print("7. Load employee CSV")
    print("Get Motivation Quote")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()
    
    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        department_summary()

    elif choice == "5":
        Unique_skills()

    elif choice == "6":
        save_json()

    elif choice == "7":
        load_csv()

    elif choice == "8":
        get_quote()

    elif choice == "9":

        print("Thank You")
        break
    else:
        print("Invalid choice")








    
























    




















