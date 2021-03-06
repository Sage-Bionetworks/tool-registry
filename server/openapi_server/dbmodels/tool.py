from mongoengine import StringField, URLField

from openapi_server.dbmodels.base_document import BaseDocument  # noqa: E501


class Tool(BaseDocument):
    name = StringField(required=True, unique=True)
    version = StringField()
    license = StringField()
    repository = StringField()
    description = StringField()
    author = StringField()  # TODO: Replace by object
    authorEmail = StringField()
    url = URLField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
