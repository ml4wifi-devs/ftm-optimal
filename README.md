# FTM-ML

## Installation

### Python package

1. Clone the repository:
	```
	git clone https://github.com/mldr-devs/ftm-ml.git
	```
2. Install requirements:
	```
	pip install -e .
	```

### ns-3 network simulator

The wifi-ftm-ns3 extension of the ns-3 network simulator needs to be installed on your machine. We show you how to install the ns-3 by downloading the official distribution, apply the [wifi-ftm-ns3](https://github.com/tkn-tub/wifi-ftm-ns3) patch, and integrate it with our solution. You can read more on ns-3 installation process in the
[official installation notes](https://www.nsnam.org/wiki/Installation).

1. Download and unzip ns-3.35:
	```
	wget https://www.nsnam.org/releases/ns-allinone-3.35.tar.bz2
	tar -xf ns-allinone-3.35.tar.bz2
	mv ns-allinone-3.35/ns-3.35 $NS3_DIR
	```
2. Apply patch:
	```
	cp $PROJECT_ROOT/ns3_files/ns-3.35-to-wifi-ftm-ns3.patch $NS3_DIR
	cd $NS3_DIR
	patch -p1 -i ns-3.35-to-wifi-ftm-ns3.patch
	```
3. To flawlessly synchronize files between the repository and the ns-3 installation, you can create symbolic links to the corresponding folders:
	```
    cd $NS3_DIR
    rm -rf scratch
    ln -s $PROJECT_ROOT/ns3_files/scratch scratch
    ```
4. Build ns-3:
	```
	./waf configure -d optimized --enable-examples --enable-tests --disable-werror --disable-python
	./waf
	```

### ns3-ai

The ns3-ai module interconnects ns-3 and Python by transferring data through a shared memory pool. 
The memory can be accessed by both sides, thus making the connection. Read more about ns3-ai at the
[official repository](https://github.com/hust-diangroup/ns3-ai).

1.  Clone our fork of ns3-ai into `contrib` directory
	```
	cd $NS3_DIR/contrib/
	git clone https://github.com/m-wojnar/ns3-ai.git
	```
2. Go to ns3-ai directory and install the ns3-ai Python interface:
	```
	cd "$NS3_DIR/contrib/ns3-ai/"
	pip install py_interface
	```
3. Rebuild ns-3:
	```
	cd $NS3_DIR
	./waf configure -d optimized --enable-examples --enable-tests --disable-werror --disable-python
	./waf
	```
 