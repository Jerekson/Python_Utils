import textwrap
from pathlib import Path

def new_tables(datas, col_key_width=25, col_value_width=50):
    """
    Affiche les données sous forme de tableau CLI sans débordement, 
    en utilisant textwrap pour gérer les longues lignes.
    """
    
    # Largeur totale du tableau
    total_width = col_key_width + col_value_width + 6
    
    # Ligne de séparation
    sep_line = f"+{'-' * col_key_width}+{'-' * col_value_width}+"
    
    # --- Affichage de l'en-tête ---
    print(sep_line)
    print(f"| {'Nom du Dépôt':<{col_key_width}}| {'Résultats Git':<{col_value_width}}|")
    print(sep_line)

    # --- Affichage des données ---
    for key, value in datas.items():
        key_str = str(key.name) 
        
        # 1. Nettoyer et Envelopper (Wrap) le texte long
        # Utilisez textwrap.wrap() pour découper le texte long en lignes de la taille de la colonne
        value_lines = []
        for line in value.strip().split('\n'):
            # Chaque ligne Git est enveloppée pour ne pas dépasser la largeur de la colonne
            wrapped_lines = textwrap.wrap(line, width=col_value_width)
            value_lines.extend(wrapped_lines)
            
        # Si le résultat Git était vide (ex: juste un espace), assurez-vous qu'il y a au moins une ligne vide
        if not value_lines:
            value_lines = ['']

        # 2. Affichage ligne par ligne
        # Nous itérons sur la plus longue collection (value_lines)
        for i, line in enumerate(value_lines):
            
            # --- Colonne Clé ---
            # Si c'est la première ligne (i=0), on affiche le nom du dépôt
            if i == 0:
                col_key_output = f"{key_str:<{col_key_width}}"
            # Sinon, on laisse la colonne vide
            else:
                col_key_output = f"{'':<{col_key_width}}"
                
            # --- Colonne Valeur ---
            col_value_output = f"{line:<{col_value_width}}"

            print(f"| {col_key_output}| {col_value_output}|")
        
        # Ligne de séparation entre les entrées
        print(sep_line)

# --- Exemple d'utilisation (Simulation) ---

simulated_data = {
    Path('labo_kivy'): "On branch main\nYour branch is up to date with 'origin/main'.\nnothing to commit, working tree clean",
    Path('little_projects'): "Changes not staged for commit:\n(use \"git add <file>...\" to update what will be committed) [This line is intentionally made longer to test wrapping, this line will break into two or more lines.]\nmodified:   README.md",
}

new_tables(simulated_data)