class GestionnaireBudget:
    def __init__(self, montant):
        self.disponible = montant
        self.budgets = {}
        self.depenses = {}

    # crée des budgets provisionnels
    def budget_ajout(self, nom, montant):

        # Message d'erreur si ce budget existe déjà comme clé dans le dictionnaire budgets
        if nom in self.budgets:
            raise ValueError("Ce budget existe déjà")
        
        # Message d'erreur si dépassement du budget
        if montant > self.disponible:
            raise ValueError("Fonds insuffisant")

        # Crée le budget avec le nom et le montant ad hoc dans le dictionnaire budgets
        self.budgets[nom] = montant
        # Soustrait le budget à la somme disponible
        self.disponible -= montant
        # Crée la dépense (avec une liste vide) dans le dictionnaire depenses
        self.depenses[nom] = []
        return print(f"Budget disponible après ajout du budget {nom} : {self.disponible}\n")
    
    #Modifie un budget prévisionnel
    def change_budget(self, nom, nouveau_montant):
        if nom not in self.budgets:
            raise ValueError("Ce budget n'existe pas")
        ancien_montant = self.budgets[nom]
        if nouveau_montant > ancien_montant + self.disponible:
            raise ValueError("Fonds insuffisants")
        # Modifie le le montant du budget via son nom et dans le dictionnaire budgets
        self.budgets[nom] = nouveau_montant
        # Met à jour la varaiable disponible en soustrayant la différence enttre le nouveau et l'ancien montant
        self.disponible -= nouveau_montant - ancien_montant
        return self.disponible

    # crée des dépenses
    def depense(self, nom, montant):
        
        # Message d'erreur si ce budget n'est pas prévu
        if nom not in self.depenses:
            raise ValueError("Ce budget n'est pas prévu")
        
        # Ajoute le montant à la liste des depenses
        self.depenses[nom].append(montant)
        
        # récupère le montant budgété dans une variable
        montant_budgete = self.budgets[nom]
        
        # récupère le montant dépensé dans une variable
        montant_depense = self.depenses[nom]
        # Renvoie le montant restant dans le budget
        return print(f"Il reste {montant_budgete - sum(montant_depense)} euros pour le budget {nom}.\n")

    def afficher_resume(self):
        # Affiche un en-tête
        print("Budget           prévisionnel   dépenses   restant")
        print("--------------- -------------- ---------- ----------")
        # Variables pour la ligne de fin de tableau
        total_budgete = 0
        total_depense = 0
        total_restant = 0
        # Parcours toutes les clés du dictionnaire budgets
        for nom in self.budgets:
            # récupère le montant budgété pour la clé en cours du dictionnaire budgets
            budgete = self.budgets[nom]
            # récupère le montant dépensé pour chaque budget
            depense = sum(self.depenses[nom])
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
        print(f"{'total':15s} {total_budgete:10.2f} {total_depense:12.2f} {total_restant:10.2f}")
        #f'{total_budgete - total_depense:10.2f}')
        print("-")

##mesdepenses = GestionnaireBudget(2000)
##mesdepenses.disponible
##mesdepenses.depenses
##mesdepenses.budgets
##mesdepenses.budget_ajout("location", 700)
##mesdepenses.budget_ajout("courses", 400)
##mesdepenses.budget_ajout("factures", 300)
##mesdepenses.budget_ajout("divertissement", 100)
##mesdepenses.budgets
##mesdepenses.depense("courses", 35)
##mesdepenses.afficher_resume()
