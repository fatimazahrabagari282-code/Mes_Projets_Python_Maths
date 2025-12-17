import math

# --- FONCTIONS MATHÉMATIQUES ---

def euclide_etendu(a, b):
    """Calcule le PGCD et les coefficients de Bézout (u, v)"""
    if a == 0:
        return b, 0, 1
    pgcd, u1, v1 = euclide_etendu(b % a, a)
    u = v1 - (b // a) * u1
    v = u1
    return pgcd, u, v

def crible_eratosthene(n):
    """Retourne la liste des nombres premiers jusqu'à n"""
    premiers = [True] * (n + 1)
    premiers[0] = premiers[1] = False
    for p in range(2, int(math.sqrt(n)) + 1):
        if premiers[p]:
            for i in range(p * p, n + 1, p):
                premiers[i] = False
    return [i for i, est_premier in enumerate(premiers) if est_premier]

# --- FONCTIONS D'AFFICHAGE ---

def afficher_tableau_premiers(liste, colonnes=10):
    """Affiche les nombres premiers sous forme de tableau"""
    if not liste:
        print("\nAucun nombre premier trouvé.")
        return
    print(f"\n[ RÉSULTAT : {len(liste)} nombres premiers trouvés ]")
    print("-" * (colonnes * 8))
    for i in range(0, len(liste), colonnes):
        ligne = liste[i:i+colonnes]
        print("".join(f"{num:^8}" for num in ligne))
    print("-" * (colonnes * 8))

# --- PROGRAMME PRINCIPAL ---

def menu():
    print("\n" + "="*45)
    print("      SOLVEUR MATHÉMATIQUE (ARITHMÉTIQUE)")
    print("="*45)
    print("1 : Calculer PGCD et PPCM")
    print("2 : Résoudre l'équation ax + by = c")
    print("3 : Crible d'Ératosthène (Nombres premiers)")
    print("Q : Quitter")
    return input("\nVotre choix : ").upper()

while True:
    choix = menu()

    if choix == 'Q':
        print("\nFin du programme. À bientôt !")
        break

    try:
        if choix in ['1', '2']:
            a = int(input("Entrez la valeur de a : "))
            b = int(input("Entrez la valeur de b : "))
            pgcd, u, v = euclide_etendu(a, b)
            
            if choix == '1':
                ppcm = abs(a * b) // pgcd
                print(f"\n>>> RÉSULTATS :")
                print(f"    PGCD({a}, {b}) = {pgcd}")
                print(f"    PPCM({a}, {b}) = {ppcm}")

            elif choix == '2':
                c = int(input("Entrez la valeur de c : "))
                print(f"\nÉquation à résoudre : {a}x + {b}y = {c}")
                
                if c % pgcd != 0:
                    print(f"\n[!] AUCUNE SOLUTION ENTIÈRE")
                    print(f"L'équation n'a pas de solution car le PGCD({pgcd}) ne divise pas {c}.")
                else:
                    # Calcul de la solution particulière
                    facteur = c // pgcd
                    x0 = u * facteur
                    y0 = v * facteur
                    
                    # Coefficients pour la solution générale
                    k_x = b // pgcd
                    k_y = a // pgcd

                    print(f"\n>>> 1. SOLUTION PARTICULIÈRE :")
                    print(f"    x0 = {x0}")
                    print(f"    y0 = {y0}")
                    print(f"    Vérification : {a}*({x0}) + {b}*({y0}) = {a*x0 + b*y0}")

                    print(f"\n>>> 2. SOLUTION GÉNÉRALE (k ∈ ℤ) :")
                    # On gère l'affichage des signes pour plus de clarté
                    signe_x = "+" if k_x >= 0 else ""
                    signe_y = "-" if k_y >= 0 else "+"
                    print(f"    x = {x0} {signe_x} {abs(k_x)}k")
                    print(f"    y = {y0} {signe_y} {abs(k_y)}k")

        elif choix == '3':
            limite = int(input("Jusqu'à quel nombre voulez-vous chercher ? "))
            liste_p = crible_eratosthene(limite)
            afficher_tableau_premiers(liste_p)

        else:
            print("\nChoix non reconnu. Veuillez taper 1, 2, 3 ou Q.")

    except ValueError:
        print("\nErreur : Veuillez saisir un nombre entier valide.")
