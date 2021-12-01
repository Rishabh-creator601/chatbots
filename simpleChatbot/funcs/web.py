import webbrowser 


def open(cmd):
	model = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
	model.open(cmd)


open('python.org')