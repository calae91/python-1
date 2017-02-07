import colors
#inverse complementaire
# dans le sens 5' 3'
# on a 
# TAGTCGTG
# et l'inverse en 3' 5'
# ATCAGCAC
ch = raw_input(colors.warning("saisir chaine : "))
ch = ch.upper()
i = len(ch) - 1
t =  ""
while i >= 0:
	if ch[i] == 'T' :
		t += 'A'
	elif ch[i] == 'A' :
		t += 'T'
	elif ch[i] == 'G' :
		t += 'C'
	elif ch[i] == 'C' :
		t += 'G'
	else : 
		t = '!' + t
	i -= 1
print colors.success(t);
