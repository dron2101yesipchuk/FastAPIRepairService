class Device:
    def __init__(self, id, name, issue):
        self._id = id
        self._name = name
        self._issue = issue

    def getid(self):
        return self._id

    def setid(self, id):
        self._id = id

    def getname(self):
        return self._name

    def setname(self, name):
        self._name = name

    def getissue(self):
        return self._issue

    def setissue(self, issue):
        self._issue = issue

    id = property(getid, setid)
    name = property(getname, setname)
    issue = property(getissue, setissue)

