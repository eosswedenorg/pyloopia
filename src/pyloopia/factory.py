
from .types import Domain, Subdomain, ZoneRecord


class Factory :

    def __init__(self, client) :
        self.client = client

    def domain(self, data) :
        return Domain(self,
            name=data["domain"],
            registered=data['registered'])

    def subdomain(self, domain, subdomain) :
        return Subdomain(self, _domain=domain, name=subdomain)

    def zonerecord(self, domain, subdomain, data) :
        return ZoneRecord(self, _domain=domain, _subdomain=subdomain, **data)
