class Radio():
	def __init__(self, marca):
		self.marca = marca
		self.encendido =  False
		self.volumen = 0
		self.en_FM = True
		self.emisoraAM = 300
		self.emisoraFM = 87.0
	def encender(self):
		self.encendido= True
	def apagar(self):
		self.encendido = False
	def subir_volumen(self):
		if self.volumen>= 100:
			self.volumen= 100
		else:
			self.volumen+= 5
	def bajar_volumen(self):
		if self.volumen <= 0:
			self.volumen = 0
		else:
			self.volumen -= 5	
	def subir_emisora(self):
		if self.en_FM == True:
			if self.emisoraFM > 107.0:
				self.emisoraFM = 87.0
			else:
				self.emisoraFM += 0.5
		elif self.en_FM == False:
			if self.emisoraAM > 1300:
				self.emisoraAM = 300
			else:
				self.emisoraAM += 40	
	def bajar_emisora(self):
		if self.en_FM == True:
			if self.emisoraFM < 87.0:
				self.emisoraFM = 107.0
			else:
				self.emisoraFM -= 0.5
		elif self.en_FM == False:
			if self.emisoraAM < 300:
				self.emisoraAM = 1300
			else:
				self.emisoraAM -= 40
	def cambiar_frecuencia(self):
		if self.en_FM == True:
			self.en_FM = False
		else:
			self.en_FM = True												

								