from daimaduan.bootstrap import db
from daimaduan.models import BaseDocument
from daimaduan.models.base import Paste


class Syntax(BaseDocument):
    name = db.StringField(required=True, unique=True)

    @property
    def pastes(self):
        return Paste.objects(codes__syntax=self.name)
