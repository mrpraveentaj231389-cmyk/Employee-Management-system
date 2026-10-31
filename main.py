import csv
import json
import requests
import logging

# ---------------- LOGGING ----------------

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- OOP ----------------

class Employee:
    def __init__(self, emp_id, name, age, department, salary, skills):
        self.emp_id = emp_id
        self.name = name.title()
        self.age = age
        self.department = department
        self.salary = salary
        self.skills = skills

    def display(self):
        print("\nEmployee Details")
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print(f"Skills: {', '.join(self.skills)}")

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary,
            "skills": self.skills
        }


employees = []


# ---------------- FUNCTIONS ----------------

def add_employee():
    try:
        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        skills = input("Enter Skills(comma separated): ").split(",")

        skills = [skill.strip() for skill in skills]

        emp = Employee(
            emp_id,
            name,
            age,
            department,
            salary,
            skills
        )

        employees.append(emp)

        with open("employees.txt", "a") as file:
            file.write(
                f"{emp_id},{name},{age},{department},{salary},{skills}\n"
            )

        logging.info("Employee Added")

        print("Employee Added Successfully")

    except ValueError:
        print("Invalid Input")


def view_employees():
    if not employees:
        print("No Employees Found")
        return

    for emp in employees:
        emp.display()


def search_employee():

    try:
        search_id = int(input("Enter Employee ID: "))

        for emp in employees:
            if emp.emp_id == search_id:
                emp.display()
                logging.info("Employee Searched")
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


def unique_skills():

    skills_set = set()

    for emp in employees:
        skills_set.update(emp.skills)

    print("\nUnique Skills")

    for skill in skills_set:
        print(skill)


def save_json():

    try:

        data = [emp.to_dict() for emp in employees]

        with open("backup.json", "w") as file:
            json.dump(data, file, indent=4)

        logging.info("JSON Backup Created")

        print("Backup Saved")

    except Exception as e:
        print("Error:", e)


def load_csv():

    try:

        with open("employees.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                emp = Employee(
                    int(row["id"]),
                    row["name"],
                    int(row["age"]),
                    row["department"],
                    float(row["salary"]),
                    row["skills"].split(";")
                )

                employees.append(emp)

        print("CSV Loaded Successfully")

    except FileNotFoundError:
        print("employees.csv File Not Found")


def get_quote():

    try:

        response = requests.get(
            "https://api.quotable.io/random",
            timeout=5
        )

        data = response.json()

        print("\nMotivational Quote")
        print(data["content"])
        print("-", data["author"])

    except Exception:
        print("API Request Failed")


# ---------------- MENU ----------------

while True:

    print("\n===== Employee Management System =====")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Department Summary")
    print("5. Show Unique Skills")
    print("6. Save JSON Backup")
    print("7. Load Employee CSV")
    print("8. Get Motivation Quote")
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
        unique_skills()

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
        print("Invalid Choice")