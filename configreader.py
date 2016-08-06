class ConfigReader:

    def __init__(self, filename='config.json'):
        self.filename = filename

    def readConfig(self):
        print ("Reading config file {}".format(self.filename))
        import json
        with open(self.filename, 'r') as f:
            config = json.load(f)
        if config is not None:
            print("Config file {} read successful".format(self.filename))
            return config
        else:
            return False

    def saveConfig(self):
        print("Saving config file {}".format(self.filename))
        import json
        config = {"snipe_urls":["http://pokezz.com/pokemons.json"],"use_blacklist":"false","use_whitelist":"false","whitelist":["Dragonite","Blastoise","Charizard","..."],"blacklist":["Rattata","Zubat","..."]}
        with open(self.filename, 'w+') as f:
            json.dump(config, f)
        print("Config file {} saved successful".format(self.filename))

    def checkConfig(self):
        print("Checking config file {}".format(self.filename))
        import os.path
        try:
            if not os.path.isfile(self.filename):
                self.saveConfig()
            with open(self.filename, 'r') as f:
                config_content = f.read()
            if config_content == None or config_content == '':
                self.saveConfig()
            return True
        except:
            return False