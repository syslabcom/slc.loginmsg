from Products.PluggableAuthService.interfaces.events import IUserLoggedInEvent
from plone import api
from plone.registry.interfaces import IRegistry
from five import grok


@grok.subscribe(IUserLoggedInEvent)
def show_login_message(ev):
    request = api.portal.getRequest()
    registry = api.portal.getUtility(IRegistry)
    message = registry['slc.loginmsg.static_message']
    if message:
        api.portal.show_message(message, request=request)
