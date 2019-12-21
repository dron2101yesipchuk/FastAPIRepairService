class Device:
    id: int
    name: str
    issue: str

    def __init__(self, id, name, issue):
        self.id = id
        self.name = name
        self.issue = issue

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.issue
        }

    def __repr__(self):
        return str(self.__dict__)