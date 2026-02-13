## Spécification des classes

### Classe Client

**Attributs :**
- `id_client` (str) correspond à l'identifiant du client
- `nom` (str) désigne le nom du client
- `prenom` (str) désigne le prénom du client
- `mail` (str) désigne l'adresse email du client
- `telephone` est le numéro de téléphone du client
- `addresse` (str) est l'addresse du client

**Rôle :** Cette classe représente un client pouvant effectuer des réservations de véhicules.



### Classe Vehicule

**Attributs :**
- `id_vehicule`  : Identifiant unique du véhicule
- `marque` : Marque du véhicule 
- `modele` : Modèle du véhicule 
- `cylindree` (int): Cylindrée du moteur en cm³ 
- `kilometrage_actuel` (int) : Kilométrage actuel du véhicule
- `date_mise_en_circulation` (str) : Date de première mise en circulation 

**Rôle :** Cette classe représente un véhicule du parc de location avec ses caractéristiques techniques et son historique. 




### Classe Reservation

**Attributs :**
- `id_reservation` (str) : Identifiant unique de la réservation
- `id_client` (str) : Identifiant du client ayant réservé
- `id_vehicule` (str) : Identifiant du véhicule réservé
- `date_depart` (str) : Date de début de la location (format ISO : AAAA-MM-JJ)
- `date_retour` (str) : Date de fin de la location (format ISO : AAAA-MM-JJ)
- `forfait_km` (int) : Nombre de kilomètres inclus dans le forfait
- `cout_journalier` (float) : Tarif journalier de location en euros
- `prix_km_supp` (float) : Prix du kilomètre supplémentaire en euros
- `cout_estime` (float) : Coût total estimé de la réservation en euros

**Rôle :** Représente une réservation liant un client à un véhicule pour une période donnée; calcule automatiquement le coût total en fonction de la durée de location, du forfait kilométrique et du tarif du véhicule.