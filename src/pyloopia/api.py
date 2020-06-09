
from .client import Client
from .factory import Factory

class api :
    _client = None
    _factory = None

    def __init__(self, username, password) :
        self._client = Client(username, password)
        self._factory = Factory(self._client)

    def getDomains(self) :
        ret = []
        for data in self._client.getDomains() :
            ret.append(self._factory.domain(data))
        return ret

    def getDomain(self, name) :
        data = self._client.getDomain(name)
        return self._factory.domain(data)

    def getSubdomain(self, domain, subdomain = "@") :
        domain = self.getDomain(domain)
        if domain :
            for sub in domain.getSubdomains() :
                if sub.name == subdomain :
                    return sub
        return None
