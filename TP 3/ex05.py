import colors
#on cherche a connaitre des caracteres inconnus dans une sequence
#si on a trop derreurs on sarrete 
ch = raw_input(colors.warning("saisir chaine : "))
ch = ch.upper()
i = 0
error = 0
t =  ""
while i < len(ch)/2 and ch[i] == ch[len(ch)-i-1]:
		i+=1
		
if i == len(ch)/2:
	print colors.success ("votre sequence est un palindrome")
else :
	print colors.error("pas un palindrome")
