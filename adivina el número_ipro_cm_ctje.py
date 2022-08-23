# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from random import randint

if __name__ == '__main__':
	intentos = 10
	num_secreto = randint(0,99)+1
	print "Adivine el numero (de 1 a 100):"
	num_ingresado = raw_input()
	while num_secreto!=num_ingresado and intentos>1:
		if num_secreto>num_ingresado:
			print "El numero es mayor"
		else:
			print "El número es menor"
		intentos = intentos-1
		print "Le quedan ",intentos," intentos:"
		num_ingresado = float(raw_input())
	if num_secreto==num_ingresado:
		print "Genial, haz adivinado ",11-intentos," intentos."
	else:
		print "El numero era: ",num_secreto

