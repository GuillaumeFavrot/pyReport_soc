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
excel_raw_data
excel_base_templates
output
```
