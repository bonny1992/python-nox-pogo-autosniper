class PokeSniperReader:
    def __init__(self,json_url):
        self.json_url = json_url
    def jsonLoader(self):
        print("Reading json from {}".format(self.json_url))
        import json
        from urllib.request import Request, urlopen
        req = Request(
            self.json_url,
            headers={'User-Agent': 'Mozilla/5.0'})
        jsonHandler = urlopen(req)
        print("Json read from {}".format(self.json_url))
        jsonDecoded = jsonHandler.read().decode()
        jsonData = json.loads(jsonDecoded)
        return jsonData
