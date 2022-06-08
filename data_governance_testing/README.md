## Data governance testing

Task is [here](https://docs.google.com/document/d/1pAr39LnEju5najG11CtCFxv0yCTBzyceUUQVWVCi09Q/edit).

### How to run model:
```
dvc pull
dvc repro
```

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
3. Generate some data file [train.csv]
4. Track that data file with dvc:
```
dvc add train.csv
```
5. Start tracking data
```
git add train.csv.dvc .gitignore
[commit and push to Git]
dvc push
```
6. Check everything
```
[clone repo and run 'dvc pull']
dvc pull train.csv
```
7. For scenarios where code needs to access data on its own, e.g. automatic CI/CD in Github Actions (no interactive user OAuth authentication is needed) we need to create JSON key as described [here] (https://dvc.org/doc/user-guide/setup-google-drive-remote#using-service-accounts) and add "Repository secret" with name GDRIVE_CREDENTIALS_DATA to Github repository.