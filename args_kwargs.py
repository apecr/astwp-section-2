def my_method(arg1, arg2):
    return arg1 + arg2

# print(my_method(5, 6))


def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6


def my_list_addition(list_arg):
    return sum(list_arg)


my_long_method(3, 4, 8, 12, 76, 87)
my_list_addition([3, 4, 8, 12, 76, 87])


def addition_simplified(*args):
    return sum(args)

# print(addition_simplified(3, 4, 8, 12, 76, 87))
# print(my_long_method(3, 4, 8, 12, 76, 87))

##


def what_are_kwargs(*args, name, location):
    print(args)
    print(name)
    print(location)


what_are_kwargs(12, 34, 56, name='Joe', location='UK')
