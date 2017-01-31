ch = raw_input("Saisir chaine :") #saisie de la chaine
ch = ch.lower() #uniformisation des tailles des chars de la chaine

taille = len(ch) #calcul de la taille de ch

a = 100.0 * ch.count('a')/taille #pourcentage de a dans la chaine
t = 100.0 * ch.count('t')/taille #idem avec t
g = 100.0 * ch.count('g')/taille #idem avec g
c = 100.0 * ch.count('c')/taille #idem avec c

other = 100.0 - (a+t+g+c) #elements inconnus

print "il y a ", a, "% de a,",t, "% de t,",g, "% de g,",c, "% de c et", other,"% de caracteres non reconnus"
#affichage des donnees
