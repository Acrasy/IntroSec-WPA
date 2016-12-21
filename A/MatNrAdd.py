with open("./pw-list/am-pass-full.txt","r") as list:

	table = list.read().strip().split()
	for i in range(len(table)):
		table[i] = table[i] + "1225253"

	with open('./pw-list/MatNr-pass.txt', mode='wt', encoding='utf-8') as myfile:
		myfile.write('\n'.join(table))




