# FTM-ML

## Installation

### Python package

1. Clone the repository:
	```
	git clone https://github.com/mldr-devs/ftm-ml.git
	```
2. Install requirements:
	```
	pip install optuna~=4.1.0
	```

### ns-3 network simulator

The [wifi-ftm-ns3](https://github.com/tkn-tub/wifi-ftm-ns3) extension of the ns-3 network simulator needs to be installed on your machine. You can read more on ns-3 installation process in the [official installation notes](https://www.nsnam.org/wiki/Installation).

1. Download and unzip wifi-ftm-ns3:
	```
	git clone https://github.com/tkn-tub/wifi-ftm-ns3.git
	mv wifi-ftm-ns3/ns-allinone-3.33-FTM-SigStr/ns-3.33 $NS3_DIR
	```
2. Copy the scenario file to the ns-3 scratch directory:
	```
    cp $PROJECT_DIR/scenario.cc $NS3_DIR/scratch
    ```
3. Build ns-3:
	```
	./waf configure -d optimized --enable-examples --enable-tests --disable-werror --disable-python
	./waf
	```
