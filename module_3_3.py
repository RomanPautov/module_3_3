values_list = [5, True, 'str']
values_dict = {'a': 5, 'b': 'Roman', 'c': False}
values_list_2 = [9, 'home']


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2, 3)
print_params(b=25)
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)