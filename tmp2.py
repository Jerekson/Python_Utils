# little_projects/pwd_store/utils/logging_config.py

import logging
import sys

def setup_logging(level=logging.INFO, handler_type='stream'):
    """
    Configure le système de logging pour le package pwd_store.
    Cette fonction DOIT être appelée explicitement par l'utilisateur.
    """
    # Évite de reconfigurer si c'est déjà fait
    if logging.getLogger().handlers:
        return

    # Crée le Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Crée le Handler (console ou fichier, par exemple)
    if handler_type == 'stream':
        handler = logging.StreamHandler(sys.stdout)
    # else:
        # handler = logging.FileHandler('pwd_store.log')

    handler.setFormatter(formatter)
    
    # Récupère le logger racine de votre package (ou le root logger)
    package_logger = logging.getLogger('little_projects.pwd_store')
    package_logger.setLevel(level)
    package_logger.addHandler(handler)
    package_logger.propagate = False # Évite la double émission si le root logger est aussi configuré

    # Log pour confirmer le démarrage (utilisez le logger du package)
    package_logger.info("Configuration de logging personnalisée démarrée.")

# ---
# Dans little_projects/pwd_store/__init__.py, vous exposez cette fonction
# from .utils.logging_config import setup_logging



# Scenario d'execution 1
# little_projects/pwd_store/__main__.py

from .utils.logging_config import setup_logging # Importe la fonction
# ... (gestion argparse pour obtenir le niveau de log) ...

if __name__ == "__main__":
    # La fonction est appelée automatiquement au démarrage de l'application
    setup_logging(level=logging.DEBUG) 
    # ... le reste du code de l'application



# Scenario 2
# script_utilisateur_externe.py
# 1. L'utilisateur configure votre package
from little_projects.pwd_store import setup_logging
setup_logging(level=logging.WARNING) # Seulement les WARNINGs et erreurs

# 2. Utilisation de votre classe
from little_projects.pwd_store import PWD_generator
generator = PWD_generator() 
# ... Les logs du package s'affichent selon la configuration ci-dessus





# Scenario 3 
# script_utilisateur_serveur.py
import logging
# L'utilisateur configure son système de logging comme il le souhaite
logging.basicConfig(level=logging.INFO, filename='server.log') 

# L'utilisateur importe votre classe
from little_projects.pwd_store import PWD_generator
generator = PWD_generator() 
# ... Vos messages de log sont automatiquement écrits dans 'server.log'