# -*- coding: utf-8 -*-

from acentoweb.collectionactions import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.vocabularies.catalog import CatalogSource


class ICollectionCopyMarker(Interface):
    pass

@provider(IFormFieldProvider)
class ICollectionCopy(model.Schema):
    """
    """

    project = RelationChoice(
         title=_(u'linked_folder'),
         description=_(u'Folder to move items to'),
         required=False,
         vocabulary='plone.app.vocabularies.Catalog',
    )



@implementer(ICollectionCopy)
@adapter(ICollectionCopyMarker)
class CollectionCopy(object):
    def __init__(self, context):
        self.context = context

    @property
    def project(self):
        if hasattr(self.context, 'project'):
            return self.context.project
        return None

    @project.setter
    def project(self, value):
        self.context.project = value
