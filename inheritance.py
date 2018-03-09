class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        # return a new Student callend friend_name in the same school as self
        return cls(name=friend_name, school=origin.school, salary=salary)


## 

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


annaW = WorkingStudent('Anna', 'Oxford', 300)
friend = WorkingStudent.friend(annaW, 'Greg', 17.5)

print(friend.name, friend.school, annaW.salary)
print(friend.salary)