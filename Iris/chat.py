import torch 
import torch.nn as nn
from util import Eval , Net 
import time 

model = Eval()



data = torch.load("data.pth")



intents = model.load("intents.json")

model_state = data['model_state']
input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
tags = data['tags']
all_words = data['all_words']


net = Net(input_size,hidden_size,output_size)
net.load_state_dict(model_state)
net.eval()



while True:
	cmd = input("You:")


	if cmd in ['break','quit','stop','exit']:
		print("!!!! STOPPING BOT !!!!")
		break 
	if "time" in cmd:
		print("Time is " + time.ctime())
 
	x = model.tokenize(cmd)
	x =model.bag_of_words(x,all_words)
	x = x.reshape(1,x.shape[0])
	x=  torch.from_numpy(x)



	output = net(x)

	_,predicted = torch.max(output,dim=1)

	probs = torch.softmax(output,dim=1)
	prob = probs[0][predicted.item()]

	tag = tags[predicted.item()]


	if prob >= 0.75:
		for intent in intents['intents']:
			if tag == intent['tag']:
				print("Bot: {}".format(model.choose(intent['responses'])))
	else:
		print("Not In mY DATABASE")



	
		
			
	
