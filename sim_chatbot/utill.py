import time,json,random,jellyfish ,re 
from nltk.tokenize import word_tokenize 
from nltk.stem.porter import PorterStemmer 

print("-" * 20 +" UTILL FUNCTION ACTIVATED " + "-"*20)

class Eval:
	def __init__(self):
		pass

	def current_time(self):
		return time.ctime()

	def load_(self,filename):
		with open(filename,"r") as f:
			file = json.load(f)

		return file 

	def tokenize(self,sentence):
		return word_tokenize(sentence)

	def stem(self,word):
		return PorterStemmer().stem(word)

	def sim(self,a,b,round_value=None):
		similarity = jellyfish.jaro_distance(a,b)

		if round_value is not None and isinstance(round_value,int):
			similarity= round(similarity,round_value)

		return similarity

	def choose(self,container):
		return random.choice(container)

	def fix(self,container=[],ignore=["?!."],lower=True):

		if lower is True:
			container = [word.lower() for word in container]
		container = [re.sub(f"{ignore}","",word) for word in container]

		return container

	def fix_cmd(self,cmd,ignore=["?!."],lower=True):
		cmd = self.fix([cmd],ignore,lower)

		return cmd[0]






