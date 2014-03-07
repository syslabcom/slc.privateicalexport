from plone.app.content.interfaces import INameFromTitle
from zope.interface import Interface
from zope.interface import implements
from zope.component import adapts
import random


class INameFromUUID(Interface):
    pass

class NameFromUUID(object):
    implements(INameFromTitle)
    adapts(INameFromUUID)

    def __init__(self, context):
        self.title = getattr(context, "_plone.uuid")
