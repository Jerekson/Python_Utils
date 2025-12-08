import pickle
import os

# --- 1. Classe Parent (Concept abstrait)
class Effet:
    """Représente un effet générique (Bonus ou Malus)."""
    def __init__(self, nom: str, duree: int):
        self.nom = nom
        self.duree = duree

    def appliquer(self, personnage):
        """Méthode vide ici, elle sera définie dans les enfants."""
        pass

# --- 2. Héritage : Bonus EST un Effet
class Bonus(Effet):
    def __init__(self, nom: str, duree: int, soin: int):
        # On appelle le constructeur du parent (Effet)
        super().__init__(nom, duree)
        self.soin = soin

    # On précise ce que fait "appliquer" pour un Bonus
    def appliquer(self, personnage):
        personnage.points_de_vie += self.soin
        print(f"✨ {personnage.nom} reçoit un bonus : +{self.soin} PV !")

# --- 3. Héritage : Malus EST un Effet
class Malus(Effet):
    def __init__(self, nom: str, duree: int, degats: int):
        super().__init__(nom, duree)
        self.degats = degats

    # On précise ce que fait "appliquer" pour un Malus
    def appliquer(self, personnage):
        personnage.points_de_vie -= self.degats
        print(f"💀 {personnage.nom} subit un malus : -{self.degats} PV !")

# --- 4. La Classe Principale
class Personnage:
    def __init__(self, nom: str, points_de_vie: int):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.effets_actifs = []

    def recevoir_effet(self, effet: Effet):
        """Ajoute un effet à la liste et l'applique immédiatement."""
        self.effets_actifs.append(effet)
        print(f"\n--- {self.nom} est touché par {effet.nom} ---")
        effet.appliquer(self)

    def afficher_etat(self):
        print(f"📊 État de {self.nom} : {self.points_de_vie} PV")

# --- 5. La Classe Orchestrateur (Partie) avec Sauvegarde/Chargement
class Partie:
    def __init__(self):
        self.joueurs = []
        print("Initialisation de la partie.")

    def ajouter_joueur(self, perso: Personnage):
        self.joueurs.append(perso)
        print(f"Joueur {perso.nom} a rejoint la partie.")

    # --- MÉTHODE DE SAUVEGARDE ---
    def sauvegarder_partie(self, chemin_fichier="sauvegarde.pkl"):
        """Sérialise l'objet Partie complet (y compris les joueurs et leurs états) avec pickle."""
        try:
            with open(chemin_fichier, 'wb') as fichier: # 'wb' pour write binary
                pickle.dump(self, fichier)
            print(f"\n✅ Partie sauvegardée avec succès dans {chemin_fichier}.")
        except Exception as e:
            print(f"\n❌ Erreur lors de la sauvegarde : {e}")

    # --- MÉTHODE DE CHARGEMENT (Méthode de Classe) ---
    @classmethod
    def charger_partie(cls, chemin_fichier="sauvegarde.pkl"):
        """Tente de désérialiser l'objet Partie. Si le fichier n'existe pas ou est corrompu, retourne une nouvelle partie."""
        
        # Vérifie si le fichier existe
        if not os.path.exists(chemin_fichier):
            print(f"Le fichier de sauvegarde '{chemin_fichier}' n'existe pas.")
            return cls() # Retourne une nouvelle instance de Partie (Partie())
            
        try:
            with open(chemin_fichier, 'rb') as fichier: # 'rb' pour read binary
                partie_chargee = pickle.load(fichier)
            print(f"\n✅ Partie chargée avec succès depuis {chemin_fichier}.")
            return partie_chargee
        except Exception as e:
            print(f"\n❌ Erreur lors du chargement (fichier corrompu ?). Démarrage d'une nouvelle partie. Erreur: {e}")
            return cls() # En cas d'erreur de lecture, retourne une nouvelle partie


# ----------------------------------------------------------------------
## --- ZONE DE TEST MODIFIÉE (Logique de jeu avec Sauvegarde) ---
# ----------------------------------------------------------------------

if __name__ == "__main__":
    SAVE_FILE = "jeu_partie.pkl"
    
    # 1. Tenter de charger la partie
    print("--- Tentative de chargement de partie ---")
    ma_partie = Partie.charger_partie(SAVE_FILE)

    # 2. Logique pour s'assurer que nous avons un héros
    if not ma_partie.joueurs:
        print("\n--- Création d'une nouvelle partie ---")
        # Création d'un personnage (Instanciation)
        hero = Personnage("Arthur", 100)
        ma_partie.ajouter_joueur(hero)
    else:
        print("\n--- Reprise de la partie sauvegardée ---")
        # On récupère le héros sauvegardé
        hero = ma_partie.joueurs[0]
    
    hero.afficher_etat()

    # Création des objets Bonus et Malus
    potion = Bonus("Potion de Vie", duree=1, soin=20)
    poison = Malus("Poison de Vipère", duree=3, degats=15)

    # Interaction : Le personnage reçoit les effets
    hero.recevoir_effet(poison)
    hero.recevoir_effet(potion)

    hero.afficher_etat()
    
    # 3. Sauvegarder la partie à la fin
    ma_partie.sauvegarder_partie(SAVE_FILE)