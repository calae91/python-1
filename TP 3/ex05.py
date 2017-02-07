import colors
#on cherche a connaitre des caracteres inconnus dans une sequence
#si on a trop derreurs on sarrete 
ch = raw_input(colors.warning("saisir chaine : "))
ch = ch.upper()
ch = ch.replace(" ", "")
i = 0
err = 0
while i < len(ch)/2 and err < 1:
	if ch[i] == 'T' and ch[len(ch) -i-1] != 'A':
		err += 1
	elif ch[i] == 'A' and ch[len(ch) -i-1] != 'T' :
		err +=1
	elif ch[i] == 'G' and ch[len(ch) -i-1] != 'C' :
		err +=1
	elif ch[i] == 'C' and ch[len(ch) -i-1] != 'G' :
		err +=1
	else :
		i+=1
		
if err == 0 :
	print colors.success ("INVERTED REPEAT")
else :
	print colors.error("NOT INVERTED REPEAT")
