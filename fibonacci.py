# exercice 2: Calculer la somme des "n" premiers termes de la suite de Fibonacci.

class Fibo:
	def __init__(self, nb): # Définition du constructeur
		self.n = nb
		
	def run(self): # Définition de la méthode run
		i = 2
		sum_fibo = 0
		# création d'un tableau de int, on initialise la suite fibonacci
		fibo = []
		fibo.append(0)
		fibo.append(1)
		while (i < self.n):
			new_fibo = fibo[i-1]+fibo[i-2]
			fibo.append(new_fibo)
			sum_fibo += new_fibo
			i = i + 1
		return(sum_fibo)

class FiboSecond:
	def __init__(self, nb): # Définition du constructeur
		self.n = nb

class FiboThird:
	def __init__(self, nb): # Définition du constructeur
		self.n = nb

myObj = Fibo(30)
myObj.run()

