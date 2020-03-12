class Personne:
    """ Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence 
    """
    def __init__(self): # Notre méthode constructeur
        """Constructeur de notre classe. Chaque attribut va être instancié
        avec une valeur par défaut... original"""
        self.nom = "Goumou"
        self.prenom = "Jean Penan" # Quelle originalité
        self.age = 33 # Cela n'engage à rien
        self.lieu_residence = "Athis-Mons"

if __name__ == "__main__":
    p = Personne()
    print("Mon nom: ",p.nom)
    print("Mon prénom: ",p.prenom)
    print("Mon age: ",p.age)
    print("Mon lieu de résidence: ", p.lieu_residence)