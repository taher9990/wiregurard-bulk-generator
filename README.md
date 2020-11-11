# wiregurard-bulk-generator

## Download the files
`wget https://bootstrap.pypa.io/get-pip.py` <br>
`git clone git://github.com/taher9990/wiregurard-bulk-generator.git` <br>
`mv get-pip.py wiregurard-bulk-generator`

## Configure the path for saving files:

Open app.conf.csv file and edit below line <br>
`cd wiregurard-bulk-generator`<br>
`vi app.conf.cs` <br>
`pathToHosts,"/home/ubuntu/wirguardConfigGen/csvdata.csv"`

## Start the installation of the pre-requisties
`apt install python3 -y`<br>
`apt install python3-distutils -y`<br>
`python3 get-pip.py`<br>

## Now run the generator 
`python3 Wireguard_ConfigGenerator.py`

#### Generated Config location:
####### Wireguard Config files:<br>
`~/generatedConfs/`<br>
####### Wireguard Config keys files: <br>
`~/keysArchive/`<br>


## Example
`$cat csvdata.csv`
<br>
Hostname,Public_FQDN,Public_Custom_Hostname,WireGuard_Subnet
<br>
PRD-INTERNAL-VLAN50-SRV1,PRD-INTERNAL-VLAN50-SRV1-P.EXAMPLE.COM,PRD-INTERNAL-VLAN50-SRV1-P,10.10.10.10/32
<br>
PRD-INTERNAL-VLAN50-SRV2,PRD-INTERNAL-VLAN50-SRV2-P.EXAMPLE.COM,PRD-INTERNAL-VLAN50-SRV2-P,10.10.10.11/32
<br>
PRD-INTERNAL-VLAN50-SRV3,PRD-INTERNAL-VLAN50-SRV3-P.EXAMPLE.COM,PRD-INTERNAL-VLAN50-SRV3-P,10.10.10.12/32
<br>
PRD-INTERNAL-VLAN50-SRV4,PRD-INTERNAL-VLAN50-SRV4-P.EXAMPLE.COM,PRD-INTERNAL-VLAN50-SRV4-P,10.10.10.13/32
<br>

`$python3 Wireguard_ConfigGenerator.py`

<br>
### Project Directories
<br>
├── Wireguard_ConfigGenerator.py
<br>
├── __init__.py
<br>
├── app.conf.csv
<br>
├── csvdata.csv
<br>
├── generatedConfs
<br>
│   ├── PRD-INTERNAL-VLAN50-SRV1-P
<br>
│   ├── PRD-INTERNAL-VLAN50-SRV2-P
<br>
│   ├── PRD-INTERNAL-VLAN50-SRV3-P
<br>
│   └── PRD-INTERNAL-VLAN50-SRV4-P
<br>
└── keysArchive
<br>
    ├── PRD-INTERNAL-VLAN50-SRV1-P
    <br>
    │   ├── privatekey
    <br>
    │   └── publickey
    <br>
    ├── PRD-INTERNAL-VLAN50-SRV2-P
    <br>
    │   ├── privatekey
    <br>
    │   └── publickey
    <br>
    ├── PRD-INTERNAL-VLAN50-SRV3-P
    <br>
    │   ├── privatekey
    <br>
    │   └── publickey
    <br>
    └── PRD-INTERNAL-VLAN50-SRV4-P
    <br>
        ├── privatekey
        <br>
        └── publickey
