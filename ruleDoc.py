
cond1 = '111'
cond2 = '110'
cond3 = '101'
cond4 = '100'
cond5 = '011'
cond6 = '010'
cond7 = '001'
cond8 = '000'

responses = []
for i in range(0,256):
	responses.append(0)
	responses[i] = bin(i)[2:]
	prepend = []
	for j in range(0,8-len(responses[i])):
		prepend.append('0')
	prestring = ''
	for zero in prepend:
		prestring = prestring + zero
	responses[i] = prestring + responses[i]

rules = {}
i = 0
for response in responses:
	rules[i] = {}
	rules[i][cond1] = response[0]
	rules[i][cond2] = response[1]
	rules[i][cond3] = response[2]
	rules[i][cond4] = response[3]
	rules[i][cond5] = response[4]
	rules[i][cond6] = response[5]
	rules[i][cond7] = response[6]
	rules[i][cond8] = response[7]

	i += 1

doc = open('ruleDoc.xml','w')

tabLvl = 0

doc.write('<rules>\n')

for k,v in rules.items():
	doc.write('\t<rule>\n')
	doc.write('\t\t<name>' + str(k) + '</name>\n')

	for cond,resp in v.items():
		doc.write('\t\t<condition>\n')
		doc.write('\t\t\t<locality>\n')
		doc.write('\t\t\t\t<left>' + cond[0] + '</left>\n')
		doc.write('\t\t\t\t<self>' + cond[1] + '</self>\n')
		doc.write('\t\t\t\t<right>' + cond[2] + '</right>\n')
		doc.write('\t\t\t</locality>\n')
		doc.write('\t\t\t<response>' + resp + '</response>\n')
		doc.write('\t\t</condition>\n')

	doc.write('\t</rule>\n')



doc.write('</rules>')

doc.close()
