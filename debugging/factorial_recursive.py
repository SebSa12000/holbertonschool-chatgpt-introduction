#!/usr/bin/python3  
# Spécifie l'interpréteur à utiliser pour exécuter le script (ici Python 3)
import sys  # Importe le module sys pour accéder aux arguments passés en ligne de commande

# Fonction récursive pour calculer la factorielle d'un nombre
def factorial(n):
    if n == 0:
        return 1  # La factorielle de 0 est définie comme étant 1
    else:
        return n * factorial(n-1)  # Appel récursif : n! = n * (n-1)!

# Récupère le premier argument de la ligne de commande (après le nom du script), le convertit en entier
f = factorial(int(sys.argv[1]))

# Affiche le résultat
print(f)