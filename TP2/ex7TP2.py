class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#exercice 7.1
ch = raw_input(bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKGREEN + 'saisir chaine : ' + bcolors.ENDC )
n = input(bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKGREEN + 'Saisir le nombre de caracteres demandes : ' + bcolors.ENDC)

#Exercice 7.3
i = input(bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKGREEN + 'Saisir les premiers(taper 1) ou les derniers caracteres (2) : ' + bcolors.ENDC)
if (i == 1) :
#Exercice 7.1
	print (bcolors.WARNING + ch[:n] + bcolors.ENDC)
elif (i == 2) :
#Exercice 7.2
	print (bcolors.WARNING + ch[len(ch) - n :] + bcolors.ENDC)
#Exercice 7.3
else :
	print bcolors.BOLD + bcolors.FAIL + 'erreur cette valeur n est pas acceptee' + bcolors.ENDC
