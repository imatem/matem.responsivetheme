from Products.Collage.browser.views import BaseTopicView


class SliderBoxTopicView(BaseTopicView):

    def getValues(self, item):
        return''

    def hasImage(self, obj):
        if obj.getImage():
            return True
        return False
