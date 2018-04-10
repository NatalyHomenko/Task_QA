import json
import requests

default = 'application/json'

class ServerAPI:

    def showAll(self):
        r = requests.get('http://qainterview.cogniance.com/candidates')
        return r

    def showId(self, id):
        r = requests.get('http://qainterview.cogniance.com/candidates/' + str(id))
        return r

    def add(self, name, position, headers=default):
        _headers = {'content-type': headers}
        _payload = {'name': str(name), 'position': str(position)}
        r = requests.post('http://qainterview.cogniance.com/candidates', data=json.dumps(_payload), headers=_headers)
        return r

    def delete(self, id):
        r = requests.delete('http://qainterview.cogniance.com/candidates/' + str(id))
        return r
