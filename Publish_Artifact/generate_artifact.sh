
# Execute this file from parent directory

# Configurations
PY_VERSION="38"
DOCKER_FILE_NAME="Dockerfile.py${PY_VERSION}"
DOCKER_IMAGE_NAME="publishartifact:py${PY_VERSION}"
SOURCE_DIR=.
CONTAINER_NAME="artifact_images_py${PY_VERSION}"

# Build docker image
docker build --rm -f ${DOCKER_FILE_NAME} -t ${DOCKER_IMAGE_NAME} ${SOURCE_DIR}

docker create -ti --name ${CONTAINER_NAME} ${DOCKER_IMAGE_NAME} bash
docker cp ${CONTAINER_NAME}:docker_examples/Publish_Artifact/main.cpython-${PY_VERSION}-x86_64-linux-gnu.so ${SOURCE_DIR}
docker rm -f ${CONTAINER_NAME}