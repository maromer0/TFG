color = 'verde'.title()
match color:
    case 'Rojo':
        print('Rojo es un color primario.')
    case 'Azul':
        print('Azul es un color primario.')
    case 'Amarillo':
        print('Amarillo es un color primario.')
    case _:
        print(f'{color} no es un color primario.')
