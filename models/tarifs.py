Tarifs = {
    4: {  
        100: {"journalier": 30.0, "km_supp": 0.15},
        200: {"journalier": 35.0, "km_supp": 0.12},
        300: {"journalier": 40.0, "km_supp": 0.10},
        "+300": {"journalier": 45.0, "km_supp": 0.08}
    },

    5: {  
        100: {"journalier": 40.0, "km_supp": 0.20},
        200: {"journalier": 45.0, "km_supp": 0.17},
        300: {"journalier": 50.0, "km_supp": 0.15},
        "+300": {"journalier": 55.0, "km_supp": 0.12}
    },

    6: {  
        100: {"journalier": 50.0, "km_supp": 0.25},
        200: {"journalier": 55.0, "km_supp": 0.22},
        300: {"journalier": 60.0, "km_supp": 0.20},
        "+300": {"journalier": 65.0, "km_supp": 0.18}
    }
}


class TarifsManager:
    
    def __init__(self):
        self.tarifs = TARIFS
    
    def obtenir_tarif(self, cylindree, forfait_km):
        if cylindree not in self.tarifs:
            return None
        
        if forfait_km not in self.tarifs[cylindree]:
            return None
        
        return self.tarifs[cylindree][forfait_km]
    
    def afficher_grille(self):
        print("\n" + "=" * 70)
        print("GRILLE TARIFAIRE - LOCATION DE VÉHICULES")
        print("=" * 70)
        
        for cylindree in sorted(self.tarifs.keys()):
            print(f"\n--- Cylindrée : {cylindree} CV ---")
            print(f"{'Forfait KM':<15} {'Tarif/jour':<15} {'Prix km supp':<15}")
            print("-" * 45)
            
            for forfait, tarif in self.tarifs[cylindree].items():
                print(f"{str(forfait) + ' km':<15} {tarif['journalier']:<15.2f} {tarif['km_supp']:<15.2f}")
        
        print("\n" + "=" * 70)