TABLEASCII = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
TAILLEASCII = len(TABLEASCII)

def inputText():
    return input("Saisissez votre texte clair à chiffrer/déchiffrer: ")

def inputKey():
    return input("Saisissez votre clé de chiffrement: ")

def verifCle(cle):
    for caractere in cle:
        if caractere not in TABLEASCII:
            return False
    return True

def verifTexte(texte):
    for caractere in texte:
        if caractere not in TABLEASCII:
            return False
    return True

def inputText():
    return input("Saisissez votre texte clair à chiffrer/déchiffrer: ")

def inputKey():
    return input("Saisissez votre clé de chiffrement: ")

def vigenere(texte, cle, mode):
    resultat = ""
    posCle = 0

    for lettre in texte:
        indexLettre = TABLEASCII.find(lettre)
        decalage = TABLEASCII.find(cle[posCle % len(cle)])
             
        if mode == "chiffrer":
            nouvellePos = (indexLettre + decalage) % TAILLEASCII
        else:
            nouvellePos = (indexLettre - decalage) % TAILLEASCII

        resultat += TABLEASCII[nouvellePos]
        posCle += 1 

    return resultat

def menu():
    choix = ""
    while choix not in ["1", "2", "3"]:
        print("1 - Chiffrer\n2 - Déchiffrer\n3 - Quitter")
        choix = input("Saisissez votre choix (1, 2, ou 3): ")
        if choix not in ["1", "2", "3"]:
            print("Choix invalide. Veuillez saisir 1, 2, ou 3.\n")
    return choix

def main():
    print("Chiffrement de Vigenère avec boucle majuscule-minuscule")
    choix = menu()

    while choix != "3":
        texte = inputText()
        cle = inputKey()
        
        if not verifTexte(texte) or not verifCle(cle):
            print("\nTEXTE OU CLE INVALIDE. VEUILLEZ RECOMMENCEZ !\n")
            continue
        
        if choix == "1":
            print("Texte chiffré:", vigenere(texte, cle, "chiffrer"))
        elif choix == "2":
            print("Texte déchiffré:", vigenere(texte, cle, "dechiffrer"))

        choix = menu()

    print("Au revoir")

def jeuEssais():
    print("######################################")
    print("############ JEU D'ESSAIS ############")
    print("######################################\n")

    print(
        "Chiffrement du texte clair 'bonjour' avec la cle 'CLE': "
        + vigenere("bonjour", "CLE", "chiffrer")
    )
    print(
        "\nDéchiffrement du texte chiffré '&<4.<;6' avec la cle 'CLE': "
        + vigenere("&<4.<;6", "CLE", "dechiffrer")
    )

    print("\n-----\n")

    print(
        "Chiffrement du texte clair 'je suis en informatique' avec la cle 'iut': "
        + vigenere("je suis en informatique", "iut", "chiffrer")
    )
    print(
        "\nDéchiffrement du texte chiffré 'T[t]k^]uZXu^X\\d\\cV^_f_[' avec la cle 'iut': "
        + vigenere("T[t]k^]uZXu^X\\d\\cV^_f_[", "iut", "dechiffrer")
    )

    print("\n-----\n")

    print(
        "Chiffrement du texte clair 'J'ai 19 ans. Nous sommes en 10/2024.' avec la cle 'bUT._INfo': "
        + vigenere("J'ai 19 ans. Nous sommes en 10/2024.", "bUT._INfo", "chiffrer")
    )
    print(
        "\nDéchiffrement du texte chiffré '-\\6w_ZgfQQIb..9DZoVEB{E=NL^bfd=qY`z}' avec la cle 'bUT._INfo': "
        + vigenere("-\\6w_ZgfQQIb..9DZoVEB{E=NL^bfd=qY`z}", "bUT._INfo", "dechiffrer")
    )

if __name__ == "__main__":
    # main() à décommenter pour choisir le texte et la clé à chiffrer ou déchiffrer
    #main()
    # jeux d'essais pour tester les algorithmes
    jeuEssais()
