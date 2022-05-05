FROM python:3.9

#WORKDIR /stars do i need it?

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

CMD ["bash"]