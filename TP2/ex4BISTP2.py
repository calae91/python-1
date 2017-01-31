ch1 = raw_input("saisir chaine char :")
ch1 = ch1.lower()
ch2 = raw_input("saisir seconde chaine :")
ch2 = ch2.lower()
if ch2 in ch1 :
	print ch2, "present dans", ch1
else :
	print "erreur ch2 n'est pas dans ch1"
