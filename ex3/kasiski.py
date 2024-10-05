def ouvrirFichier(fichier):
    try:
        with open(fichier, "r") as f:
            texte = f.read()
            return texte
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
        exit()
    
def gcd(a, b):
    """Calculer le PGCD de deux nombres."""
    while b:
        a, b = b, a % b
    return a


def trouverFragmentsRepetes(texte, longueurFragment):
    fragments = {}
    fragmentsRepetes = {} 

    for i in range(len(texte) - longueurFragment + 1):
        fragment = texte[i:i + longueurFragment]
        if fragment in fragments:
            fragments[fragment].append(i)
        else:
            fragments[fragment] = [i]

    for fragment, positions in fragments.items():
        if len(positions) > 1:
            fragmentsRepetes[fragment] = positions

    return fragmentsRepetes

def calculerDistances(positions):
    distances = []
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            distances.append(abs(positions[i] - positions[j]))
    return distances



def kasiski(texte):
    candidats = []
    temp = []
    longueurFragment = 3
    
    while len(temp) < 2 or temp[-1] == 1:
        fragmentRepetes = trouverFragmentsRepetes(texte, longueurFragment)

        repet = []

        for fragment, positions in fragmentRepetes.items():
            repet.extend(calculerDistances(positions))
        
        if repet:
            cleGCD = repet[0]
            for d in repet:
                cleGCD = gcd(cleGCD, d)
            temp.append(cleGCD)
        else:
            return '?'
            
        longueurFragment += 1

    for cle in temp:
        if cle != 1:
            candidats.append(cle)
    
    candidats = sorted(candidats, reverse=True)
    return candidats[0]

if __name__ == "__main__":
    fichier = input("Saisissez le nom du fichier: ")
    texte = ouvrirFichier(fichier)
    longueurCle = kasiski(texte)
    print(f"La longueur de la clé est : {longueurCle}")
