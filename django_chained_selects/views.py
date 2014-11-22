# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.db.models.loading import get_model
from django.http import JsonResponse
from django.utils import six
from django.views.generic.base import View


def filterchain_all(request, app_name, model_name, method_name, pk):
    Model = get_model(app_name, model_name)
    obj = Model.objects.get(pk=pk)
    qs = getattr(obj, method_name)()
    results = list(qs)
    return JsonResponse(
        [{'value': f.pk, 'display': six.text_type(f)} for f in results]
    )


class FilterChainView(View):
    def items(self):
        return [{'value': f.pk, 'display': six.text_type(f)} for f in results]
