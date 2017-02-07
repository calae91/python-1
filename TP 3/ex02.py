import colors
#on remplace les t par des u 
ch = raw_input(colors.warning("saisir chaine : "))
ch = ch.upper()
i = 0
transcrit =  ""
while i < len(ch) :
	if ch[i] == 'T' :
		transcrit += 'U'
	else :
		transcrit += ch[i]
	i += 1
print colors.success(transcrit);
