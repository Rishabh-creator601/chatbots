from utill import Eval 
from settings import botname,threshold ,stops ,byecmd

model = Eval()


intents = model.load_("intents.json")




for intent in intents['intents']:

	intent['patterns'] = model.fix(intent['patterns'])
	intent['responses'] = model.fix(intent['responses'])








	
		
			



while True:
	cmd = input("You: ")
	cmd = model.fix_cmd(cmd)
	for intent in intents['intents']:
		for pattern in intent['patterns']:
			if model.sim(cmd,pattern,2) >= threshold:
				print(f"{botname}: {model.choose(intent['responses'])}")


	if cmd in stops or cmd in byecmd:
		print("Stopping..")
		break 

	if "time" in cmd:
		print(f"{botname}: Current Time is {model.current_time()}")







			











