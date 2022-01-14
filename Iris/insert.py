from JSONDB import JsonDB 
 
import json 


print("Imported")

model = JsonDB()
model.clear()

greetings = model.create("greeting",["hello","hi","how are you ?","Hello","Hey"],
	["hi","how can i Help You","Hey $$","Hi **","@@ HELLO @@"])

goodbye = model.create("goodbye",["bye","goodbye","bye bye","Good Bye","i have to go now"],
	["bye","Yes , ok","Can we quit now?  type 'quit' To exit","Have a Good Day"])


items = model.create("items",["what you have","menu please","please Give me menu","what you sell","what items do you have","items ?"],
	["we have potatoes,tomatoes,onions Right Now","Potatoes and tomatoes"])

order = model.create("order",["i have to order","order now ","order it","please bring some"],
	["ok , your order ios being in processed","order booked sir !","your order is booked"])


about = model.create("about",["what is your name","your name","can i know your name","your naam"],
	["My name is Iris","$$ Iris $$","My name is %% Iris %%"])


bts = model.create("bts",["what you know about bts","what is bts","please tell me about bts"],
	["BTS - BORN TO SUSPEND","bts is very bad band","They are Very Bad"])





model.addM([greetings,goodbye,items,order,about,bts])

model.commit("intents.json")