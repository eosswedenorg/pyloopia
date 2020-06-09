
from .exceptions import *
from xmlrpc.client import ServerProxy as XMLRPC_Client

class Client :

    def __init__(self, username, password) :
        self._username   = username
        self._password   = password
        self._xmlrpc     = XMLRPC_Client(
            uri = 'https://api.loopia.se/RPCSERV',
            encoding = 'utf-8',
            allow_none = True
        )

    def call(self, resource, *args) :

        # Get the api function
        func = getattr(self._xmlrpc, resource)

        # Call the api and get the response
        response = func(self._username, self._password, *args)

        # Handle reponse codes.
        if response == "OK" :
            return True
        elif response == 'AUTH_ERROR' :
            raise AuthException();
        elif response == 'DOMAIN_OCCUPIED' :
            raise DomainOccupiedException()
        elif response == 'RATE_LIMITED' :
            raise RateLimitException()
        elif response == 'BAD_INDATA' :
            raise BadIndataException()
        elif response == 'UNKNOWN_ERROR' :
            raise UnknownException()

        return response

    def getDomains(self) :
        return self.call("getDomains")

    def getDomain(self, name) :
        return self.call("getDomain", name)

    def getSubdomains(self, domain) :
        return self.call("getSubdomains", domain)

    '''
    Zone records
    '''

    def getZoneRecords(self, domain, subdomain = None) :
        if subdomain == None :
            return self._xmlrpc.getZoneRecords(self._username, self._password, domain)
        return self._xmlrpc.getZoneRecords(self._username, self._password, domain, subdomain)

    def addZoneRecord(self, domain, subdomain, record) :
        return self._xmlrpc.addZoneRecord(self._username, self._password, domain, subdomain, record)

    def removeZoneRecord(self, domain, subdomain, record_id) :
        return self._xmlrpc.removeZoneRecord(self._username, self._password, domain, subdomain, record_id)

    def updateZoneRecord(self, domain, subdomain, record) :
        return self._xmlrpc.updateZoneRecord(self._username, self._password, domain, subdomain, record)
