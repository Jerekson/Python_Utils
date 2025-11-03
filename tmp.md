```python
def get_integer_input(prompt_text: str) -> int:
    # ... code de prompt_toolkit pour récupérer le texte ...
    
    # Tentative de conversion : c'est là que le ValueError se produit.
    try:
        return int(text_input)
    except ValueError as e:
        # C'est ici que l'erreur est créée (levée)
        raise InvalidFormatError("L'entrée doit être un nombre entier valide.") from e
```
**Explication du `raise` :**
1.  Si l'utilisateur entre `"ABC"`, la ligne `int("ABC")` lève une **`ValueError`** (l'erreur interne de Python pour "mauvaise valeur").
2.  Le bloc `except ValueError as e:` intercepte cette erreur interne.
3.  Au lieu de laisser l'erreur interne de Python remonter, nous lançons notre propre erreur claire : `raise InvalidFormatError(...)`.

C'est l'étape de **lancement** de l'exception personnalisée.

## 3. Comment l'**Utiliser** (`except`) dans le Contrôleur

Une fois que la Vue a lancé (`raise`) l'`InvalidFormatError`, elle remonte au Contrôleur, qui est l'endroit où nous devons la capturer pour redémarrer la boucle de saisie.

Voici comment le Contrôleur (`controllers/cli.py`, concept) utiliserait cette exception :

```python
# Fichier : controllers/cli.py (concept)

# 1. On importe l'exception depuis le module
from ..modules.exceptions import InvalidFormatError, EmptyInputError, InputValidationFailed
from ..views.cli import display_message, get_integer_input

def handle_settings_flow():
    while True: # Boucle pour re-essayer en cas d'erreur
        try:
            # 2. On appelle la fonction de la Vue qui peut lever l'erreur
            frequency = get_integer_input("Fréquence de changement (jours) : ")
            
            # Si le code arrive ici, la saisie est réussie
            break 
            
        except InvalidFormatError as e:
            # ⭐️ 3. On capture spécifiquement l'erreur de format ⭐️
            display_message(str(e), is_error=True)
            continue # Recommence la boucle 'while True'

        except (EmptyInputError, InputValidationFailed) as e:
            # On capture les autres erreurs de validation (ex: champ vide)
            display_message(str(e), is_error=True)
            continue
            
        except (EOFError, KeyboardInterrupt):
            # Annulation
            return

### Synthèse

En résumé, l'utilisation de l'`InvalidFormatError` se fait en trois étapes :

1.  **Détection (dans la Vue) :** La `ValueError` interne est capturée autour de l'appel à `int()`.
2.  **Lancement (dans la Vue) :** La `ValueError` est remplacée par `raise InvalidFormatError(...)`.
3.  **Gestion (dans le Contrôleur) :** L'`except InvalidFormatError` est utilisé pour cibler l'erreur et redémarrer la boucle.
```