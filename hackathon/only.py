
def onlyint(str):
	while(True):
		try:
			i=int(input(str))
			return i
			
		except:
			print('Enter Only Integers')
