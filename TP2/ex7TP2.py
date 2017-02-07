#exercice 7.1
ch = raw_input("saisir chaine : ")
n = input("Saisir le nombre de caracteres demandes : ")

#Exercice 7.3
i = input("Saisir les premiers(taper 1) ou les derniers caracteres (2) : ")
if (i == 1) :
#Exercice 7.1
	print (ch[:n])
elif (i == 2) :
#Exercice 7.2
	print (ch[len(ch) - n :])
#Exercice 7.3
else :
	print "erreur cette valeur n'est pas acceptee"
