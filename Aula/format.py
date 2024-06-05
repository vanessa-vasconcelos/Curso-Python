a = 'AAAAAAA'
b = 'B'
C = 1.1
string = 'a = {} b = {} c = {:.2f}'
string = 'a = {0} b = {1} c = {2:.2f}' # Com indices
formato = string.format(a, b, C)
print(formato)