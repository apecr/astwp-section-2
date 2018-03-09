lottery_player_one_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer('Rolf')
player_two = LotteryPlayer('John')
player_one.numbers = (1, 2, 3, 4, 5, 6)
# print(player_one.name, player_one.numbers)
# print(player_one.total())
# print(player_one.name == player_two.name)
# print(player_one.numbers == player_two.numbers)

##


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school_static():
        # Static method in Java
        print('I am going to school.')

    @classmethod
    def go_to_school_class(cls):
        # Static method in Java
        print('I am going to school.')
        print('I am {}'.format(cls))


anna = Student('Anna', 'MIT')
anna.marks = [92, 91, 100]
anna.go_to_school_class()
anna.go_to_school_static()
