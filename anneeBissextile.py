# Cet exercice permet de determiner si une annee est bissextile ou non

annee = int(input("Donnez une année:"))

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 !=0):
    print("L'année {} est bissextile.".format(annee))

else:
    print("L'annee {} n'est pas bissextile.".format(annee))