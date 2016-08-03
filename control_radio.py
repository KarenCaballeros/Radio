from radio import Radio
mi_radio = Radio("Sony")
desea_continuar = True
while desea_continuar == True:
	"""
	   *MENU*
	1. AM/FM
	2. Subir Volumen
	3. Bajar volumen
	4. Subir estacion
	5. Bajar estacion
	6. Apagar
	"""
	opcion_elegida= input("Ingrese opcio elegida: ")

	if opcion_elegida == 1:
		mi_radio.cambiar_frecuencia()
	elif opcion_elegida == 2:
		mi_radio.subir_volumen()
	elif opcion_elegida == 3:
		mi_radio.bajar_volumen()	
	elif opcion_elegida == 4:
		mi_radio.subir_emisora()
	elif opcion_elegida == 5:
		mi_radio.bajar_emisora()
	elif opcion_elegida == 6:
		mi_radio.apagar()
	else:
		"Opcion invalida"		

		