parameter_dict = {
    'h': 10e-6,
    'a': .95e-6,
    'b': 1e-6,
    'Rm': 0.1,
    'Cm': 1e-2,
    'rho_i': 1,
    'rho_e': 1,
    'M2': 500000,
    'N2': 1000,
    'I_hat': 1e-6,
    'W': 0
}

positions = [(i, j) for i in range(0, 4) for j in range(0, 3)]

for (row, col), (key, value) in zip(positions, parameter_dict.items()):
    print('row = ' + str(row) + ', col = ' + str(col) + ', key = ' + key + ', value = ' + str(value))
    parameter_dict[key] = 'a'

for value in parameter_dict.values():
    print(value)