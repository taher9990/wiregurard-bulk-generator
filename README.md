# wiregurard-bulk-generator

## Download the files
` wget https://bootstrap.pypa.io/get-pip.py`
`git clone git://github.com/taher9990/wiregurard-bulk-generator.git`

## Configure the path for saving files:

Open app.conf.csv file and edit below line 
`pathToHosts,"/home/ubuntu/wirguardConfigGen/csvdata.csv"`

## Start the installation of the pre-requisties
apt install python3 -y
apt install python3-distutils -y
python3 get-pip.py

## Now run the generator 
`Wireguard_ConfigGenerator.py`
