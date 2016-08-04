from radio import Radio

mi_radio = Radio("Sony")

desea_continuar = True

while desea_continuar == True:

	if not mi_radio.encendido:
		print(
	"""Su radio esta apagado. 
1. Encenderlo
2. Salir.""")
		encender_salir= int(input("Ingrese opcion elegida: "))

		if encender_salir == 1:
			mi_radio.encender()
		elif encender_salir == 2:
			print("Gracias por utilizar Radio, Adios.")
			desea_continuar == False
		else: 
			print("")
			print("Opcion invalida.")

	else:
		print("")
		print(
"""*MENU*
1. AM/FM
2. Subir Volumen
3. Bajar volumen
4. Subir estacion
5. Bajar estacion
6. Apagar
""")
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
			print("Opcion invalida")		

		