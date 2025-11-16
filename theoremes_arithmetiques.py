import math

# =================================================================
# Algorithme d'Euclide Étendu (PGCD)
# =================================================================
def euclide_etendu(a, b):
    """
    Calcule le PGCD(a, b) et les coefficients de Bézout (x0, y0)
    tels que a*x0 + b*y0 = PGCD(a, b).
    Retourne (d, x0, y0).
    """
    a_original, b_original = a, b
    a_abs, b_abs = abs(a), abs(b)
    
    if a_abs == 0 and b_abs == 0:
        return 0, 0, 0
    
    r_prev, r_curr = a_abs, b_abs
    x_prev, x_curr = 1, 0
    y_prev, y_curr = 0, 1
    
    # Boucle de l'algorithme d'Euclide
    while r_curr != 0:
        quotient = r_prev // r_curr
        r_prev, r_curr = r_curr, r_prev - quotient * r_curr
        x_prev, x_curr = x_curr, x_prev - quotient * x_curr
        y_prev, y_curr = y_curr, y_prev - quotient * y_curr

    d = r_prev
    x0_abs, y0_abs = x_prev, y_prev
    
    # Ajustement des signes pour correspondre aux a et b originaux
    x0 = x0_abs * (1 if a >= 0 else -1)
    y0 = y0_abs * (1 if b >= 0 else -1)
        
    # Vérification et ajustement final si nécessaire
    if a * x0 + b * y0 != d:
        x0 = -x0
        y0 = -y0
        
    return d, x0, y0

# =================================================================
# Calcul du PPCM
# =================================================================
def ppcm(a, b):
    """
    Calcule le PPCM(a, b) en utilisant la relation PGCD * PPCM = |a * b|.
    """
    # 1. Obtenir le PGCD
    d, _, _ = euclide_etendu(a, b)
    
    if d == 0:
        return 0 # Si a=0 et b=0, PGCD=0, PPCM=0
    
    # 2. Calculer le PPCM
    # Utilisation de abs() pour un PPCM positif et // pour l'entier.
    return abs(a * b) // d 

# =================================================================
# Crible d'Ératosthène
# =================================================================
def crible_eratosthene(n):
    """
    Détermine tous les nombres premiers inférieurs ou égaux à n.
    """
    if n < 2:
        return []

    # Initialisation du crible
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while (p * p) <= n:
        if is_prime[p]:
            # Marquer tous les multiples de p (à partir de p*p) comme non-premiers
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
        
    # Extraction des nombres premiers
    primes = [i for i, est_premier in enumerate(is_prime) if est_premier]
    
    return primes

# =================================================================
# Programme Principal
# =================================================================
if __name__ == "__main__":
    
    print("="*60)
    print("=== 1. PGCD, PPCM et Résolution Diophantienne (ax + by = c) ===")
    print("="*60)
    
    try:
        a = int(input("Entrez la valeur de a : "))
        b = int(input("Entrez la valeur de b : "))
        c = int(input("Entrez la valeur de c : "))
    except ValueError:
        print("\nERREUR : Veuillez entrer uniquement des nombres entiers pour a, b, c.")
        exit()

    d, x0, y0 = euclide_etendu(a, b)
    m = ppcm(a, b)
    
    print(f"\n✅ Le PGCD de {a} et {b} est : **{d}**")
    print(f"✅ Le PPCM de {a} et {b} est : **{m}**")
    
    if c % d != 0:
        print(f"\n❌ Pas de solution entière pour l'équation : PGCD({d}) ne divise pas c={c}.")
    else:
        # Calcul de la solution particulière (xp, yp) et générale
        k_facteur = c // d
        xp = x0 * k_facteur
        yp = y0 * k_facteur
        alpha = b // d
        beta = -a // d
        
        print(f"\n⭐ Solution particulière : **x = {xp}, y = {yp}**")
        
        # Affichage de la solution générale de manière claire
        print("\n**La famille des solutions entières est de la forme (k ∈ Z) :**")
        print("   x = {}{}{}k".format(
            xp, 
            " + " if alpha >= 0 else " - ", 
            abs(alpha) if abs(alpha) != 1 else ("" if abs(alpha) == 1 else "")
        ))
        print("   y = {}{}{}k".format(
            yp, 
            " + " if beta >= 0 else " - ", 
            abs(beta) if abs(beta) != 1 else ("" if abs(beta) == 1 else "")
        ))
    
    # -------------------------------------------------------------
    
    print("\n" + "="*60)
    print("=== 2. Nombres Premiers (Théorème/Crible d'Ératostène) ===")
    print("="*60)
    
    try:
        n_max = int(input("Entrez le nombre maximum (N) pour trouver les nombres premiers (ex: 25) : "))
    except ValueError:
        print("\nERREUR : Veuillez entrer uniquement un nombre entier positif pour N.")
        exit()
        
    if n_max < 2:
        print("\nLe nombre doit être supérieur ou égal à 2.")
    else:
        nombres_premiers = crible_eratosthene(n_max)
        
        print(f"\nLes nombres premiers inférieurs ou égaux à **{n_max}** sont :")
        print(nombres_premiers)
        print(f"Total de **{len(nombres_premiers)}** nombres premiers trouvés.")
