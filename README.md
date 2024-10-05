# TP 1+2

## Exercice 1 : Chiffre de Vigenère

### Test 1 :

- Input : texte: `bonjour`, clé: `CLE`
- Output : `&<4.<;6`

### Test 2 :

- Input : texte: `je suis en informatique`, clé: `iut`
- Output : `p8AtI/:R7oS)/46!F5<:'`

### Test 3 :

- Input : texte: `J'ai 19 ans. Nous sommes en 10/2024.`, clé: `bUT._INfo`
- Output : ```-\6w_ZgfQQIb..9DZoVEB{E=NL^bfd=qY`z}```

## Exercice 2 : Déchiffrement du chiffre de Vigenère

### Test 1 :

- Input : texte: `&<4.<;6`,  clé: `CLE`
- Output : `bonjour`

### Test 2 :

- Input : texte: `p8AtI/:R7oS)/46!F5<:'`, clé: `iut`
- Output : `je suis en informatique`

### Test 3 :

- Input : texte: ```-\6w_ZgfQQIb..9DZoVEB{E=NL^bfd=qY`z}```, clé: `bUT._INfo`
- Output : `J'ai 19 ans. Nous sommes en 10/2024.`

## Exercice 3 : L'attaque de Kasiski

### Test 1:

- Input : fichier: `texteTD.txt`, (chiffré avec la clé "PARADIGM")
- Output : `8`

### Test 1:
- Input : fichier: `texte3000.txt`, (chiffré avec la clé "testcle")
- Output : `7`
