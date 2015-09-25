# Install

Scruffy requires dependencies which can be tricky to install.  
Here's a way to install them easily.

## OSX

	# dependencies
	brew install graphviz plotutils
	brew install imagemagick --with-librsvg

	# if you haven't `pip` yet
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	sudo python get-pip.py

	# install `scuffy` and `image` (PIL replacement)
	sudo pip install image scruffy

Tested on OSX 10.10.5