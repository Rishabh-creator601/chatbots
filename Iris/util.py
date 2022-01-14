from nltk.tokenize import word_tokenize 
from nltk.stem.porter import PorterStemmer 
from torch.utils.data import Dataset,DataLoader 
from JSONDB import JsonDB 
import numpy as np 
import torch ,random 
import torch.nn as nn 

print("-"*20 + "Utils activated" + "-"*20)




class ChatDataset(Dataset):
	def __init__(self,x,y):
		self.x_train = x
		self.y_train = y

	def __len__(self):
		return len(self.x_train)

	def __getitem__(self,idx):
		return self.x_train[idx], self.y_train[idx]





class Eval(JsonDB):
	def __init__(self):
		pass

	def tokenize(self,sentence):
		return word_tokenize(sentence)

	def stem(self,word):
		return PorterStemmer().stem(word)

	def dataset(self,x,y,batch_size=10,shuffle=True,num_workers=0):
		data = ChatDataset(x,y)
		data = DataLoader(data,batch_size=batch_size,shuffle=shuffle,num_workers=num_workers)
		return data 

	def bag_of_words(self,tokenized_words,all_words):
		tokenized_words = [self.stem(word) for word in tokenized_words]

		bag = np.zeros(len(all_words),dtype=np.float32)

		for idx, w in enumerate(all_words):
			if w in tokenized_words:
				bag[idx] = 1
		return bag 

	def choose(self,container):
		return random.choice(container)








class Net(nn.Module):
	def __init__(self,a,b,c):
		super(Net,self).__init__()
		self.l1 = nn.Linear(a,b)
		self.l2 = nn.Linear(b,b)
		self.l3 = nn.Linear(b,c)
		self.relu = nn.ReLU()

	def forward(self,x):
		x = self.relu(self.l1(x))
		x  = self.relu(self.l2(x))
		x=  self.l3(x)

		return x 

