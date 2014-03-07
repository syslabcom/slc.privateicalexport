from plone.app.content.interfaces import INameFromTitle
from zope.interface import Interface
from zope.interface import implementer
from zope.component import adapter
import random


class INameFromUUID(Interface):
    pass

@adapter(INameFromUUID)
@implementer(INameFromTitle)
class NameFromUUID(object):

    def __init__(self, context):
        self.title = getattr(context, "_plone.uuid")
