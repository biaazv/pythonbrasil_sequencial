#!/usr/bin/env python
media = 0
for i in range (4):
	nota = float(input("Digite a nota: "))
	media+=nota
	print(media)
print(f"A média é {media/4}")
