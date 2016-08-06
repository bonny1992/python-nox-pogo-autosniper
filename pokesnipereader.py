class PokeSniperReader:
    def __init__(self,json_urls):
        self.json_urls = json_urls
    def jsonLoader(self):
        snipeFound = []
        for url in self.json_urls:
            print("Reading json from {}".format(url))
            import json
            from urllib.request import Request, urlopen
            req = Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0'})
            jsonHandler = urlopen(req)
            print("Json read from {}".format(url))
            jsonDecoded = jsonHandler.read().decode()
            jsonData = json.loads(jsonDecoded)
            snipeFound.append(jsonData)
        return snipeFound
