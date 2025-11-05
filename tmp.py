import os
from pathlib import Path

# --- Exceptions minimales (pour l'exemple) ---
class InvalidPathError(Exception):
    """Erreur levée si le chemin ou le nom de fichier est invalide."""
    pass

def validate_and_get_filepath(prompt_message: str, allow_new_file: bool) -> Path:
    """
    Demande à l'utilisateur un chemin et un nom de fichier, 
    puis vérifie leur validité.
    
    Args:
        prompt_message (str): Le message à afficher à l'utilisateur.
        allow_new_file (bool): Si True, le fichier n'a pas besoin d'exister.
        
    Returns:
        Path: L'objet Path validé.
        
    Raises:
        InvalidPathError: Si la validation échoue.
    """
    
    while True:
        try:
            # 1. SAISIE UTILISATEUR
            path_input = input(prompt_message).strip()

            # --- CONTRÔLE 1 : Nom du Fichier et Extension ---
            if not path_input:
                raise InvalidPathError("Le chemin ne peut pas être vide.")
            
            p = Path(path_input)
            
            # Vérifier l'extension
            if p.suffix.lower() != '.json':
                raise InvalidPathError("Le fichier doit avoir l'extension '.json'.")
                
            # --- CONTRÔLE 2 : Caractères Dangereux (Injection) ---
            # Pour se protéger des injections de commande OS:
            # On vérifie l'absence de caractères de séparation de commandes 
            # (souvent utilisés par des attaquants dans des chemins malveillants).
            if any(c in p.name for c in (';', '&', '|', '`', '$', '(', ')')):
                raise InvalidPathError("Nom de fichier invalide ou potentiellement dangereux (caractères spéciaux).")


            # --- CONTRÔLE 3 : Localisation du Fichier ---
            
            # Si nous voulons lire un fichier existant (allow_new_file=False)
            if not allow_new_file:
                # Vérifie que le fichier existe
                if not p.is_file():
                    raise InvalidPathError(f"Le fichier '{path_input}' n'existe pas ou n'est pas un fichier.")
                
            # Si nous créons un nouveau fichier (allow_new_file=True)
            if allow_new_file:
                # Vérifie que le répertoire parent existe (la localisation)
                parent_dir = p.parent
                if not parent_dir.is_dir() and parent_dir != Path('.'):
                    # p.parent retourne '.' si l'utilisateur entre juste 'new.json'.
                    # On permet cela, mais on s'assure que si un répertoire est spécifié, il existe.
                    raise InvalidPathError(f"Le répertoire parent '{parent_dir}' n'existe pas.")

            # Si toutes les vérifications passent
            return p
            
        except InvalidPathError as e:
            print(f"[ERREUR VALIDATION] {e}. Veuillez réessayer.")
            continue
        
        except (EOFError, KeyboardInterrupt):
            print("\nOpération annulée.")
            raise

# --- Exemple d'Utilisation ---

def demonstrate_validation():
    print("--- Démarrage de la démonstration de validation ---")
    
    # Cas 1 : Création d'un nouveau fichier (allow_new_file=True)
    try:
        new_path = validate_and_get_filepath(
            prompt_message="Entrez un chemin pour CRÉER un fichier JSON (ex: config/new.json) : ",
            allow_new_file=True
        )
        print(f"\n[SUCCÈS] Chemin de création validé: {new_path}")
    except Exception:
        print("[ÉCHEC] Arrêt du test.")
        
    # Cas 2 : Lecture d'un fichier existant (allow_new_file=False)
    try:
        existing_path = validate_and_get_filepath(
            prompt_message="Entrez le chemin d'un fichier EXISTANT (ex: path_validator.py) : ",
            allow_new_file=False
        )
        print(f"\n[SUCCÈS] Chemin de lecture validé: {existing_path}")
    except Exception:
        print("[ÉCHEC] Arrêt du test.")

if __name__ == '__main__':
    demonstrate_validation()