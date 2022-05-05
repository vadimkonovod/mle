## Containerization

Task is [here](https://docs.google.com/document/d/1CrWx350_j5s2YCWaI8trDccIRJC2aRDHHL46uUp6weo/edit).

Build image:
```
docker build -t stars .
```

Run container:
```
docker run --rm -it -v "$(pwd)/volume:/volume" stars
```

Run Starspace:
```
cd Starspace
./starspace train -trainFile /volume/input_file.txt -model /volume/output_file
```