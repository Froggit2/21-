def print_params(a = 1, b = 'стр', c = True):
    print(a,b,c)
print_params()
print_params(a = 2,b = 2, c = 8)
print_params(5)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [2,'два',True]
values_dict = {'a':2,'b':4,'c':True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1,'два']           #все работает
print_params(*values_list_2,42)