employees = []

def add_employee(emp_id, name, specialties, improvement_areas):
    employee = {
        "emp_id": emp_id,
        "name": name,
        "specialties": specialties,
        "improvement_areas": improvement_areas,
        "performance_score": 0
    }
    employees.append(employee)
    print("Employee added successfully.")

def evaluate_employee_performance(emp_id, score):
    for employee in employees:
        if employee["emp_id"] == emp_id:
            employee["performance_score"] = score
            print("Employee performance evaluated successfully.")
            return
    print("Employee not found.")

def view_employee_performance():
    if not employees:
        print("No employees available.")
    else:
        print("Employee Performance:")
        for employee in employees:
            print("Employee ID: ",employee['emp_id'])
            print(f"Name: {employee['name']}")
            print(f"Specialties: {', '.join(employee['specialties'])}")
            print(f"Areas for Improvement: {', '.join(employee['improvement_areas'])}")
            print(f"Performance Score: {employee['performance_score']}")
            print("-------------------------")

def employee_menu():
    while True:
        print("\n--- Employee Menu ---")
        print("1. View employee performance")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            view_employee_performance()

        elif choice == "2":
            print("Exiting the employee menu...")
            break

        else:
            print("Invalid choice. Please try again.")

def manager_menu():
    while True:
        print("\n--- Manager Menu ---")
        print("1. Add an employee")
        print("2. Evaluate employee performance")
        print("3. View employee performance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            specialties = input("Enter employee specialties (separated by commas): ").split(",")
            improvement_areas = input("Enter areas for improvement (separated by commas): ").split(",")
            add_employee(emp_id, name, specialties, improvement_areas)

        elif choice == "2":
            emp_id = input("Enter employee ID to evaluate performance: ")
            score = float(input("Enter performance score: "))
            evaluate_employee_performance(emp_id, score)

        elif choice == "3":
            view_employee_performance()

        elif choice == "4":
            print("Exiting the manager menu...")
            break

        else:
            print("Invalid choice. Please try again.")

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Employee Menu")
        print("2. Manager Menu")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            employee_menu()

        elif choice == "2":
            manager_menu()

        elif choice == "3":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")
main_menu()
