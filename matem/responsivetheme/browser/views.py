from Products.Collage.browser.views import BaseTopicView
from Products.Five import BrowserView

from plone import api
from smtplib import SMTPRecipientsRefused
from Products.CMFCore.interfaces import ISiteRoot
from zope.component import getUtility


class SliderBoxTopicView(BaseTopicView):

    def getValues(self, item):
        return''

    def hasImage(self, obj):
        if obj.getImage():
            return True
        return False

class ContactInfoIM(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        # self.id = 'contact-info-im'
        # self.form = None

    def __call__(self):
        form = self.request.form
        # if form:
        #     formkeys = form.keys()
        #     if 'acceptedbox' in formkeys:
        #         if 'selectapp' in formkeys:
        #             return self.printlist(form['acceptedbox'])
        #         else:
        #             self.accept_applications(form['acceptedbox'])
        #     elif 'emailbox' in formkeys:
        #         if 'email_option' in formkeys:
        #             self.send_advisor_email(form['emailbox'])
        return self.index()

    def changerecipient(self):
        return ''

    def test(self, condition, option1, option2):

        if condition:
            return option1

        return option2

    def send_email(self):

        encoding = getUtility(ISiteRoot).getProperty('email_charset', 'utf-8')

        mail_host = api.portal.get_tool(name='MailHost')
        m_to = ''
        m_from = ''
        subject = ''

        mail_text = ""

        try:
            mail_host.send(mail_text, m_to, m_from, subject=subject, charset=encoding, immediate=True)
        except SMTPRecipientsRefused:
            # Don't disclose email address on failure
            # raise SMTPRecipientsRefused('Recipient address rejected by server')
            raise SMTPRecipientsRefused('Recipient address rejected by server')
