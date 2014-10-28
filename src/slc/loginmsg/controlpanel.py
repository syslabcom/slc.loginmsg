from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from slc.loginmsg.interfaces import ILoginMsgSettings
from plone.z3cform import layout
from z3c.form import form


class LoginMsgControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = ILoginMsgSettings
    schema_prefix = "slc.loginmsg"

LoginMsgControlPanelView = layout.wrap_form(
    LoginMsgControlPanelForm, ControlPanelFormWrapper)
LoginMsgControlPanelView.label = u"Login message settings"
