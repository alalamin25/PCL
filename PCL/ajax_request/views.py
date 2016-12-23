# import datetime
from django.views import View


from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect
import json as simplejson
from master_table.models import Deport, FPItem


def return_json(data):
    if(data):
        data = data.name
    else:
        data = "Undefined"
    data = {'data': data}
    json = simplejson.dumps(data)
    return HttpResponse(json, content_type='application/javascript')

class FPItemView(View):

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        # json = {'data': ''}
        data = ""
        if(code):
            data = FPItem.objects.filter(code=code).first()
        # if(data):
        #     data = data.name
        # else:
        #     data = "Undefined"

        # # [action_list.append((each, each)) for each in choices]
        # print("data is: ")
        # print(data)
        # data = {'data': data}
        # json = simplejson.dumps(data)
        # # json = {'data': data}

        # print("\n\n in action choice method json is")
        # print(json)
        return return_json(data)

    def post(self, request, *args, **kwargs):
        pass


class DeportView(View):

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        # json = {'data': ''}
        data = "Undefined"
        if(code):
            data = Deport.objects.filter(code=code).first()

        if(data):
            data = data.name

        else:
            data = "Undefined"

        # [action_list.append((each, each)) for each in choices]
        print("data is: ")
        print(data)
        data = {'data': data}
        json = simplejson.dumps(data)
        # json = {'data': data}

        print("\n\n in action choice method json is")
        print(json)
        return HttpResponse(json, content_type='application/javascript')

    def post(self, request, *args, **kwargs):
        pass
