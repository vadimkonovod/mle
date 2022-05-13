## Containerization

Task is [here](https://docs.google.com/document/d/1CrWx350_j5s2YCWaI8trDccIRJC2aRDHHL46uUp6weo/edit).

Build image:
```
docker build -t stars --build-arg USER_ID=$(id -u) .
```

Run container:
```
docker run --rm -it -v "$(pwd)/volume:/volume" -e INPUT_FILE=input_file.txt stars 
```