import math

# --- FONCTIONS MATHÉMATIQUES ---

def euclide_etendu(a, b):
    """Retourne (pgcd, u, v) tel que a*u + b*v = pgcd"""
    if a == 0:
        return b, 0, 1
    pgcd, u1, v1 = euclide_etendu(b % a, a)
    u = v1 - (b // a) * u1
    v = u1
    return pgcd, u, v

def resoudre_diophantienne(a, b, c):
    """Résout ax + by = c"""
    pgcd, u0, v0 = euclide_etendu(a, b)
    if c % pgcd != 0:
        return None
    facteur = c // pgcd
    return pgcd, u0 * facteur, v0 * facteur

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
    """Affiche une liste de nombres sous forme de tableau lisible"""
    if not liste:
        print("Aucun nombre premier trouvé.")
        return
    
    print(f"\nNombre(s) premier(s) trouvé(s) : {len(liste)}")
    print("-" * (colonnes * 8))
    
    for i in range(0, len(liste), colonnes):
        ligne = liste[i:i+colonnes]
        # On formate chaque nombre pour qu'il prenne 6 caractères d'espace
        print("".join(f"{num:^8}" for num in ligne))
    
    print("-" * (colonnes * 8))

# --- PROGRAMME PRINCIPAL ---

def menu():
    print("\n" + "="*40)
    print("      OUTIL D'ARITHMÉTIQUE COMPLET")
    print("="*40)
    print("1 : Calculer PGCD et PPCM")
    print("2 : Résoudre l'équation diophantienne (ax + by = c)")
    print("3 : Crible d'Ératosthène (Nombres premiers)")
    print("Q : Quitter")
    return input("\nVotre choix : ").upper()

while True:
    choix = menu()

    if choix == 'Q':
        print("Au revoir !")
        break

    try:
        if choix in ['1', '2']:
            a = int(input("Entrez a : "))
            b = int(input("Entrez b : "))
            
            pgcd, u, v = euclide_etendu(a, b)
            
            if choix == '1':
                ppcm = abs(a * b) // pgcd
                print(f"\n[RÉSULTATS]\nPGCD({a}, {b}) = {pgcd}\nPPCM({a}, {b}) = {ppcm}")
            
            elif choix == '2':
                c = int(input("Entrez c : "))
                sol = resoudre_diophantienne(a, b, c)
                if sol:
                    pg, x0, y0 = sol
                    print(f"\n[SOLUTION]\nUne solution : {a}({x0}) + {b}({y0}) = {c}")
                    print(f"Formule générale : x = {x0} + {b//pg}k  |  y = {y0} - {a//pg}k")
                else:
                    print(f"\nAucune solution : {c} n'est pas divisible par le PGCD ({pgcd})")

        elif choix == '3':
            n = int(input("Afficher les nombres premiers jusqu'à : "))
            liste_p = crible_eratosthene(n)
            afficher_tableau_premiers(liste_p)

        else:
            print("Choix invalide, recommencez.")

    except ValueError:
        print("\nErreur : Entrez des nombres entiers valides.")
