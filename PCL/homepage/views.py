from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/admin/login/')
def admin_home_page(request):

    return render(request, "homepage/admin_index.html")
