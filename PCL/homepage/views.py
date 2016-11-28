from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def index_page(request):

    return render(request, "homepage/index_page.html")


@login_required(login_url='/admin/login/')
def admin_home_page(request):

    return render(request, "homepage/admin_home_page.html")