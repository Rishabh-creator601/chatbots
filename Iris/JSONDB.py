import json 


class JsonDB:
	def __init__(self,filename=None):
		if filename is None:
			self.filename = {"intents":[]}
		else:
			self.filename = self.load(filename)


	def add(self,value={}):
		self.filename['intents'].append(value)

	def addM(self,values=[]):
		for value in values:
			self.add(value)

	def show(self):
		return self.filename


	def commit(self,filename,indent=4):
		with open(filename,"w") as f:
			json.dump(self.filename,f)
		f.close()

	def load(self,filename):
		with open(filename,"r") as f:
			data = json.load(f)
		return data 

	def create(self,tagname=None,patterns=[],responses=[]):
		data = {'tag':tagname,"patterns":patterns,"responses":responses}
		return data 

	def clear(self):
		self.filename = {"intents":[]}



