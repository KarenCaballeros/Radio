class Radio():
	def __init__(self,Sony):
		self.marca = marca
		self.encendido =  False
		self.volumen = 0
		self.emisora = 0
		self.emisoraAM = 0
		self.emisoraFM = 88.0
	def encender (self):
		self.encendido= True
	def apagar (self):
		self.encendido = False
	def subir_volumen (self):
		if self.volumen>= 100:
			self.volumen= 100
		else:
			self.volumen+= 5
	def bajar_volumen (self):
		if self.volumen <= 0:
			self.volumen = 0
	def subir_emirosa (self):
		if self.en_FM == True:
			self.emisora 
								