Tarifs = {
    4: {  
        100: {"journalier": 30.0, "km_supp": 0.15},
        200: {"journalier": 35.0, "km_supp": 0.12},
    },

    5: {  
        100: {"journalier": 40.0, "km_supp": 0.20},  
    },
    
}


class TarifsManager:
    
    def __init__(self):
        self.tarifs = TARIFS
    
    def obtenir_tarif(self, cylindree, forfait_km):
        pass
    
    def afficher_grille(self):
        pass