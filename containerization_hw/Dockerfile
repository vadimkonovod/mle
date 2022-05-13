ARG BASE_CONTAINER=python:3.9
FROM ${BASE_CONTAINER}

ENV INPUT_FILE=input_file.txt

# workdir, for clarity
WORKDIR /stars

# install
RUN \
	apt-get update && apt-get install -y \
	unzip \
	git \
	wget

# build boost lib
RUN \
	wget https://boostorg.jfrog.io/artifactory/main/release/1.63.0/source/boost_1_63_0.zip && \
	unzip boost_1_63_0.zip && \
	mv boost_1_63_0 /usr/local/bin

# build starspace
RUN \
	git clone https://github.com/facebookresearch/Starspace.git && \
	cd Starspace && \
	make

# create user in order to restrict permissions
ARG USER_ID

RUN adduser --disabled-password --gecos '' --uid $USER_ID user
USER user

ENTRYPOINT ./Starspace/starspace train -trainFile /volume/${INPUT_FILE} -model /volume/output_file