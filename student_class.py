class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.name}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")


if __name__ == "__main__":
    main()
