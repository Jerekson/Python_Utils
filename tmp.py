# Assurez-vous d'avoir installé ceci dans votre venv : pip install simple-term-menu
from simple_term_menu import TerminalMenu
import sys

# Fonctions d'action (simulées pour l'exemple)
def create_password_action():
    print("\n[INFO] 🔑 Démarrage de la création d'un nouveau mot de passe...")
    input("Appuyez sur Entrée pour continuer...")

def display_entries_action():
    print("\n[INFO] 📋 Affichage des 5 dernières entrées de la BDD...")
    input("Appuyez sur Entrée pour continuer...")

def delete_entry_action():
    print("\n[INFO] 🗑️ Suppression d'une entrée : besoin de l'ID...")
    input("Appuyez sur Entrée pour continuer...")

def main_menu():
    
    # 1. Définir les options du menu
    # L'option 'Quitter' est la dernière pour une sortie propre.
    options = [
        "Créer un nouveau mot de passe",
        "Afficher les entrées de la BDD",
        "Supprimer une entrée",
        "Configurer l'application",
        "Quitter l'application"
    ]
    
    # Dictionnaire liant l'index de l'option à la fonction correspondante
    actions = {
        0: create_password_action,
        1: display_entries_action,
        2: delete_entry_action,
        # 3: configuration_action, # Vous ajouterez cette fonction
        4: lambda: sys.exit(0)  # Utilisation d'une lambda pour quitter proprement
    }
    
    # 2. Boucle principale du menu
    while True:
        # Création et affichage du menu interactif
        terminal_menu = TerminalMenu(
            options,
            title="=== GESTIONNAIRE DE MOTS DE PASSE ===",
            menu_cursorsimple_select_menu="-> ",
            menu_cursor_style=("fg_blue", "bold"),
            menu_highlight_style=("bg_gray", "fg_blue"),
        )
        
        # Affiche le menu et attend la sélection de l'utilisateur
        menu_entry_index = terminal_menu.show()
        
        # 3. Exécuter l'action basée sur l'index sélectionné
        if menu_entry_index is None: 
            # Si l'utilisateur appuie sur Ctrl+C ou Ctrl+D
            print("\n👋 Sortie forcée.")
            sys.exit(0)
            
        if menu_entry_index in actions:
            actions[menu_entry_index]()
        else:
            # Si l'index ne correspond pas à une fonction définie (par exemple, option 3 ou 4)
            print(f"\n[ATTENTION] L'option {options[menu_entry_index]} n'est pas encore implémentée.")
            input("Appuyez sur Entrée pour retourner au menu principal...")

if __name__ == "__main__":
    main_menu()