class Student:
    def __init__(self, student_id, student_name, course, year_level):
        self.student_id = student_id
        self.name = student_name
        self.course = course
        self.year_level = year_level

class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.array = [None] * self.capacity

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

        print(f"Resized array to new capacity: {self.capacity}")

    def add(self, student):

        if self.size >= self.capacity:
            self.resize()

        self.array[self.size] = student
        self.size += 1

        print(f"Student added successfully")

    def display(self):
        if self.size == 0:
            print("No students in the record.")
            return

            print("\n=== Student Records ===")

            for i in range(self.size):
                student = self.array[i]
                print(f"\nStudent #{i + 1}:")
                print(f"Student ID: {student.student_id}")
                print(f"Student Name: {student.name}")
                print(f"Course: {student.course}")
                print(f"Year Level: {student.year_level}")

    def search(self, student_id):
        for i in range(self.size):
            if self.array[i].student_id == student_id:
                return i

        return -1

    def update(self, student_id, student_name, course, year_level):
        
        index = self.search(student_id)

        if index == -1:
            print("Student not found.")

            return

        self.array[index].name = student_name
        self.array[index].course = course
        self.array[index].year_level = year_level

        print("Student record updated successfully.")

    def remove(self, student_id):

        index = self.search(student_id)

        if index == -1:
            print("Student not found.")
            return

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1

        print("Student record removed successfully.")
        
    def display_array_information(self):
        print("\n=== Array Information ===")
        print(f"Current number of students: {self.size}")
        print(f"Current array capacity: {self.capacity}")

def main():

    students = DynamicArray()

    while True:
        print("\n================================")
        print("     STUDENT RECORD MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":

            print("\n=== Add Student ===")

            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            course = input("Enter Course: ")
            
            while True:
                try:
                    year_level = int(input("Enter Year Level: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer for Year Level.")

            student = Student(student_id, student_name, course, year_level)

            students.add(student)

        elif choice == "2":
            
            students.display()

        elif choice == "3":

            print("\n=== SEARCH STUDENT ===")

            student_id = input("Enter Student ID: ")

            index = students.search(student_id)

            if index == -1:

                print(f"Student not found.")

            else:

                student = students.array[index]

                print("\nStudent found:")
                print(f"Student ID: {student.student_id}")
                print(f"Student Name: {student.name}")
                print(f"Course: {student.course}")
                print(f"Year Level: {student.year_level}")

        elif choice == "4":

            print("\n=== UPDATE STUDENT ===")

            student_id = input("Enter Student ID to update: ")

            index = students.search(student_id)
            if index == -1:

                print("Student not found.")
            
            else:
                student_name = input("Enter new Student Name: ")
                course = input("Enter new Course: ")
                
                while True:
                    try:
                        year_level = int(input("Enter new Year Level: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                students.update(student_id, student_name, course, year_level)

        elif choice == "5":

            print("\n=== REMOVE STUDENT ===")

            student_id = input("Enter Student ID: ")
            students.remove(student_id)

        elif choice == "6":
            students.display_array_information()

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

main()