#effectue addition, soustraction, division et multiplication à la demande de l'utilisateur
# avec les nombres entrés par celui-ci
# entrer "diviser", "multiplier", "addition" ou "soustraire" dans le premier argument

def calculer(op, x, y):


    res = 0

    if op == "diviser":
        res = x/y
    elif op == "multiplier":
        res = x*y
    elif op == "addition":
        res = x+y
    elif op == "soustraire":
        res = x-y
    else:
        res = "Entrez une des 4 opérations svp"

    print(res)

#Exemple:

calculer("multiplier", 10, 2)
