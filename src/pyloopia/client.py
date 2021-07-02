
from .exceptions import AuthException, DomainOccupiedException, RateLimitException, BadIndataException, UnknownException
from xmlrpc.client import ServerProxy as XMLRPC_Client


class Client :

    def __init__(self, username, password) :
        self._username = username
        self._password = password
        self._xmlrpc = XMLRPC_Client(
            uri='https://api.loopia.se/RPCSERV',
            encoding='utf-8',
            allow_none=True
        )

    def call(self, resource, *args) :

        # Get the api function
        func = getattr(self._xmlrpc, resource)

        # Call the api and get the response
        response = func(self._username, self._password, *args)

        # Check if the response could be an error.
        if type(response) is list and len(response) == 1 and type(response[0]) is str  :
            code = response[0]

            # Handle reponse codes.
            if code == "OK" :
                return True
            elif code == 'AUTH_ERROR' :
                raise AuthException()
            elif code == 'DOMAIN_OCCUPIED' :
                raise DomainOccupiedException()
            elif code == 'RATE_LIMITED' :
                raise RateLimitException()
            elif code == 'BAD_INDATA' :
                raise BadIndataException()
            elif code == 'UNKNOWN_ERROR' :
                raise UnknownException()

        return response

    def getDomains(self) :
        return self.call("getDomains")

    def getDomain(self, name) :
        return self.call("getDomain", name)

    def addDomain(self, name) :
        return self.call("addDomain", name)

    def getSubdomains(self, domain) :
        return self.call("getSubdomains", domain)

    def addSubdomain(self, domain, subdomain) :
        return self.call("addSubdomain", domain, subdomain)

    '''
    Zone records
    '''

    def getZoneRecords(self, domain, subdomain=None) :
        if subdomain is None :
            return self.call("getZoneRecords", domain)
        return self.call("getZoneRecords", domain, subdomain)

    def addZoneRecord(self, domain, subdomain, record) :
        return self.call("addZoneRecord", domain, subdomain, record)

    def removeZoneRecord(self, domain, subdomain, record_id) :
        return self.call("removeZoneRecord", domain, subdomain, record_id)

    def updateZoneRecord(self, domain, subdomain, record) :
        return self.call("updateZoneRecord", domain, subdomain, record)
