# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.interface import Interface
from zope import schema


class ILoginMsgSettings(Interface):

    static_message = schema.TextLine(
        title=u"A static login message",
        default=u""
    )
