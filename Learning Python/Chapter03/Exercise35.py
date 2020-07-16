def print_horizontal(block_width, grid_width):
    for i in range(grid_width):
        print('+', end = ''), print((block_width - 1)*' - ', end = '')
    print('+')

def print_vertical(grid_width, block_height, block_width):
    for j in range(block_height):
        for i in range(grid_width):
            print('|', end = ''), print((block_width - 1)*'   ', end = '')
        print('|')
    
def build_grid(grid_height, grid_width, block_height, block_width):
    print_horizontal(block_width, grid_width)
    for i in range(grid_height):
        print_vertical(grid_width, block_height, block_width)
        print_horizontal(block_width, grid_width)

build_grid(2, 2, 4, 4) #grid_height, grid_width, block_width, block_height