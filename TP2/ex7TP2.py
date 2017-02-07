import colors
#exercice 7.1
ch = raw_input(colors.warning("saisir chaine : "))
n = input(colors.warning("Saisir le nombre de caracteres demandes : "))
verif = 0
#Exercice 7.3
while verif == 0:	
	i = input(colors.warning("Saisir les premiers(taper 1) ou les derniers caracteres (2) : "))
	if (i == 1) :
		#Exercice 7.1
		print (colors.success(ch[:n]))
		verif += 1
	elif (i == 2) :
	#Exercice 7.2
		print (colors.success(ch[len(ch) - n :]))
		verif += 1
	#Exercice 7.3
	else :
		print colors.error("erreur cette valeur n'est pas acceptee")
