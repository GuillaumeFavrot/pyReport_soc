# pyReport

#### A - Launching virtual environment


It is highly recommended to use this app in a virtual environement to ensure a proper python dependency management.

All python packages are listed in the requirements.txt file

In the root directory of the app run the following commands :

```
pip3 install pipenv
pipenv shell
pipenv install -r ./requirements.txt
```

#### B - Creating source and output folders


In order to store excel base data files and template or generate output files, a few base folders need to be created at the root of the app.

Create the following folders in the root folder of the script:
```
base_data
templates
output
logs
```

#### C - Importing data

Source data can be imported from both .csv  and .xlsx files. Those files must be droped in the "base_data" folder.

The importer tool retrieves data from a given file and store it into a pandas dataframe using the following syntaxe :

```
from utilities.data_import.import_processor import import_file

df = import_file("file_name.csv")
```


