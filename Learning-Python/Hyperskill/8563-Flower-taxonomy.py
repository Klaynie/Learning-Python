iris = {}

def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    global iris
    iris[id_n] = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
    if len(kwargs) != 0:
        for key, value in kwargs.items():
            iris[id_n][key] = value

add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')

print(iris)