import colors
#on remplace les t par des u 
ch = raw_input(colors.warning("saisir chaine : "))
ch = ch.upper()
i = 0
while i < len(ch) - 1 :
	if ch[i] == 'T' :
		print colors.success('U')
	else :
		print colors.warning(ch[i])
	i += 1
