from util import Eval,Net 
import torch
import torch.nn as nn 



model = Eval()


intents = model.load("intents.json")



all_words = []
tags = []
xy = []



for intent in intents['intents']:
	tag = intent['tag']
	tags.append(tag)

	for pattern in intent['patterns']:

		w = model.tokenize(pattern)

		all_words.extend(w)
		xy.append((w,tag))


all_words = [model.stem(word) for word in all_words  if word not in ["?","!",".",","]]
all_words = sorted(set(all_words))

tags = sorted(set(tags))




x_train = []
y_train  = []



for (word,label) in xy:
	bag = model.bag_of_words(word,all_words)

	x_train.append(bag)


	tag = tags.index(label)

	y_train.append(tag)



dataset = model.dataset(x_train,y_train)



input_size = len(x_train[0])
hidden_size = 8
output_size = len(tags)
num_epochs = 1000

net = Net(input_size,hidden_size,output_size)
optimizer = torch.optim.Adam(net.parameters(),lr=0.001)
criterion = nn.CrossEntropyLoss()


for i in range(num_epochs):
	for (data,label) in dataset:
		label = label.to(dtype=torch.long)

		outputs = net(data)


		loss = criterion(outputs,label)


		optimizer.zero_grad()
		loss.backward()
		optimizer.step()

	if i % 100 == 0:
		print("Loss : {} Epoch : {}".format(loss.item(),i))


print("Final Loss : {}".format(loss))



data = {
	"model_state":net.state_dict(),
	"input_size":input_size,
	"hidden_size":hidden_size,
	"output_size":output_size,
	"tags":tags,
	"all_words":all_words
}



torch.save(data,"data.pth")


print("file saved")