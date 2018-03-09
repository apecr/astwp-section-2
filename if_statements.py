# should_continue = True
# if should_continue:
#     print('Hello')

# known_people = ['John', 'Anna', 'Mary']
# person = input('Enter the person you know: ')

# if person in known_people:
#     print('You know {}!'.format(person))
# else:
#     print('You don\'t know {}!'.format(person))

## Exercise

def who_do_you_know():
    # Ask the user for a list of people they know
    # Split the string into a list
    # return that list
    string_list_users = input('Write a list of people you know ')
    return [person.strip() for person in string_list_users.split(',')]


def ask_user():
    name = input('Name a friend of yours ')
    if name in who_do_you_know():
        print('You know {}!'.format(name))
    else:
        print('You dont know {}!'.format(name))
    # Ask user for a name
    # See if their name is in the list of people they know
    # Print out that they know the person

ask_user()