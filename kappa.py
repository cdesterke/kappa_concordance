# -*-coding:Latin-1 -*

"""
Created on Mon Apr 27 20:23:34 2015
Kappa coefficient of concordance
@author: Christophe Desterke
email : christophe.desterke@gmail.com
python3.4
"""
import os

continued = True

while continued:

	print("	--------------------------------")
	print("	Kappa Coefficient of Concordance")
	print("	--------------------------------")
	
	variable = input ("Enter the name of your variable: ")

#this software allows the determination of Kappa coefficient of a binomial qualitative variable on a sample
#of subjects in group case or control
#kappa coefficient allows to distinguish observed concordance from the hasard concordance

#enter the numbers by group and declaration of the variables in float format

	CasePos = input ("Enter the number of positive cases: ")
	try:
		CasePos = float (CasePos)
	except ValueError:
		print('	Enter an integrer number!')
		continue
	
	CaseNeg = input ("Enter the number of negative cases: ")
	try:
		CaseNeg = float (CaseNeg)
	except ValueError:
		print('	Enter an integrer number!')
		continue	

	ControlPos = input ("Enter the number of positive controls: ")
	try:
		ControlPos = float (ControlPos)
	except ValueError:
		print(' Enter an integrer number!')
		continue 	

	ControlNeg = input ("Enter the number of negative controls: ")
	try:
		ControlNeg = float (ControlNeg)
	except ValueError:
		print('	Enter an integrer number !')
		continue

#calculation of intermediate variables		

	TotalCase = CasePos + CaseNeg
	print('The total number of cases is = ', TotalCase)

	TotalControl = ControlPos + ControlNeg
	print('The total number of controls is = ', TotalControl)

	TotalPos = CasePos + ControlPos
	print('The total number of positive subjects is = ', TotalPos)

	TotalNeg = CaseNeg + ControlNeg
	print('The total number of negative subjects is = ', TotalNeg)

#calculation of total number N 
	N = TotalControl + TotalCase

#calculation of observed concordance
	CO = (CasePos + ControlNeg) / N

#calculation of concordance linked to random
	CH = ((TotalCase * TotalPos) + (TotalControl * TotalNeg)) / (N * N)

#calculation of kappa score
	Kappa = (CO - CH) / (1 - CH)


	print("The total number of subjects is: ", N)
	print("The observed concordance is: ", CO)
	print("The concordance linked to random is: ", CH)
	print("The KAPPA coefficient of concordance is: ", Kappa)

#interpretation of kappa coefficient
	if Kappa < 0.5:
		print("The concordance is linked to random!")
	else:
		print("The concordance is well observed!")

		
#interaction for saving the result in an exit file named KAPPA_RESULTS	

	add =  input('Do you want to add the results to the file KAPPA_RESULTS.txt (y/n)? ')
	if add == "y" or add == "Y":
		
#file of exit
		variable = str (variable)
		CasePos = str (CasePos)
		CaseNeg = str (CaseNeg)
		ControlPos = str (ControlPos)
		ControlNeg = str (ControlNeg)
		N = str (N)
		CO = str (CO)
		CH = str (CH)
		Kappa = str (Kappa)
			
		mon_fichier = open ("KAPPA_RESULTS.txt", "a")
		mon_fichier.write ("---------------------------------------------------------------------")
		mon_fichier.write ("\n")
		mon_fichier.write ("Kappa Concordance on the variable: "+ variable + "\n")
		mon_fichier.write ("Number of positive cases: "+ CasePos + "\n")
		mon_fichier.write ("Number of negative cases: "+ CaseNeg + "\n")
		mon_fichier.write ("Number of positive controls: "+ ControlPos + "\n")
		mon_fichier.write ("Number of negative controls: "+ ControlNeg + "\n")
		mon_fichier.write ("Total number of subjects: "+ N + "\n")
		mon_fichier.write ("Observed concordance: "+ CO + "\n")
		mon_fichier.write ("Concordance linked to random: "+ CH + "\n")
		mon_fichier.write ("Kappa coefficient of concordance: " + Kappa + "\n")
	
		mon_fichier.close()
		
#interaction for the end of the software	

	end =  input('Do you want to end the software (y/n)? ')
	if end == "y" or end == "Y":
		continued = False


os.system("pause")
