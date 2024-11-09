#!/usr/bin/env python
peso_estabelecido = 50.00
multa_quilo = 4.00

peso_pescado = float(input("Digite o peso pescado: "))
excesso = peso_pescado - peso_estabelecido
valor_multa = excesso * multa_quilo

print(f'Excesso de {excesso} quilos e a multa é de R${valor_multa}')