#!/usr/bin/sh

script=/home/users/ryanhass/ME469_FinalProject/postProcessing//ME469-Final-Project/visualize_nalu.py

# Install Python packages
if [ -f $HOME/.local/bin/pip ]
then
	echo "PIP found"
else
	echo "PIP not found. Install PIP."
	wget https://bootstrap.pypa.io/get-pip.py
	python3 get-pip.py --user
	rm get-pip.py
fi


if [ -d $HOME/.local/lib/python3.6/site-packages/numpy/ ]
then
	echo "Numpy found"
else
	echo "Numpy not found. Installing numpy."
	pip install numpy --user
fi


if [ -d $HOME/.local/lib/python3.6/site-packages/matplotlib/ ]
then
	echo "Matplotlib found"
else
	echo "Matplotlib not found. Installing matplotlib."
	pip install matplotlib --user
fi


if [ -d $HOME/.local/lib/python3.6/site-packages/netCDF4/ ]
then
	echo "NetCDF4 found"
else
	echo "NetCDF4 not found. Installing netCDF4."
	pip install netCDF4 --user
fi

# Run nalu
echo "Post process nalu"
if [ -f /home/users/ryanhass/ME469_FinalProject/datFiles/baseline1/viscousPump.e ]
then
	echo "Start to generate plot."
	python3 $script
	echo "Done!"
else
	echo "ERROR: viscousPump.e not found."
fi
