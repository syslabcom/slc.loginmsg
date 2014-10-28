from Products.CMFPlone.utils import safe_unicode
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
    show_news_item = registry['slc.loginmsg.show_news_item']
    if show_news_item:
        cat = api.portal.get_tool('portal_catalog')
        items = cat(portal_type='News Item',
                    sort_on='created',
                    sort_order='reverse',
                    )
        if items:
            text = items[0].getObject().getText()
            pt = api.portal.get_tool('portal_transforms')
            message = pt.convertTo('text/plain', text).getData().strip()[:255]
            api.portal.show_message(safe_unicode(message), request=request)
