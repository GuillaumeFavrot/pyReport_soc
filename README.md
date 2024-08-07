# pyReport

#### A - Lancement de l'environnement virtuel


Il est fortement recommandé d'utiliser cette application dans un environnement virtuel afin d'assurer une bonne gestion des dépendances python.

Tous les paquets python sont listés dans le fichier requirements.txt.

Dans le répertoire racine de l'application, lancez les commandes suivantes :

```
pip3 install pipenv
pipenv shell
pipenv install -r ./requirements.txt
```

#### B - Création des dossiers source et de sortie


Afin de stocker les fichiers de données de base d'Excel et de générer les fichiers de sortie, quelques dossiers de base doivent être créés à la racine de l'application.

Créez les dossiers suivants dans le dossier racine du script :
```
base_data
templates
output
logs
```

#### C - Importation de données

Les données sources peuvent être importées à partir de fichiers .csv et .xlsx. Ces fichiers doivent être déposés dans le dossier « base_data ».

L'outil d'importation récupère les données d'un fichier donné et les stocke dans un dataframe pandas via la syntaxe suivante :

```
from utilities.data_import.import_processor import import_file

df = import_file(timer, logger, "nom_du_fichier.csv")
```


