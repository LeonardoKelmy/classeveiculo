# teste do carro

from veiculo import carro

meuCarro = carro('Ford', 'Mustang', 'chumbo', 0)

# Exibição do meu carro
print('\n\t\t\t -- Meu Carro -- \n')


for i in range(0, 250):
    meuCarro.acelerar()

# Exibição do meu carro acelerado
print('\n\t -- Meu Carro Acelerado -- \n')
print(meuCarro)

for i in range(0, 250):
    meuCarro.frear()

# Exibição do meu carro acelerado
print('\n\t -- Meu Carro Freado -- \n')
print(meuCarro)
