Étapes pour installer les dépendances à partir de requirements.txt :

    Cloner le dépôt GitHub :d cloner votre dépôt GitHub contenant le fichier requirements.txt.

    Accéder au répertoire du projet : Une fois le dépôt cloné, ouvrir un terminal (Anaconda Prompt, terminal Linux, Command Prompt, etc.) et 
    naviguer vers le répertoire où se trouve le fichier requirements.txt en utilisant la commande cd.

    Créer un environnement virtuel (recommandé) : Il est conseillé d'utiliser un environnement virtuel pour éviter les conflits entre les différentes versions des packages. 
    Cela peut être fait avec venv (module intégré à Python) ou conda pour les environnements conda.

    Activer l'environnement virtuel (si utilisé) : Une fois l'environnement virtuel créé,  l'activer à l'aide de la commande spécifique au gestionnaire 
    d'environnement utilisé (activate <nom_de_l'environnement> pour venv, ou conda activate <nom_de_l'environnement> pour conda).

    Installer les dépendances à partir de requirements.txt : Utiliser pip ou conda, en fonction de l'environnement virtuel utilisé, 
    pour installer les dépendances répertoriées dans le fichier requirements.txt. Voici comment cela peut être fait :

        Pour pip :

pip install -r requirements.txt

Pour conda :

        conda install --file requirements.txt

    Vérifier l'installation : Une fois l'installation terminée, vérifier que toutes les dépendances ont été correctement installées en exécutant
    le projet ou en vérifiant la liste des packages installés dans l'environnement.

