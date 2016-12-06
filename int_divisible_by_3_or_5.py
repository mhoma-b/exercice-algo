#exercice 1: Calculer la somme des entiers divisible par 3 ou par 5 entre 1 et n.

class N : # Définition de notre classe
	def __init__(self, nb): # Définition du constructeur
		self.n = nb

	def run(self): # Définition de la méthode run
		i = 0 # la variable qu'on incrémentera
		sum_int = 0 # la variable qui stockera la somme de tous les entiers divisibles par 3 ou 5
		while(i < self.n): # tant que i < à l'entier limite
			if( i%3 ==0) or (i%5 == 0): # on vérifie que i est divisible par 3 ou 5
				sum_int += i
			i = i + 1 # on incrémente i
		return(sum_int)

	#def get_classes(): #définition de get_classes()
		#en cours...

myObj = N(30)
myObj.run();
