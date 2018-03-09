my_variable = 'hello'

grades = [77, 80, 90, 95, 100]
grades_tuple = (77, 80, 90, 95, 100, 105, 107, 90)
set_grades = {77, 80, 90, 100, 100}


def average(grades):
    return sum(grades) / len(grades)


set_grades.add(60)
set_grades.add(60)
# print(set_grades)

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_number = {1, 3, 5, 6, 9, 11}

# print(your_lottery_numbers.union(winning_number))
# print(your_lottery_numbers.intersection(winning_number))
# print({1, 2, 3, 4}.difference({1, 2}))
