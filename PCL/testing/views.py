from io import BytesIO
from datetime import timedelta
from reportlab.pdfgen import canvas
import json
import datetime


from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.db.models import Sum
import json as simplejson


def action_choices(request):
    action_list = []
    ChoiceA = ("on-false", "on-true")
    ChoiceB = ("always", "never")

    action_type = request.GET.get('action_type')
    if str(action_type).lower() == 'a':
        choices = ChoiceA
    elif str(action_type).lower() == 'b':
        choices = ChoiceB
    elif str(action_type).lower() == 'alamin':
    	choices = ("Almerciful", "Allah")
    else:
        choices = ("alamin", "lia")

    [action_list.append((each, each)) for each in choices]
    json = simplejson.dumps(action_list)
    print("\n\n in action choice method json is")
    print(json)
    return HttpResponse(json, content_type='application/javascript')
