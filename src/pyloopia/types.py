

class Type :
    '''
    Base class for types.
    '''

    def __init__(self, factory, **data) :
        self._factory = factory
        self._client = factory.client

        for k, v in data.items() :
            if hasattr(self, k) :
                setattr(self, k, v)

    def toArray(self) :
        vars = {}
        for k, v in self.__class__.__dict__.items() :
            if k.startswith('_') :
                continue
            if hasattr(self, k) :
                v = getattr(self, k)
            if not callable(v) :
                vars[k] = v
        return vars

    def __repr__(self):
        return str(self.toArray())


class Domain(Type) :

    name = None
    registered = None
    paid = 0
    reference_no = 0
    renewal_status = 0
    expiration_date = None
    subdomains = None

    def __init__(self, factory, **data) :
        self.subdomains = []
        super().__init__(factory, **data)

    # Get all subdomains for this domain.
    def getSubdomains(self) :
        if len(self.subdomains) < 1 :
            for sub in self._client.getSubdomains(self.name) :
                self.subdomains.append(self._factory.subdomain(self.name, sub))
        return self.subdomains

    # Add a subdomain to this domain.
    def addSubdomain(self, subdomain) :
        result = self._client.addSubdomain(self.name, subdomain)
        if result :
            return self._factory.subdomain(self.name, subdomain)
        return result


class Subdomain(Type) :

    _domain = None

    name = None
    zonerecords = None

    def __init__(self, factory, **data) :
        self.zonerecords = []
        super().__init__(factory, **data)

    # Get all zone records for this subdomain
    def getZoneRecords(self) :
        if len(self.zonerecords) < 1 :
            for data in self._client.getZoneRecords(self._domain, self.name) :
                self.zonerecords.append(self._factory.zonerecord(self._domain, self.name, data))
        return self.zonerecords


class ZoneRecord(Type) :

    _domain = None
    _subdomain = None

    record_id = None
    type = None
    ttl = 3600
    priority = 0
    rdata = None

    def create(self) :
        return self._client.addZoneRecord(self._domain, self._subdomain, self.toArray())

    def delete(self) :
        return self._client.deleteZoneRecord(self._domain, self._subdomain, self.id)

    def update(self) :
        return self._client.updateZoneRecord(self._domain, self._subdomain, self.toArray())

    def save(self) :
        # if we have a id, update.
        if self.record_id :
            return self.update()
        return self.create()
