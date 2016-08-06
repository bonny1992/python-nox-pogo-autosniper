from configreader import ConfigReader
from pokesnipereader import PokeSniperReader
from time import sleep

ConfigReaderObject = ConfigReader()
while True:
    if ConfigReaderObject.checkConfig() == True:
        break
Config = ConfigReaderObject.readConfig()
while True:
    JsonObject = PokeSniperReader(Config['pokezz_address'])
    PokeFounds = JsonObject.jsonLoader()
    print ("Numero pokemon trovati: " + str(len(PokeFounds)))
    with open('E:\pokesnipes.txt', 'w+') as f:
        for data in PokeFounds:
            f.write('**********************************************************\n')
            f.write("Nome: " + str(data['name']) + '\n')
            f.write("Latitudine: " + str(data['lat']) + '\n')
            f.write("Longitudine: " + str(data['lng']) + '\n')
    sleep(10)

