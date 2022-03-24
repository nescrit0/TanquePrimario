navegadores = ['chrome', 'firefox', 'opera', 'safari']
print('chrome' in navegadores)

navegadores1 = ['chrome', 'firefox', 'opera', 'safari']
print('edge' in navegadores1)

entrada = input('Introduce el nombre de un navegador:\n')
navegadores = ['chrome', 'firefox', 'opera', 'safari']
if entrada in navegadores:
    print('El navegador que buscas está en la lista.')
else:
    print('El navegador que buscas no está en la lista.')