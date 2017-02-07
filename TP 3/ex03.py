import colors
#inverse complementaire
# dans le sens 5' 3'
# on a 
# TAGTCGTG
# et l'inverse en 3' 5'
# ATCAGCAC
ch = raw_input(colors.warning("saisir chaine : "))
ch = ch.upper()
i = 0
t =  ""
while i < len(ch):
	if ch[i] == 'T' :
		t = 'A' + t
	elif ch[i] == 'A' :
		t = 'T' + t
	elif ch[i] == 'G' :
		t = 'C' + t
	elif ch[i] == 'C' :
		t = 'G' + t
	else : 
		t += ""
	i += 1
print colors.success(t);
