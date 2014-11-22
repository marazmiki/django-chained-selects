# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.forms.widgets import Select
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.safestring import mark_safe
import django


if django.VERSION >= (1, 2, 0) and getattr(
        settings,
        'USE_DJANGO_JQUERY', True):
    USE_DJANGO_JQUERY = True
else:
    USE_DJANGO_JQUERY = False
    JQUERY_URL = getattr(settings, 'JQUERY_URL', 'http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js')

URL_PREFIX = getattr(settings, "CHAINED_SELECTS_URL_PREFIX", "")


class ChainedSelectWidget(Select):
    def __init__(self, parent_name, app_name, model_name, method_name=None,
                 *args, **kwargs):
        self.parent_name = parent_name
        self.app_name = app_name
        self.model_name = model_name
        self.method_name = method_name
        super(ChainedSelectWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, choices=()):
        url = reverse('filter_all', kwargs={'app_name': self.app_name,
                                            'model_name': self.model_name,
                                            'method_name': self.method_name,
                                            'pk': '$pk$'})
        attrs = attrs or {}
        attrs.update(**{
            'data-parent-id': 'id_%s' % self.parent_name,  # @TODO rm hardcoded
            'data-url': mark_safe(url),
            'data-empty-label': '---------',               # @TODO rm hardcoded
            'class': 'chained'
        })
        # print(name, value, 'choices=',choices)
        output = super(ChainedSelectWidget, self).render(name, value, attrs, choices)
        return mark_safe(output)

    class Media(object):
        js = ()

        if USE_DJANGO_JQUERY:
            js += (
                static('admin/js/jquery.min.js'),
                static('admin/js/jquery.init.js'),
            )
        elif JQUERY_URL:
            js += (
                JQUERY_URL,
            )
        js += (
            static('chained_selects/delayed_fill.js'),
        )
