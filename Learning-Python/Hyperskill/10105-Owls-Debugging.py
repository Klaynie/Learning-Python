def nighttime(func):
    def wrapper():
        print('It is nighttime')
        return func()

    return wrapper


@nighttime
def get_message(name):
    print('We can hear some night birds like', name)


get_message('owls')
