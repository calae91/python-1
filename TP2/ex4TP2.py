ch1 = raw_input("saisir chaine char :")
ch2 = raw_input("saisir seconde chaine :")
if ch1.count(ch2) :
	print ch2, "present dans", ch1
else :
	print "erreur ch2 n'est pas dans ch1"
