from Products.Collage.browser.views import BaseTopicView
from Products.Five import BrowserView


class SliderBoxTopicView(BaseTopicView):

    def getValues(self, item):
        return''

    def hasImage(self, obj):
        if obj.getImage():
            return True
        return False

class ContactInfoIM(BrowserView):

    def changerecipient(self):
        return ''
