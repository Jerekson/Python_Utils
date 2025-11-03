# Python_Utils

## TODO
### little projects 
 - Build the keylogger to send the capture keystrokes to a server you built using Python

### labo
#### test-module
 - __test_module_sqlite__ : has to be improved for multithread, nosqli & trigger

## IN PROGRESS
### little projects

### Python_and_network
- check_website - check if an url is alive
 
## DONE
### little projects
 - pwd_store - v1 done. check README before new improvement


----
[&cross;]  
[&check;]  

----
# Tips 

## Create an executable package
Quant à l'utilisation par quelqu'un qui ne connaît pas Python, la solution idéale est de transformer votre script en un **exécutable autonome** que l'utilisateur peut lancer directement (un fichier `.exe` sur Windows, un binaire sur Linux, etc.).

### 1\. Comment contourner l'activation du `venv` (Exécutables)

Si vous ne voulez pas que vos utilisateurs aient à gérer Python, ni `venv`, ni `pip`, la seule solution est d'utiliser un outil qui "packagera" votre code Python et toutes ses dépendances (y compris l'interpréteur Python minimal nécessaire) dans un **seul fichier ou dossier distribuable**.

L'outil le plus populaire pour cela est **PyInstaller**.

#### A. Le Principe de PyInstaller

PyInstaller lit votre script principal, trouve toutes les bibliothèques qu'il importe (comme `sqlite3`, `simple-term-menu`, etc.), et les compile avec l'interpréteur Python dans un seul package.

L'utilisateur final n'a qu'à double-cliquer sur le fichier généré.

#### B. Les Étapes à Suivre

1.  **Installez PyInstaller** (dans votre `venv` \!) :

    ```bash
    (venv) pip install pyinstaller
    ```

2.  **Générez l'exécutable :**
    Exécutez cette commande depuis le répertoire racine de votre projet :

    ```bash
    (venv) pyinstaller mon_script_principal.py --onefile
    ```

      * Le flag `--onefile` est souvent utilisé pour créer un seul fichier exécutable, ce qui est plus simple à distribuer.
      * **Attention :** Vous devrez peut-être ajouter l'option `--add-data` ou `--add-files` si votre application dépend de fichiers externes (comme votre fichier `data_config.json` ou votre BDD `keystore.db`).

3.  **Distribuez :**
    PyInstaller crée un dossier `dist/` dans votre répertoire de projet. Vous donnez à l'utilisateur le fichier exécutable qui s'y trouve (`mon_script_principal.exe` sur Windows).

    L'utilisateur **n'a plus besoin d'installer Python ni d'activer un `venv`**. Il lance le programme directement.

-----

### 2\. Note sur l'Environnement Virtuel pour le Développeur

Même si l'utilisateur final n'utilise pas de `venv`, **vous**, en tant que développeur, **devez toujours utiliser un `venv`**.

Pourquoi ?

  * **PyInstaller fonctionne mieux** s'il n'a à gérer que les dépendances d'un environnement propre et isolé.
  * Si vous installez `simple-term-menu` au niveau du système (ce que votre Linux vous a empêché de faire), PyInstaller risque de ne pas trouver la bonne version ou d'inclure des bibliothèques inutiles du système dans votre exécutable final, ce qui le rend très volumineux et potentiellement instable.

Le `venv` est une couche de propreté et de sécurité pour **votre** travail de développement, qui rend la création de l'exécutable final fiable.


## Get all 'TODO : ' in CLI
### in Linux : 
standard
```Bash
grep -r -i -n "TODO : " .
```

restain to python type file
```Bash
grep -r -i -n --include=\*.py "TODO" .
```

### In Windows
```Bash
findstr /s /i /n "TODO" *.py
```



# Troubleshooting 

##  source ./venv/bin/activate : command not found
```Bash
-bash: ./venv/bin/activate: line 4: syntax error near unexpected token `$'{\r''
'bash: ./venv/bin/activate: line 4: `deactivate () { 
```

### Solution 1 
```Bash
sudo apt update
sudo apt install dos2unix
```  
```Bash
dos2unix ./venv/bin/activate
```  

## pip install dont work
### L'erreur : 
```bash 
pip install simple-term-menu
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

### Solution 1  
#### 1 - create a virtual environnment.  
in the project root folder, make 
```Bash
python3 -m venv venv
```
it create a folder named 'venv' which will contain the isolated environnement  
  
#### 2 - launch the environnment 
In Linux and MacOS :  
```Bash
source venv/bin/activate
```
  
For Windows  
With PowerShell  
```PowerShell
venv\Script\Activate.ps1
```

Or if it was created with Linux 
```PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
. .\venv\bin\activate
```

#### 3 - Install the package 
```Bash 
(venv) pip install [package name]
```
The package is now installed only for the actual project

#### 4 - End the environnement
```Bash
(venv) deactivate
```
