def print_horizontal(width_in, amount_horizontal):
    for i in range(amount_horizontal):
        print('+', end = ''),print((width_in-1)*'-', end = '')
    print('+')

def print_vertical(amount_vertical, block_height, block_width):
    for j in range(block_height):
        for i in range(amount_vertical):
            print('|', end = ''),print((block_width-1)*' ', end = '')
        print('|')
    
def build_grid(grid_height, grid_width, block_width, block_height):
    print_horizontal(block_width, grid_width)
    for i in range(grid_height):
        print_vertical(grid_width, block_height, block_width)
        print_horizontal(block_width, grid_width)

build_grid(10, 10, 8, 2) #grid_height, grid_width, block_width, block_height