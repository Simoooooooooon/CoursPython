## Étapes pour installer les dépendances à partir de `requirements.txt` :

1. **Cloner le dépôt GitHub :**
   - Cloner votre dépôt GitHub contenant le fichier `requirements.txt`.

2. **Accéder au répertoire du projet :**
   - Une fois le dépôt cloné, ouvrir un terminal (Anaconda Prompt, terminal Linux, Command Prompt, etc.) et naviguer vers le répertoire où se trouve le fichier `requirements.txt` en utilisant la commande `cd`.

3. **Créer un environnement virtuel (recommandé) :**
   - Il est conseillé d'utiliser un environnement virtuel pour éviter les conflits entre les différentes versions des packages. Cela peut être fait avec `venv` (module intégré à Python) ou `conda` pour les environnements conda.

4. **Activer l'environnement virtuel (si utilisé) :**
   - Une fois l'environnement virtuel créé, l'activer à l'aide de la commande spécifique au gestionnaire d'environnement utilisé (`activate <nom_de_l'environnement>` pour `venv`, ou `conda activate <nom_de_l'environnement>` pour `conda`).

5. **Installer les dépendances à partir de `requirements.txt` :**
   - Utiliser `pip` ou `conda`, en fonction de l'environnement virtuel utilisé, pour installer les dépendances répertoriées dans le fichier `requirements.txt`. Voici comment cela peut être fait :

     - **Pour `pip` :**
       ```bash
       pip install -r requirements.txt
       ```

     - **Pour `conda` :**
       ```bash
       conda install --file requirements.txt
       ```

6. **Vérifier l'installation :**
   - Une fois l'installation terminée, vérifier que toutes les dépendances ont été correctement installées en exécutant le projet ou en vérifiant la liste des packages installés dans l'environnement.


