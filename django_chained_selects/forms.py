# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django_chained_selects.widgets import ChainedSelectWidget


class ChainedSelectsFormMixin(object):
    def __init__(self, *args, **kwargs):
        super(ChainedSelectsFormMixin, self).__init__(*args, **kwargs)
        self.hide_empty_querysets()
        self.patch_widgets()

    def get_chained_selects(self):
        if not hasattr(self, 'ChainedSelectsMeta'):
            return []
        chains = getattr(self.ChainedSelectsMeta, 'chains', [])
        return {k: v for k, v in chains.items()}

    def hide_empty_querysets(self):
        if self.data:
            return
        for field in self.get_chained_selects():
            self.fields[field].queryset = self.fields[field].queryset.none()

    def patch_widgets(self):
        for field_name, parent_name in self.get_chained_selects().items():
            field = self.fields[field_name]
            model = field.queryset.model
            parent_model = self.fields[parent_name].queryset.model
            print("patch field %s" % field_name, field.queryset)
            field.widget = ChainedSelectWidget(
                parent_name=parent_name,
                app_name=model._meta.app_label,
                model_name=parent_model._meta.model_name,
                method_name='chained_relation',      # the name of queryset method
                choices=field.queryset,
            )
