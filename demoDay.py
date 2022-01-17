class Person():
    def __init__(self, name, gender, dob):
        self.name = name
        self.gender = gender
        self.dob = dob

    def description_person(self):
        print("Ten: " + self.name)
        print("Gioi tinh: " + self.gender)
        print("Ngay sinh: " + str(self.dob))


class Student(Person):
    def __init__(self, name, gender, dob, code, gpa, email):
        super().__init__(name, gender, dob)
        self.code = code
        self.gpa = gpa
        self.email = email

    def description_student(self):
        super().description_person()
        print("Ma sinh vien: " + self.code)
        print("Diem trung binh: " + str(self.gpa))
        print("Email: " + self.email)

    def check_scholarship(self):
        if self.gpa >= 3.2:
            print(self.name + " co duoc hoc bong")
        else:
            print(self.name + " khong duoc hoc bong")


student = Student("Kien", "Nam", 8, "B19DCCN348", 3.19, "kiendq.b19cn348@stu.ptit.edu.vn")
student.description_student()
student.check_scholarship()
