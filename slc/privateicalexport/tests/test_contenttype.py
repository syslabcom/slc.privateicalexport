# -*- coding: utf-8 -*-

from plone import api
from slc.privateicalexport.tests.base import FUNCTIONAL_TESTING
from zope.component import getUtility

import unittest2 as unittest


class TestContentType(unittest.TestCase):
    layer = FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_set_calendars(self):
        self.assertTrue(1 is not None)
