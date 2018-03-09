class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        # return a new Student callend friend_name in the same school as self
        return cls(friend_name, origin.school, *args)

## 

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


annaW = WorkingStudent('Anna', 'Oxford', 300, 'Software Developer')
friend = WorkingStudent.friend(annaW, 'Greg', 17.5, 'Professor')

print(friend.name, friend.school, annaW.salary)
print(friend.salary)