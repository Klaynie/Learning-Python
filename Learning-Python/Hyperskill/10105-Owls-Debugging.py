def nighttime(func):
    def wrapper(args):
        print('It is nighttime')
        return func(args)

    return wrapper


@nighttime
def get_message(name):
    print('We can hear some night birds like', name)


get_message('owls')
