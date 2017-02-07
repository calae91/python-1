import colors
#on cherche a connaitre des caracteres inconnus dans une sequence
#si on a trop derreurs on sarrete 
ch = raw_input(colors.warning("saisir chaine : "))
ch = ch.upper()
nb_err = int(input (colors.warning("saisir nb erreur max : ")))
alphabet = "ATGC"
i = 0
error = 0
t =  ""
while i < len(ch) and error <= nb_err:
	if ch[i] not in alphabet :
		print colors.error("ERR NUM : " + str(error) + ", CHAR NUM : " + str(i))
		print "    " + colors.error(ch[i] + " N'EST PAS UN CARACTERE VALIDE")
		error += 1
		t += colors.error(ch[i])
	else :
		t += colors.success(ch[i])
	i+=1
if error == 0:
	print colors.success("Fin aucune erreur")
else :
	if (i < len(ch) -1) :
		print colors.error ("TROP D'ERREURS DANS LA SEQUENCE ARRET A : " + str(i))
		print colors.success("SEQ OBTENUE (incomplete) : " + t)
	else :
		print colors.success("IL Y A ") + colors.error(str(error)) + colors.success(" ERREURS DANS LA SEQ")
		print colors.success("SEQ OBTENUE : ") + t
