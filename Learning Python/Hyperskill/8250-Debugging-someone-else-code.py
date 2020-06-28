import debugpy

def which_type(el):
    """ This function is needed to control which arguments are passed further. """
    debugpy.breakpoint()
    if type(el) is 'str':                      # 1st line
        debugpy.breakpoint()
        print('The string has been given.')    # 2nd line
    else:                                      # 3rd line
        debugpy.breakpoint()
        print('Another type has been given.')  # 4th line

for element in [3, 'three', ['3'], {'three'}]:
    print(which_type(element))