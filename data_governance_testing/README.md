## Data governance testing

Task is [here](https://docs.google.com/document/d/1pAr39LnEju5najG11CtCFxv0yCTBzyceUUQVWVCi09Q/edit).

### How to setup DVC:
1. Init DVC:
```
dvc init [--subdir] 
```
2. Setup DVC remote:
```
dvc remote add -d myremote gdrive://{GOOGLE_DRIVE_FOLDER_ID}
[commit and push to Git]
```
3. Generate some data file (titanic.csv)
4. Track that data file with dvc:
```
dvc add titanic.csv
```
5. Start tracking data
```
git add titanic.csv.dvc .gitignore
[commit and push to Git]
dvc push
```
6. Check everything
```
[clone repo and run dvc pull:]
dvc pull titanic.csv
```