# FTM-ML

## Installation

### Python package

1. Clone the repository:
	```
	git clone https://github.com/mldr-devs/ftm-ml.git
	```
2. Install requirements:
	```
	pip install -r requirements.txt
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
