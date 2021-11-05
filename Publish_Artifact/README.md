# Artifact Publishing

This is a simple README.md file containing some text for helpful information.

## Highlight:

1. main source code is `main.py`
2. execute `setup.py` to build the source code for different platforms and executables.
3. In `Dockerfile` of this project, git repository is cloned to `/docker_examples` folder.

# Steps:
1. Clone the repository [project folder Publish_Artifact]
2. Execute `docker build` command to build image:
```shell
docker build --rm -f "Publish_Artifact/Dockerfile" -t publishartifact:latest "Publish_Artifact"
```
3. Execute `docker run` command to run the image:
```shell
docker run --rm -it  publishartifact:latest
```


# [Optional] In order to transfer file from container image perform below steps

### Syntax:
```shell
docker cp <containerId>:/file/path/within/container /host/path/target
```

### Steps
1. To get container ID, execute `docker ps` command. 
2. If container ID is: `12eec88327fa`, then execute:
```shell
docker cp 12eec88327fa:/docker_examples/Publish_Artifact/main.cpython-36m-x86_64-linux-gnu.so Projects/dockerExamples/Publish_Artifact/
docker cp 12eec88327fa:/docker_examples/Publish_Artifact/main.cpython-37m-x86_64-linux-gnu.so Projects/dockerExamples/Publish_Artifact/
docker cp 12eec88327fa:/docker_examples/Publish_Artifact/main.cpython-38-x86_64-linux-gnu.so Projects/dockerExamples/Publish_Artifact/
docker cp 12eec88327fa:/docker_examples/Publish_Artifact/main.cpython-39-x86_64-linux-gnu.so Projects/dockerExamples/Publish_Artifact/
```
