#!/usr/bin/env python
genero = ''
v1 = 0
v2 = 0
h = float(input("Digite sua altura: "))

while genero != 'm' and genero != 'h':
    genero = input("Escolha o gênero M ou H: ").lower()
    
if genero == 'h':
    genero = 'homem'
    peso_ideal = (72.7*h)-58
else:
    genero = 'mulher'
    peso_ideal = (62.1*h)-44.7
        
print(f'Para {genero}, com a altura {h} m, o peso ideal é {round(peso_ideal)}.')


