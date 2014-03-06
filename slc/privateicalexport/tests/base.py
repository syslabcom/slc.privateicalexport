# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone import api
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles


class PrivateIcalExportLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Prepare Zope instance by loading appropriate ZCMLs."""

        import slc.privateicalexport
        self.loadZCML(package=slc.privateicalexport)

    def setUpPloneSite(self, portal):
        """Prepare a Plone instance for testing."""
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'Products.CMFPlone:plone')

        # Install the privateicalexport profile
        self.applyProfile(portal, 'slc.privateicalexport:default')

        # Create test content
        # self.applyProfile(portal, 'slc.privateicalexport:testfixture')

        # Login as Manager
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)

        # Add some users
        editor = api.user.create(
            email="editor@example.com",
            username="editor",
            properties={"fullname": "An Editor"},
        )

    def tearDownZope(self, app):
        """Tear down Zope."""


FIXTURE = PrivateIcalExportLayer()
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="slc.privateicalexport:Functional")
