import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('In the decorator!')
        func()
        print('After the decorator')
    return function_that_runs_func

@my_decorator
def a_function():
    print('I am the function')

# a_function()

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print('I am the decorator {}'.format(number))
            if number == 56:
                print('Not running the function!')
            else:
                func(*args, **kwargs)
            print('After the decorator')
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(42)
def my_function_too(x, y):
    print(x, y)

my_function_too(57,67)