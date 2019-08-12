grid_height = 4
grid_width = 4
block_width = 7
block_height = 2

def print_horizontal(width_in, amount_horizontal):
    for i in range(amount_horizontal):
        print('+', end = ''),print((width_in-1)*'-', end = '')
    print('+')
def print_vertical(amount_horizontal, block_height):
    for j in range(block_height):
        for i in range(amount_horizontal):
            print('|', end = ''),print((block_width-1)*' ', end = '')
        print('|')
    
def build_grid(grid_height,block_width, grid_width):
    print_horizontal(block_width,grid_width)
    for i in range(grid_height):
        print_vertical(grid_width, block_height)
        print_horizontal(block_width,grid_width)
#print_horizontal(block_width, grid_width)
#print_vertical(grid_width, block_height)
build_grid(grid_height,block_width,grid_width)