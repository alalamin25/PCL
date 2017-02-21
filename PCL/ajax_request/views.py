# import datetime
from django.views import View


from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect
import json as simplejson
from master_table.models import Deport, FPItem
from sales.models import SellDetailInfo


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


class DeportReturnView(View):

    def get(self, request, *args, **kwargs):
        memo_no = request.GET.get('memo_no')
        product_id = request.GET.get('product_id')
        # json = {'data': ''}
        print(memo_no)
        data = ""
        if(memo_no):
            data = SellDetailInfo.objects.filter(sell__memo_no=memo_no, product_code__id=product_id).first()
            print(data)
        if(data):
            data = data.rate
        else:
            data = -1
        data = {'data': data}
        json = simplejson.dumps(data)
        return HttpResponse(json, content_type='application/javascript')

    def post(self, request, *args, **kwargs):
        pass
