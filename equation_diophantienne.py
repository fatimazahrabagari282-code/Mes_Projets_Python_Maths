import math

# ==============================================================================
# 1. Tâche 1 & 2: PGCD et Algorithme d'Euclide Étendu
# ==============================================================================
def euclide_etendu(a, b):
    """
    Implémente l'Algorithme d'Euclide Étendu.
    Retourne (d, x0, y0) tels que a*x0 + b*y0 = d, où d = pgcd(a, b).
    """
    a_original, b_original = a, b
    a_abs, b_abs = abs(a), abs(b)
    
    # Cas triviaux
    if a_abs == 0 and b_abs == 0:
        return 0, 0, 0
    
    # Initialisation pour l'algorithme d'Euclide étendu
    r_prev, r_curr = a_abs, b_abs
    x_prev, x_curr = 1, 0
    y_prev, y_curr = 0, 1
    
    while r_curr != 0:
        quotient = r_prev // r_curr
        
        # Calcul du nouveau reste
        r_prev, r_curr = r_curr, r_prev - quotient * r_curr
        
        # Calcul des nouveaux coefficients de Bézout
        x_prev, x_curr = x_curr, x_prev - quotient * x_curr
        y_prev, y_curr = y_curr, y_prev - quotient * y_curr

    # d est le dernier reste non nul (r_prev)
    d = r_prev
    x0_abs, y0_abs = x_prev, y_prev
    
    # Ajustement des signes de x0 et y0 en fonction des entrées originales
    x0 = x0_abs * (1 if a >= 0 else -1)
    y0 = y0_abs * (1 if b >= 0 else -1)
        
    # Double vérification pour s'assurer que a*x0 + b*y0 = d
    if a * x0 + b * y0 != d:
        x0 = -x0
        y0 = -y0
        
    return d, x0, y0

# ==============================================================================
# Programme Principal (Tâche 6: Interaction utilisateur et Affichage clair)
# ==============================================================================

if __name__ == "__main__":
    print("=== Résolution de l'équation diophantienne linéaire ax + by = c ===")
    
    try:
        # Tâche 6: Demander les valeurs de a, b et c
        a = int(input("Entrez la valeur de a : "))
        b = int(input("Entrez la valeur de b : "))
        c = int(input("Entrez la valeur de c : "))
    except ValueError:
        print("\nERREUR : Veuillez entrer uniquement des nombres entiers.")
        exit()

    print("\n--- Équation à résoudre: {}x + {}y = {} ---".format(a, b, c))

    # Calcul du PGCD et des coefficients de Bézout
    d, x0, y0 = euclide_etendu(a, b)
    
    print("\nÉtape 1 : Vérification d'existence (Tâche 3)")
    print(f"Calcul du PGCD(a, b) = {d}")

    # Tâche 3: Vérification d'existence
    if c % d != 0:
        # d ne divise pas c
        print(f"\n**Pas de solution entière** : d={d} ne divise pas c={c}.")
    else:
        # d divise c
        print(f"\n**Il existe des solutions entières** : d={d} divise c={c}.")

        # Tâche 4: Calcul d'une solution particulière
        
        # Facteur multiplicatif k = c/d
        k_facteur = c // d
        
        # Calcul de la solution particulière (xp, yp)
        xp = x0 * k_facteur
        yp = y0 * k_facteur
        
        print("\nÉtape 2 : Solution particulière (Tâche 4)")
        print(f"Coefficients de Bézout: {a}({x0}) + {b}({y0}) = {d}")
        print(f"Solution particulière (xp, yp) : ({xp}, {yp})")
        print(f"Vérification: {a}({xp}) + {b}({yp}) = {a*xp + b*yp} (égal à {c})")

        # Étape 3: Écrire la solution générale (Tâche 5)
        
        # Les paramètres alpha et beta sont: alpha = b/d, beta = -a/d
        alpha = b // d
        beta = -a // d
        
        print("\nÉtape 3 : Solution générale (Tâche 5)")
        print(f"Les paramètres sont : α = {alpha}, β = {beta}")
        
        print("\n**La famille des solutions entières est de la forme (x, y) = (xp + αk, yp + βk), k ∈ Z :**")
        print("** (x, y) = ({}{}{}k, {}{}{}k), k ∈ Z **".format(
            xp, 
            " + " if alpha >= 0 else " - ", 
            abs(alpha) if abs(alpha) != 1 else "", 
            yp, 
            " + " if beta >= 0 else " - ", 
            abs(beta) if abs(beta) != 1 else ""
        ))
        
        print(f"\nValeurs demandées: xp={xp}, yp={yp}, α={alpha}, β={beta}, d={d}")
