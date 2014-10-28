import unittest2 as unittest
from Products.PlonePAS.events import UserLoggedInEvent
from Testing.makerequest import makerequest
from plone import api
from plone.registry.interfaces import IRegistry
from zope.event import notify

from slc.loginmsg.testing import IntegrationTestCase


class TestSetMessage(IntegrationTestCase):
    def setUp(self):
        mt = api.portal.get_tool('portal_membership')
        self.user = mt.getAuthenticatedMember()
        self.request = makerequest(self.layer['app']).REQUEST
        self.status_messages = api.portal.IStatusMessage(self.request)
        self.registry = api.portal.getUtility(IRegistry)

    def test_no_message(self):
        notify(UserLoggedInEvent(self.user))
        messages = self.status_messages.show()
        self.assertEqual(len(messages), 0)

    def test_static_message(self):
        self.registry['slc.loginmsg.static_message'] = u'Welcome!'
        notify(UserLoggedInEvent(self.user))
        messages = self.status_messages.show()
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, u'Welcome!')
