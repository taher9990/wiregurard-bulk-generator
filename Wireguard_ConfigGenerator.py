import csv
import os


def generateKeys(keysRepoName, x, keyGenBashCmd):
    try:
        os.makedirs(keysRepoName)
    except:
        pass
    try:
        os.chdir(keysRepoName)
        os.makedirs(x[2])
    except:
        print(f"Skipping {x[2]} already exists. ")
    os.chdir(x[2])
    os.system(keyGenBashCmd)
    os.chdir("../..")
    #


def readEntriesList(pathToHosts):
    with open(pathToHosts, 'r') as file:
        reader = csv.reader(file)
        pageSet = [row for row in reader]
    return pageSet[1:]


def confGrabber(confFile):
    pageSet = {}
    with open(confFile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:
                pageSet[row[0]] = row[1]
    return pageSet


if __name__ == '__main__':
    keyGenBashCmd = confGrabber("app.conf.csv")["keyGenBashCmd"]
    pathToHosts = confGrabber("app.conf.csv")["pathToHosts"]
    generatedConfsPath = confGrabber("app.conf.csv")["generatedConfsPath"]
    keysRepoName = confGrabber("app.conf.csv")["keysRepoName"]

    # TODO read csv file to be filled from
    entries = readEntriesList(pathToHosts)

    # TODO generate the keys and files
    for x in entries:
        generateKeys(keysRepoName, x, keyGenBashCmd)

    # TODO read keys to JSON
    allData = {}
    for x in entries:
        allData[x[2]] = {
            "Alias": f"{x[2]}",
            "Description": f"{x[2]}",
            "PrivateKey": "",
            "PublicKey": "",
            "Address": f"{x[3]}",
            "ListenPort": "45987",
        }
    for x in os.listdir(keysRepoName):
        with open(f"{keysRepoName}/{x}/privatekey", "r") as privateKeyData:
            allData[x]["PrivateKey"] = privateKeyData.read()
        with open(f"{keysRepoName}/{x}/publickey", "r") as publicKeyData:
            allData[x]["PublicKey"] = publicKeyData.read()

    # TODO generate configs
    for x in allData:
        allData[x]["interfaceBlock"] = f'[Interface]\n' \
                                       f'# Alias:  {allData[x]["Alias"]}\n' \
                                       f'# Description:  {allData[x]["Description"]}\n' \
                                       f'PrivateKey = {allData[x]["PrivateKey"]}\n' \
                                       f'Address = {allData[x]["Address"]}\n' \
                                       f'ListenPort = {allData[x]["ListenPort"]}'
        allData[x]["peerBlock"] = f'\n[Peer]\n' \
                                  f'# Alias: {allData[x]["Alias"]}\n' \
                                  f'# Description: {allData[x]["Description"]}\n' \
                                  f'PublicKey =  {allData[x]["PublicKey"]}\n' \
                                  f'AllowedIPs =  {allData[x]["Address"]}\n' \
                                  f'Endpoint =  {allData[x]["Alias"]}:{allData[x]["ListenPort"]}\n' \
                                  f'PersistentKeepalive = 25'

    try:
        os.makedirs(generatedConfsPath)
    except:
        pass

    for x in allData:
        fileData = allData[x]["interfaceBlock"] + "\n"
        for y in allData:
            if x != y:
                fileData += allData[y]["peerBlock"] + "\n"
        allData[x]["fileData"] = fileData
        with open(generatedConfsPath + "/" + x, "w") as fileOut:
            fileOut.write(fileData)
