
class Person:
    def __init__(self, name, age, id_number, email):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.email = email
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID Number: {self.id_number}")
        print(f"Email: {self.email}")
    
    def update_email(self, new_email):
        self.email = new_email
        print(f"Email updated to: {self.email}")


class Student(Person):
    def __init__(self, name, age, id_number, email, student_id, course, year_of_study):
        super().__init__(name, age, id_number, email)
        self.student_id = student_id
        self.course = course
        self.year_of_study = year_of_study
        self.grades = []
        self.fees_balance = 0
    
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print(f"Year of Study: {self.year_of_study}")
        print(f"Current GPA: {self.calculate_gpa()}")
        print(f"Fees Balance: ${self.fees_balance}")
    
    def add_grade(self, subject, grade):
        self.grades.append({"subject": subject, "grade": grade})
        print(f"Grade {grade} added for {subject}")
    
    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        total_points = sum(grade_info["grade"] for grade_info in self.grades)
        return round(total_points / len(self.grades), 2)
    
    def pay_fees(self, amount):
        self.fees_balance -= amount
        print(f"Paid ${amount}. Remaining balance: ${self.fees_balance}")
    
    def add_fees(self, amount):
        self.fees_balance += amount
        print(f"Fees of ${amount} added. Total balance: ${self.fees_balance}")


class Lecturer(Person):
    def __init__(self, name, age, id_number, email, employee_id, department, salary, subjects):
        super().__init__(name, age, id_number, email)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.subjects = subjects  
        self.office_hours = "Not set"
    
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary}")
        print(f"Subjects Teaching: {', '.join(self.subjects)}")
        print(f"Office Hours: {self.office_hours}")
    
    def set_office_hours(self, hours):
        self.office_hours = hours
        print(f"Office hours set to: {self.office_hours}")
    
    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f"Subject '{subject}' added to teaching list")
        else:
            print(f"Already teaching '{subject}'")
    
    def give_salary_raise(self, raise_amount):
        self.salary += raise_amount
        print(f"Salary raised by ${raise_amount}. New salary: ${self.salary}")


class Staff(Person):
    def __init__(self, name, age, id_number, email, employee_id, position, salary, department):
        super().__init__(name, age, id_number, email)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.department = department
        self.work_schedule = "9 AM - 5 PM"
    
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary}")
        print(f"Work Schedule: {self.work_schedule}")
    
    def set_work_schedule(self, schedule):
        self.work_schedule = schedule
        print(f"Work schedule updated to: {self.work_schedule}")
    
    def promote(self, new_position, salary_increase):
        old_position = self.position
        self.position = new_position
        self.salary += salary_increase
        print(f"Promoted from {old_position} to {new_position}")
        print(f"Salary increased by ${salary_increase}. New salary: ${self.salary}")
    
    def request_leave(self, days, reason):
        print(f"Leave request submitted: {days} days for {reason}")



def main():
    
    
    
    student1 = Student(
        name="Alice Johnson",
        age=20,
        id_number="ID001",
        email="alice.johnson@university.edu",
        student_id="STU2024001",
        course="Computer Science",
        year_of_study=2
    )
    
    
    lecturer1 = Lecturer(
        name="Dr. Robert Smith",
        age=45,
        id_number="ID002",
        email="robert.smith@university.edu",
        employee_id="EMP2021001",
        department="Computer Science",
        salary=75000,
        subjects=["Data Structures", "Algorithms"]
    )
    
   
    staff1 = Staff(
        name="Maria Garcia",
        age=35,
        id_number="ID003",
        email="maria.garcia@university.edu",
        employee_id="EMP2020001",
        position="Administrative Assistant",
        salary=45000,
        department="Student Affairs"
    )
    
    #
    print("1. STUDENT INFORMATION:")
    print("-" * 30)
    student1.display_info()
    print()
    
    student1.add_fees(5000)
    student1.add_grade("Mathematics", 85)
    student1.add_grade("Physics", 92)
    student1.add_grade("Chemistry", 78)
    student1.pay_fees(2000)
    print()
    
    print("Updated Student Information:")
    student1.display_info()
    print("\n" + "="*50 + "\n")
    
    
    print("2. LECTURER INFORMATION:")
    print("-" * 30)
    lecturer1.display_info()
    print()
    
    lecturer1.set_office_hours("Monday 2-4 PM, Wednesday 10-12 PM")
    lecturer1.add_subject("Machine Learning")
    lecturer1.give_salary_raise(5000)
    print()
    
    print("Updated Lecturer Information:")
    lecturer1.display_info()
    print("\n" + "="*50 + "\n")
    
    
    print("3. STAFF INFORMATION:")
    print("-" * 30)
    staff1.display_info()
    print()
    
    staff1.set_work_schedule("8 AM - 4 PM")
    staff1.promote("Senior Administrative Assistant", 5000)
    staff1.request_leave(5, "Family vacation")
    print()
    
    print("Updated Staff Information:")
    staff1.display_info()
    print("\n" + "="*50 + "\n")
    
    
    print("4. INHERITANCE DEMONSTRATION:")
    print("-" * 35)
    print("All objects can use parent class methods:")
    student1.update_email("alice.new@university.edu")
    lecturer1.update_email("robert.new@university.edu")
    staff1.update_email("maria.new@university.edu")

if __name__ == "__main__":
    main()