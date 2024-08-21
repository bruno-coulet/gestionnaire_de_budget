disponible = 2500.00
budgets = {}
depenses = {}

# crée des budgets provisionnels
def budget_ajout(nom, montant):

    global disponible
    
    # Message d'erreur si ce budget existe déjà comme clé dans le dictionnaire budgets
    if nom in budgets:
        raise ValueError("Ce budget existe déjà")
    
    # Message d'erreur si dépassement du budget
    if montant > disponible:
        raise ValueError("Fonds insuffisant")

    # Crée le budget avec le nom et le montant ad hoc dans le dictionnaire budgets
    budgets[nom] = montant
    # Soustrait le budget à la somme disponible
    disponible -= montant
    # Crée la dépense (avec une valeur nulle) dans le dictionnaire depenses
    depenses[nom] = 0
    return print(f"Budget disponible : {disponible}")

# crée des dépenses
def depense(nom, montant):
    
    # Message d'erreur si ce budget n'est pas prévu
    if nom not in depenses:
        raise ValueError("Ce budget n'est pas prévu")
    
    # Ajoute le montant à la clé correspondante du dictionnaire depenses
    depenses[nom] += montant
    
    # récupère le montant budgété dans une variable
    montant_budgete = budgets[nom]
    
    # récupère le montant dépensé dans une variable
    montant_depense = depenses[nom]
    # Renvoie le montant restant dans le budget
    return print(f"Il reste {montant_budgete - montant_depense} euros pour le budget {nom}.")

def afficher_resume():
    # Affiche un en-tête
    print("Budget           prévisionnel   dépenses   restant")
    print("--------------- -------------- ---------- ----------")
    # Variables pour la ligne de fin de tableau
    total_budgete = 0
    total_depense = 0
    total_restant = 0
    # Parcours toutes les clés du dictionnaire budgets
    for nom in budgets:
        # récupère le montant budgété pour la clé en cours du dictionnaire budgets
        budgete = budgets[nom]
        # récupère le montant dépensé pour la clé en cours du dictionnaire depenses
        depense = depenses[nom]
        # calcul ce qu'il reste dans le budget en cours
        restant = budgete - depense
        # Affiche un résumé d'une ligne pour le le budget en cours
        print(f"{nom:15s} {budgete:10.2f} {depense:12.2f} {restant:10.2f}")
        # Modification des variables pour la ligne de fin de tableau
        total_budgete += budgete
        total_depense += depense
        total_restant += restant
    # Ligne de fin de tableau    
    print("--------------- -------------- ---------- ----------")
    print(f"{"Total":15s} {total_budgete:10.2f} {total_depense:12.2f} {total_restant:10.2f}"
          f'{total_budgete - total_depense:10.2f}')

budget_ajout("courses",500)
budget_ajout("location",900)
depense("courses",35)
depense("location",550)
afficher_resume()