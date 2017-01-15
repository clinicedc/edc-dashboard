from ..url_mixins import ExtraQuerystringMixin, NextUrlMixin


class WrapperError(Exception):
    pass


class Wrapper(NextUrlMixin, ExtraQuerystringMixin):

    def __init__(self, obj):
        super().__init__()
        self._wrapped = True
        self._original_object = obj

    def object_url_wrapper(self, key=None, obj=None):
        obj.extra_querystring = self.get_extra_querystring(key=key, obj=obj)
        obj.next_url = self.get_next_url(key=key, obj=obj)
        return obj
