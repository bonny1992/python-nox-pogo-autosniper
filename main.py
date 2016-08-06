from configreader import ConfigReader
from pokesnipereader import PokeSniperReader
from time import sleep


ConfigReaderObject = ConfigReader()
while True:
    if ConfigReaderObject.checkConfig() == True:
        break
Config = ConfigReaderObject.readConfig()
while True:
    JsonObject = PokeSniperReader(Config['snipe_urls'])
    PokeFounds = JsonObject.jsonLoader()
    if current_pkmns != PokeFounds:
        print ("N. pokemon found: " + str(len(PokeFounds)))
        for indices in PokeFounds:
            for data in indices:
                print('**********************************************************')
                print("Name: {}".format(str(data['name'])))
                print("Lat: {}".format(str(data['lat'])))
                print("Long: {}".format(str(data['lng'])))
    sleep(5)

