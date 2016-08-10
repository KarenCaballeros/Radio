from radio import Radio

mi_radio = Radio("Sony")

desea_continuar = True

while desea_continuar == True:

	if not mi_radio.encendido:
		print("")
		print(
"""SU RADIO ESTA APAGA. 
1. Encenderlo
2. Salir.""")
		encender_salir= int(input("Ingrese opcion elegida: "))

		if encender_salir == 1:
			mi_radio.encender()
		elif encender_salir == 2:
			print("Gracias por utilizar Radio, Adios.")
			desea_continuar = False
		else: 
			print("")
			print("Opcion invalida.")

	else:
		print("")
		print("ESTADO ACTUAL DE RADIO")
		print("Marca del radio: " , mi_radio.marca)
		print("Encendido: " , mi_radio.encendido)	
		if mi_radio.en_FM == True:
			print("Emisora: FM")
			print("Estacion: " , mi_radio.emisoraFM)
		else:
			print("Emisora: AM") 
			print("Estacion: " , mi_radio.emisoraAM)
		print("Volumen: " , mi_radio.volumen)
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
		opcion_elegida= int(input("Ingrese opcion elegida: "))

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
			print("")
			continuar= input("Si desea continuar escriba si: ")	
			if continuar == "si":
				desea_continuar = True
			else:
				desea_continuar = False	
		else:
			print("Opcion invalida")

			

		

		